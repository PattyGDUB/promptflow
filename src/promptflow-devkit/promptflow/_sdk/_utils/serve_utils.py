import abc
import logging
import multiprocessing
import os
import platform
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import webbrowser
from pathlib import Path
from typing import Any, Dict, Optional

from promptflow._constants import FlowLanguage
from promptflow._proxy._csharp_inspector_proxy import EXECUTOR_SERVICE_DLL
from promptflow._sdk._constants import OSType
from promptflow._utils.flow_utils import resolve_flow_path

logger = logging.getLogger(__name__)


def find_available_port() -> str:
    """Find an available port on localhost"""
    # TODO: replace find_available_port in CSharpExecutorProxy with this one
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        _, port = s.getsockname()
        return str(port)


def _resolve_python_flow_additional_includes(source) -> Path:
    # Resolve flow additional includes
    from promptflow.client import load_flow

    flow = load_flow(source)
    from promptflow._sdk.operations import FlowOperations

    with FlowOperations._resolve_additional_includes(flow.path) as resolved_flow_path:
        if resolved_flow_path == flow.path:
            return source
        # Copy resolved flow to temp folder if additional includes exists
        # Note: DO NOT use resolved flow path directly, as when inner logic raise exception,
        # temp dir will fail due to file occupied by other process.
        temp_flow_path = Path(tempfile.TemporaryDirectory().name)
        shutil.copytree(src=resolved_flow_path.parent, dst=temp_flow_path, dirs_exist_ok=True)

    return temp_flow_path


def start_flow_service(
    language: str,
    *,
    flow_dir: Path,
    static_folder: str = None,
    host: str = "localhost",
    port: int = 8080,
    config: dict = None,
    environment_variables: Dict[str, str] = None,
    init: Dict[str, Any] = None,
    skip_open_browser: bool = True,
):
    logger.info(
        "Start promptflow server with port %s",
        port,
    )
    os.environ["PROMPTFLOW_PROJECT_PATH"] = flow_dir.absolute().as_posix()
    if language == FlowLanguage.Python:
        helper = PythonFlowServiceHelper(
            static_folder=static_folder,
            flow_dir=flow_dir,
            host=host,
            port=port,
            config=config or {},
            environment_variables=environment_variables or {},
            init=init or {},
            skip_open_browser=skip_open_browser,
        )
    else:
        helper = CSharpFlowServiceHelper(
            flow_dir=flow_dir,
            port=port,
        )
    helper.run()


class BaseFlowServiceHelper:
    def __init__(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def start_in_subprocess(self):
        pass

    @abc.abstractmethod
    def terminate_subprocess(self):
        pass

    @classmethod
    def create_simple(cls, language, flow_dir, port):
        if language == FlowLanguage.CSharp:
            return CSharpFlowServiceHelper(
                flow_dir=flow_dir,
                port=port,
            )
        # use else so that Prompty will also go this path
        return PythonFlowServiceHelper(
            static_folder=None,
            flow_dir=flow_dir,
            host="localhost",
            port=port,
            config={},
            environment_variables={},
            init={},
            skip_open_browser=True,
        )


class PythonFlowServiceHelper(BaseFlowServiceHelper):
    def __init__(self, static_folder, flow_dir, host, port, config, environment_variables, init, skip_open_browser):
        self._static_folder = static_folder
        self.flow_dir = flow_dir
        self.host = host
        self.port = port
        self.config = config
        self.environment_variables = environment_variables
        self.init = init
        self.skip_open_browser = skip_open_browser
        super().__init__()

        self._subprocess: Optional[multiprocessing.Process] = None

    @property
    def static_folder(self):
        if self._static_folder is None:
            return None
        return Path(self._static_folder).absolute().as_posix()

    def run(self):
        from promptflow._sdk._configuration import Configuration
        from promptflow.core._serving.app import create_app

        pf_config = Configuration(overrides=self.config)
        logger.info(f"Promptflow config: {pf_config}")
        connection_provider = pf_config.get_connection_provider()
        flow_dir = _resolve_python_flow_additional_includes(self.flow_dir)
        os.environ["PROMPTFLOW_PROJECT_PATH"] = flow_dir.absolute().as_posix()
        logger.info(f"Change working directory to model dir {flow_dir}")
        os.chdir(flow_dir)
        app = create_app(
            static_folder=self.static_folder,
            environment_variables=self.environment_variables,
            connection_provider=connection_provider,
            init=self.init,
        )
        if not self.skip_open_browser:
            target = f"http://{self.host}:{self.port}"
            logger.info(f"Opening browser {target}...")
            webbrowser.open(target)
        # Debug is not supported for now as debug will rerun command, and we changed working directory.
        app.run(port=self.port, host=self.host)

    def start_in_subprocess(self):
        self._subprocess = multiprocessing.Process(target=self.run)
        self._subprocess.start()

    def terminate_subprocess(self):
        if self._subprocess is not None:
            self._subprocess.terminate()
            self._subprocess.join()


class CSharpFlowServiceHelper(BaseFlowServiceHelper):
    def __init__(self, flow_dir, port):
        self.port = port
        self.flow_dir, self.flow_file_name = resolve_flow_path(flow_dir)
        super().__init__()

        self._process: Optional[subprocess.Popen] = None

    def _construct_command(self):
        return [
            "dotnet",
            EXECUTOR_SERVICE_DLL,
            "--port",
            str(self.port),
            "--yaml_path",
            self.flow_file_name,
            "--assembly_folder",
            ".",
            "--connection_provider_url",
            "",
            "--log_path",
            "",
            "--serving",
        ]

    def run(self):
        try:
            command = self._construct_command()
            subprocess.run(command, cwd=self.flow_dir, stdout=sys.stdout, stderr=sys.stderr)
        except KeyboardInterrupt:
            pass

    def start_in_subprocess(self):
        self._process = subprocess.Popen(
            args=self._construct_command(),
            cwd=self.flow_dir,
        )

    def terminate_subprocess(self):
        if platform.system() == OSType.WINDOWS:
            # send CTRL_C_EVENT to the process to gracefully terminate the service so that we can gather complete trace
            self._process.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            # for Linux and MacOS, Popen.terminate() will send SIGTERM to the process
            self._process.terminate()

        try:
            self._process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self._process.kill()
