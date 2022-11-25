from logging import Logger
from typing import Protocol, Optional, Union, Literal, Dict, List, Any

from requests import Session


class TFCEndpoint(Protocol):
    def __init__(
        self,
        instance_url: str,
        org_name: str,
        headers: Optional[Dict[str, str]],
        well_known_paths: Optional[Dict[str, str]],
        verify: bool,
        log_level: Optional[Union[str, int]],
        session: Optional[Session] = None,
    ): ...
    _verify: bool = ...
    _headers: Dict[str, str] = ...
    _session: Session = ...
    _org_name: str = ...
    _modules_v1_base_url: str = ...
    _api_v2_base_url: str = ...
    _meta_base_url: str = ...
    _logger: Logger = ...
    _instance_url: str = ...

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
        return_raw: bool = ...,
        allow_redirects: bool = ...,
        query: Optional[str] = ...,
        filters: Optional[List] = ...,
        page: Optional[int] = ...,
        page_size: Optional[int] = ...,
        search: Optional[Dict] = ...,
        include: Optional[str] = ...,
        sort: Optional[str] = ...,
        offset: Optional[int] = ...,
        limit: Optional[int] = ...,
        provider: Optional[str] = ...,
        namespace: Optional[str] = ...,
        verified: Optional[bool] = ...,
        since: Optional[str] = ...
    ) -> Union[Dict[str, Any], bytes]: ...


    def _patch(self, url: str, data: Optional[Dict[Any, Any]] = None) -> None: ...
    def _post(
        self, url: str, data: Optional[Union[Dict[Any, Any], str, bytes]] = None
    ) -> Optional[Dict[str, Any]]: ...
    def _put(
        self,
        url: str,
        octet: Optional[bool] = None,
        data: Optional[Union[Dict[Any, Any], str, bytes]] = None,
    ) -> None: ...
    def _create(self, url: str, payload: Optional[Dict[Any, Any]]) -> Dict[Any, Any]: ...
    def _destroy(self, url: str, data=None) -> None: ...
    def _list(
        self,
        url: str,
        return_raw: bool = ...,
        allow_redirects: bool = ...,
        query: Optional[str] = ...,
        filters: Optional[List] = ...,
        page: Optional[int] = ...,
        page_size: Optional[int] = ...,
        search: Optional[Dict] = ...,
        include: Optional[str] = ...,
        sort: Optional[str] = ...,
        offset: Optional[int] = ...,
        limit: Optional[int] = ...,
        provider: Optional[str] = ...,
        namespace: Optional[str] = ...,
        verified: Optional[bool] = ...,
        since: Optional[str] = ...
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
