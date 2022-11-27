import json
from dataclasses import dataclass, field
from typing import Literal, List, Dict, Optional


@dataclass
class AgentPool:
    type: Literal["agent-pools"]
    name: str
    organization_scoped: bool = False
    allowed_workspaces: Optional[List[str]] = field(default_factory=list)

    def __str__(self):
        """
        Returns a JSON string representation of the object.
        """
        return json.dumps(self.to_json_api(), indent=4)

    def to_json_api(self) -> Dict:
        """
        Returns a JSON API representation of the object.
        """
        data = {
            "data": {
                "type": self.type,
                "attributes": {
                    "name": self.name,
                    "organization-scoped": self.organization_scoped,
                },
            },
        }

        if self.allowed_workspaces:
            data["data"]["relationships"] = {
                "allowed-workspaces": {
                    "data": [
                        {"id": ws_id, "type": "workspaces"}
                        for ws_id in self.allowed_workspaces
                    ],
                }
            }
        return data

