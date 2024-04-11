import multiprocessing
import os
import subprocess
from pathlib import Path


class RunMode:
    COMPUTE = "compute"
    SERVING = "serving"


def get_process_num() -> int:
    """Get process number of server based on CPU core num."""

    worker_num_env = "PROMPTFLOW_WORKER_NUM"
    worker_num = os.getenv(worker_num_env)
    cpu_core_num = multiprocessing.cpu_count()
    try:
        if worker_num is None:
            print(f"The promptflow worker number not set, setting {worker_num_env} to CPU core number: {cpu_core_num}")
            return cpu_core_num
        else:
            worker_num = int(worker_num)
            max_process = cpu_core_num * 2
            if worker_num > max_process:
                print(
                    "The promptflow worker number is too large, "
                    f"setting {worker_num_env} to (2 * the number of cores) = {max_process}"
                )
                return max_process
            else:
                return worker_num
    except Exception as e:
        print(f"Invalid value for {worker_num_env}. It must be an integer. Error: {e}")
        return cpu_core_num


def is_pf_model(model_dir: Path) -> bool:
    """
    Check whether a given model_dir contains 'MLmodel' file or 'flow.dag.yaml'.
    """
    return model_dir.joinpath("MLmodel").exists() or model_dir.joinpath("flow.dag.yaml").exists()


def get_run_mode() -> str:
    """Get PROMPTFLOW_RUN_MODE for pf serving scenario."""

    run_mode = os.getenv("PROMPTFLOW_RUN_MODE")
    if not run_mode:
        print("Detecting promptflow run mode...")
        model_dir = os.getenv("AZUREML_MODEL_DIR")
        pf_project_path = os.getenv("PROMPTFLOW_PROJECT_PATH")
        if not model_dir and not pf_project_path:
            run_mode = RunMode.COMPUTE
        elif model_dir:
            # Check model file to determine if it is MIR serving deployment or runtime deployment.
            # will remove this once we didn't support MIR runtime for both 1P & 3P.
            model_dir = Path(model_dir)
            if is_pf_model(model_dir):
                run_mode = RunMode.SERVING
            elif len(list(model_dir.iterdir())) == 1 and is_pf_model(list(model_dir.iterdir())[0]):
                # Only has one sub dir, it is a model deployment
                run_mode = RunMode.SERVING
            else:
                run_mode = RunMode.COMPUTE
        else:
            # If PROMPTFLOW_PROJECT_PATH is set, this is a serving environment
            run_mode = RunMode.SERVING

    print(f"Promptflow run mode: {run_mode}")
    return run_mode


def start_server():
    """Start promptflow server based on run mode."""

    print(f"The build info of image: {os.getenv('BUILD_INFO')}")
    run_mode = get_run_mode()
    if run_mode == RunMode.SERVING:
        worker_num = str(get_process_num())
        worker_threads = os.getenv("PROMPTFLOW_WORKER_THREADS", "1")
        gunicorn_app = "promptflow.core._serving.app:create_app(extension_type='azureml')"
        print(
            f"Start promptflow serving server with worker_num: {worker_num}, "
            f"worker_threads: {worker_threads}, app: {gunicorn_app}"
        )
        subprocess.run(
            [
                "gunicorn",
                "-w",
                worker_num,
                "--threads",
                worker_threads,
                "-b",
                "0.0.0.0:8080",
                "--timeout",
                "300",
                gunicorn_app,
            ]
        )
    else:
        host = os.getenv("HOST", "0.0.0.0")
        port = os.getenv("PORT", "8000")
        uvicorn_app = "promptflow.executor._service.app:app"
        print(f"Start promptflow python server with app: {uvicorn_app}")
        subprocess.run(["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-b", f"{host}:{port}", uvicorn_app])


start_server()
