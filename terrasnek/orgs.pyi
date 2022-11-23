from typing import Any, Dict, List, Literal, Protocol
from .endpoint import TFCEndpoint

class TFCOrgs(TFCEndpoint, Protocol):
    def __init_(
        self,
        instance_url: str,
        org_name: str,
        headers: dict,
        well_known_paths: dict,
        verify: bool,
        log_level: str,
    ) -> None: ...
    _org_api_v2_base_url: str = ...

    def required_entitlements(self) -> List[Any]: ...
    def terraform_cloud_only(self) -> Literal[False]: ...

    def entitlements(self, org_name: str) -> Dict[str, Any]: ...
