import logging
from typing import Protocol, Any, Optional, Dict, Literal, List

from .orgs import TFCOrgs
from .workspaces import TFCWorkspaces


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


    workspaces: TFCWorkspaces = ...
    orgs: TFCOrgs = ...
    def get_token(self) -> str: ...
    def get_entitlements(self) -> Optional[List[str]]: ...
    def set_org(self, org_name: str) -> None: ...
    def set_token(self, token: str) -> None: ...
    def _initialize_endpoints(self) -> None: ...
    def well_known_paths(self) -> Dict[str, str]: ...
    def _get(self, url: str) -> Any: ...
