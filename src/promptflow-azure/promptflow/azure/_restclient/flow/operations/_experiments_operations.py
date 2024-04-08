# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.8.0, generator: @autorest/python@5.13.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_submit_experiment_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    experiment_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    experiment_name = kwargs.pop('experiment_name', None)  # type: Optional[str]
    description = kwargs.pop('description', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/Experiments/{experimentId}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "experimentId": _SERIALIZER.url("experiment_id", experiment_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if experiment_name is not None:
        _query_parameters['experimentName'] = _SERIALIZER.query("experiment_name", experiment_name, 'str')
    if description is not None:
        _query_parameters['description'] = _SERIALIZER.query("description", description, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_experiment_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    experiment_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/Experiments/{experimentId}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "experimentId": _SERIALIZER.url("experiment_id", experiment_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_resubmit_experiment_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    experiment_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/Experiments/{experimentId}/resubmit")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "experimentId": _SERIALIZER.url("experiment_id", experiment_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_resubmit_experiment_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    experiment_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/Experiments/{experimentId}/resubmit')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str'),
        "experimentId": _SERIALIZER.url("experiment_id", experiment_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class ExperimentsOperations(object):
    """ExperimentsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~flow.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def submit_experiment(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        experiment_id,  # type: str
        experiment_name=None,  # type: Optional[str]
        description=None,  # type: Optional[str]
        body=None,  # type: Optional["_models.SubmitExperimentRequest"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FlowDto"
        """submit_experiment.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param experiment_id:
        :type experiment_id: str
        :param experiment_name:  Default value is None.
        :type experiment_name: str
        :param description:  Default value is None.
        :type description: str
        :param body:  Default value is None.
        :type body: ~flow.models.SubmitExperimentRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FlowDto, or the result of cls(response)
        :rtype: ~flow.models.FlowDto
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FlowDto"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'SubmitExperimentRequest')
        else:
            _json = None

        request = build_submit_experiment_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            experiment_id=experiment_id,
            content_type=content_type,
            json=_json,
            experiment_name=experiment_name,
            description=description,
            template_url=self.submit_experiment.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('FlowDto', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    submit_experiment.metadata = {'url': "/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/Experiments/{experimentId}"}  # type: ignore


    @distributed_trace
    def get_experiment(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        experiment_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ExperimentDefinition"
        """get_experiment.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param experiment_id:
        :type experiment_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExperimentDefinition, or the result of cls(response)
        :rtype: ~flow.models.ExperimentDefinition
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ExperimentDefinition"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_experiment_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            experiment_id=experiment_id,
            template_url=self.get_experiment.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ExperimentDefinition', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_experiment.metadata = {'url': "/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/Experiments/{experimentId}"}  # type: ignore


    @distributed_trace
    def resubmit_experiment(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        experiment_id,  # type: str
        body=None,  # type: Optional["_models.ResubmitExperimentRequest"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FlowDto"
        """resubmit_experiment.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param experiment_id:
        :type experiment_id: str
        :param body:  Default value is None.
        :type body: ~flow.models.ResubmitExperimentRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FlowDto, or the result of cls(response)
        :rtype: ~flow.models.FlowDto
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FlowDto"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'ResubmitExperimentRequest')
        else:
            _json = None

        request = build_resubmit_experiment_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            experiment_id=experiment_id,
            content_type=content_type,
            json=_json,
            template_url=self.resubmit_experiment.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('FlowDto', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    resubmit_experiment.metadata = {'url': "/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/Experiments/{experimentId}/resubmit"}  # type: ignore


    @distributed_trace
    def resubmit_experiment(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        experiment_id,  # type: str
        body=None,  # type: Optional["_models.ResubmitExperimentRequest"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FlowDto"
        """resubmit_experiment.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param experiment_id:
        :type experiment_id: str
        :param body:
        :type body: ~flow.models.ResubmitExperimentRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FlowDto, or the result of cls(response)
        :rtype: ~flow.models.FlowDto
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FlowDto"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'ResubmitExperimentRequest')
        else:
            _json = None

        request = build_resubmit_experiment_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            experiment_id=experiment_id,
            content_type=content_type,
            json=_json,
            template_url=self.resubmit_experiment.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('FlowDto', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    resubmit_experiment.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/Experiments/{experimentId}/resubmit'}  # type: ignore

