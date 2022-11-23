from logging import Logger
from typing import Protocol, Optional, TypeVar, Union, Literal, Dict, List, Any

from requests import Session

class TFCEndpoint(Protocol):
    def __init__(
        self,
        instance_url: str,
        org_name: str,
        headers: Optional[Dict[str, str]],
        well_known_paths: Optional[Dict[str, str]],
        verify: bool,
        log_level: Optional[str],
        session: Optional[Session] = None,
    ):
        ...
    _session: Session = ...
    _api_v2_base_url: str = ""
    _logger: Logger = Logger(__name__)

    def required_entitlements(self) -> List[str]: ...
    def terraform_cloud_only(self) -> bool: ...
    def terraform_enterprise_only(self) -> bool: ...
    def _list_all(
        self,
        url: str,
        include: Optional[str] = None,
        search: Optional[str] = None,
        filters: Optional[List[Dict]] = None,
        query: Optional[str] = None,
    ) -> Dict[Union[Literal["data"], Literal["response"]], List[Any]]: ...
    def _delete(self, url: str, data: Optional[Dict[Any, Any]] = None) -> None: ...
    def _get(
        self,
            url: str,
            return_raw: bool = False,
            allow_redirects: bool = False,
            query: Optional[str] = None,
            filters: Optional[List] = None,
            page: Optional[int] = None,
            page_size: Optional[int] = None,
            search: Optional[str] = None,
            include: Optional[str] = None,
            sort: Optional[str] = None,
            offset: Optional[int] = None,
            limit: Optional[int] = None,
            provider: Optional[str] = None,
            namespace: Optional[str] = None,
            verified: Optional[bool] = False,
            since: Optional[str] = None,
    ) -> Dict[str, Any]: ...
    def _patch(self, url: str, data: Optional[Dict[Any, Any]] = None) -> None: ...
    def _post(
        self, url: str, data: Optional[Dict[Any, Any]] = None
    ) -> Optional[Dict[str, Any]]: ...
    def _put(
        self,
        url: str,
        octet: Optional[bool] = None,
        data: Optional[Dict[Any, Any]] = None,
    ) -> None: ...
    def _create(self, url: str, payload: Dict[Any, Any]) -> Dict[Any, Any]: ...
    def _destroy(self, url: str, data=None) -> None: ...
    def _list(
        self,
        url: str,
        return_raw: bool = False,
        allow_redirects: bool = False,
        query: Optional[str] = None,
        filters: Optional[List] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        search: Optional[str] = None,
        include: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        provider: Optional[str] = None,
        namespace: Optional[str] = None,
        verified: Optional[bool] = False,
        since: Optional[str] = None,
    ) -> Dict: ...
    def _show(self, url: str, include: Optional[str] = None) -> Dict: ...
    def _update(self, url: str, payload: Dict) -> Dict: ...
    def _download(
        self,
        url: str,
        target_path: str,
        header_with_url: Optional[str] = None,
        allow_redirects: bool = False,
    ) -> None: ...
    def get_current_org(self) -> Dict: ...
