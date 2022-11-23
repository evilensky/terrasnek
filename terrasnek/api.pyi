import logging
from typing import Protocol, Any, Optional, Dict, Union, Literal, List
from .workspaces import TFCWorkspaces
from ._constants import (
    TFC_SAAS_URL,
    TFC_SAAS_HOSTNAME,
    HTTP_OK,
    TERRASNEK_LOG_LEVEL,
    TERRASNEK_VERSION,
)

class ListAllProtocol(Protocol):

    """Protocol for the list_all method."""

    def list_all(self): ...


class TFC(Protocol):
    _logger: logging.Logger
    _log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    _token: str
    _current_org: Optional[str]
    def __init__(
        self,
        api_token: str,
        url: Literal['https://app.terraform.io'] = ...,
        verify: bool = ...,
        log_level: int = ...,
    ) -> None: ...


    workspaces: TFCWorkspaces
    def get_token(self) -> str: ...
    def set_org(self, org_name: str) -> None: ...
    def set_token(self, token: str) -> None: ...
    def _initialize_endpoints(self) -> None: ...
    def well_known_paths(self) -> Dict[str, str]: ...
    def _get(self, url: str) -> Any: ...
