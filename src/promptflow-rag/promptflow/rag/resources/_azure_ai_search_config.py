# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# General todo: need to determine which args are required or optional when parsed out into groups like this.
# General todo: move these to more permanent locations?

# Defines stuff related to the resulting created index, like the index type.

from typing import Optional
from ._connection_config import ConnectionConfig


class AzureAISearchConfig:
    """Config class for creating an Azure AI Search index.

    :param ai_search_index_name: The name of the Azure AI Search index.
    :type ai_search_index_name: Optional[str]
    :param ai_search_connection_id: The Azure AI Search connection Config.
    :type ai_search_connection_config: Optional[ConnectionConfig]
    """

    def __init__(
        self,
        *,
        ai_search_index_name: Optional[str] = None,
        ai_search_connection_config: Optional[ConnectionConfig] = None,
    ) -> None:
        self.ai_search_index_name = ai_search_index_name
        self.ai_search_connection_config = ai_search_connection_config
