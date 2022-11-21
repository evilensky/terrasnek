from typing import Protocol, Any, Optional, Dict
from .workspaces import TFCWorkspacesProtocol
from ._constants import (
    TFC_SAAS_URL,
    TFC_SAAS_HOSTNAME,
    HTTP_OK,
    TERRASNEK_LOG_LEVEL,
    TERRASNEK_VERSION,
)

class ListAllProtocol(Protocol):

    """Protocol for the list_all method."""

    def list_all(
        self,
        page: Optional[int] = None,
        include: Optional[str] = None,
        search: Optional[str] = None,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Any: ...

class api(Protocol):
    workspaces: TFCWorkspacesProtocol

    def set_org(self, org_name: str) -> None: ...
    def __init__(
        self, token: str, organization: str, url: str = "https://app.terraform.io"
    ) -> None: ...

class TFC:
    def __init__(
        self,
        api_token: str,
        url: str = TFC_SAAS_URL,
        verify: bool = True,
        log_level=TERRASNEK_LOG_LEVEL,
    ) -> None:
        self._logger = None
        ...
    workspaces: TFCWorkspacesProtocol
    def set_org(self, org_name: str) -> None: ...

class TFCWorkspaces(TFCWorkspacesProtocol): ...
