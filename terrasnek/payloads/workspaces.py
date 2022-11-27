import json
from dataclasses import dataclass, field
from typing import Literal, List, Dict, Optional


@dataclass
class Workspace:
    type: Literal["workspaces"]
    name: str
    agent_pool_id: Optional[str]
    allow_destroy_plan: Optional[bool]
    auto_apply: bool
    description: Optional[str]
    file_triggers_enabled: bool = False
    global_remote_state: bool = False
    operations: bool = False
    queue_all_runs: bool = False
    speculative_enabled: bool = False
    ssh_key_id: str = ""
    terraform_version: str = ""
    trigger_prefixes: List[str] = field(default_factory=list)
    vcs_repo: Dict = field(default_factory=dict)
    working_directory: str = ""
    execution_mode: str = "remote"

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
                    "agent-pool-id": self.agent_pool_id,
                    "auto-apply": self.auto_apply,
                    "description": self.description,
                    "file-triggers-enabled": self.file_triggers_enabled,
                    "global-remote-state": self.global_remote_state,
                    "operations": self.operations,
                    "queue-all-runs": self.queue_all_runs,
                    "speculative-enabled": self.speculative_enabled,
                    "ssh-key-id": self.ssh_key_id,
                    "terraform-version": self.terraform_version,
                    "trigger-prefixes": self.trigger_prefixes,
                    "vcs-repo": self.vcs_repo,
                    "working-directory": self.working_directory,
                    "execution-mode": self.execution_mode,
                },
            },
        }

        return data
