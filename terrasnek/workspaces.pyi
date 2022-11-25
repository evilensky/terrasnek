from typing import Any, Dict, Optional
from requests import Session

from terrasnek.api import ListAllProtocol
from terrasnek.endpoint import TFCEndpoint


class TFCWorkspaces(ListAllProtocol, TFCEndpoint):
    def __init__(
            self,
            instance_url: str,
            org_name: str,
            headers: Optional[Dict[str, str]],
            well_known_paths: Optional[Dict[str, str]],
            verify: bool,
            log_level: Optional[str],
            session: Optional[Session],
    ):
        ...
        #super().__init__(instance_url, org_name, headers, well_known_paths, verify, log_level, session)

    _org_api_v2_base_url: str = ...
    _ws_api_v2_base_url: str = ...

    def create(self, payload: dict) -> dict: ...
    def destroy(self, workspace_id: str) -> dict: ...
    def force_unlock(self, workspace_id: str) -> Any: ...
    def lock(self, workspace_id: str, payload: Dict) -> Any: ...
    def list(
        self,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include: Optional[str] = None,
        search: Optional[Dict] = None,
        filters: Optional[str] = None,
    ) -> Any: ...
    def show(
        self,
        workspace_name: Optional[str] = None,
        workspace_id: Optional[str] = None,
        include: Optional[str] = None,
    ) -> Any: ...
    def unlock(self, workspace_id: str) -> Any: ...
    def update(
        self,
        payload: Dict,
        workspace_name: Optional[str] = None,
        workspace_id: Optional[str] = None,
    ) -> Any: ...
    def assign_ssh_key(self, workspace_id: str, payload: Dict) -> Any: ...
    def unassign_ssh_key(self, workspace_id: str, payload: Dict) -> Any: ...
    def get_remote_state_consumers(
        self,
        workspace_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Any: ...
    def replace_remote_state_consumers(
        self, workspace_id: str, payload: Dict
    ) -> Any: ...
    def delete_remote_state_consumers(
        self, workspace_id: str, payload: Dict
    ) -> Any: ...
    def list_tags(self, workspace_id: str) -> Any: ...
    def add_tags(self, workspace_id: str, payload: Dict) -> Any: ...
    def list_all_resources(self, workspace_id: str): ...
    def remove_tags(self, workspace_id: str, payload: Dict) -> Any: ...
