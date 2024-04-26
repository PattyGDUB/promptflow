import os

import pytest
from azure.identity import DefaultAzureCredential

from promptflow.evals.synthetic import AdversarialSimulator


@pytest.mark.usefixtures(
    "model_config", "recording_injection", "ml_client_config", "configure_default_azure_credential"
)
@pytest.mark.e2etest
class TestAdvSimulator:
    def test_adv_sim_init(self, model_config, ml_client_config):
        os.environ["rai_svc_url"] = "https://int.api.azureml-test.ms"
        template = "adv_conversation"
        project_scope = {
            "subscription_id": ml_client_config["subscription_id"],
            "resource_group_name": ml_client_config["resource_group_name"],
            "workspace_name": ml_client_config["project_name"],
            "credential": DefaultAzureCredential(),
        }
        simulator = AdversarialSimulator(template=template, project_scope=project_scope)
        assert callable(simulator)
