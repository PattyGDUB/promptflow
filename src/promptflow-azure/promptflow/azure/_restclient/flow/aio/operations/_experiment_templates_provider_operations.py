# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.8.0, generator: @autorest/python@5.13.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._experiment_templates_provider_operations import build_get_index_entity_by_id_request, build_get_updated_entity_ids_for_workspace_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ExperimentTemplatesProviderOperations:
    """ExperimentTemplatesProviderOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_index_entity_by_id(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        body: Optional["_models.UnversionedEntityRequestDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject"] = None,
        **kwargs: Any
    ) -> "_models.UnversionedEntityResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject":
        """get_index_entity_by_id.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param body:  Default value is None.
        :type body:
         ~flow.models.UnversionedEntityRequestDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return:
         UnversionedEntityResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject,
         or the result of cls(response)
        :rtype:
         ~flow.models.UnversionedEntityResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.UnversionedEntityResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'UnversionedEntityRequestDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject')
        else:
            _json = None

        request = build_get_index_entity_by_id_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            content_type=content_type,
            json=_json,
            template_url=self.get_index_entity_by_id.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('UnversionedEntityResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_index_entity_by_id.metadata = {'url': "/flow/v1.0/flowexperimenttemplates/getIndexEntities"}  # type: ignore


    @distributed_trace_async
    async def get_updated_entity_ids_for_workspace(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        body: Optional["_models.UnversionedRebuildIndexDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject"] = None,
        **kwargs: Any
    ) -> "_models.UnversionedRebuildResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject":
        """get_updated_entity_ids_for_workspace.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param body:  Default value is None.
        :type body:
         ~flow.models.UnversionedRebuildIndexDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return:
         UnversionedRebuildResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject,
         or the result of cls(response)
        :rtype:
         ~flow.models.UnversionedRebuildResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.UnversionedRebuildResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            _json = self._serialize.body(body, 'UnversionedRebuildIndexDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject')
        else:
            _json = None

        request = build_get_updated_entity_ids_for_workspace_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            content_type=content_type,
            json=_json,
            template_url=self.get_updated_entity_ids_for_workspace.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('UnversionedRebuildResponseDtoExperimentTemplateIndexEntityExperimentTemplateAnnotationsExperimentTemplatePropertiesExtensibleObject', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_updated_entity_ids_for_workspace.metadata = {'url': "/flow/v1.0/flowexperimenttemplates/rebuildIndex"}  # type: ignore

