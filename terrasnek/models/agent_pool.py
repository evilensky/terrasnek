"""
Module for the Terraform Cloud API agent pools and agents endpoints and associated payloads.
"""

from datetime import datetime
from typing import Literal, Optional, TypedDict, List, Dict

from pydantic import BaseModel, Field


def to_dash_case(snake_str: str) -> str:
    """
    Converts a string from snake_case to dash-case.
    """
    components = snake_str.split("_")
    return "-".join(components)


class TFCModel(BaseModel):
    """
    Base class for all TFC models.
    """

    class Config:
        """
        Pydantic configuration for all TFC models.
        """

        allow_population_by_field_name = True
        # extra = "forbid"
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }


class TFCLinks(TFCModel):
    """
    Links model for TFC API payloads.
    """

    self: str = Field(..., alias="self")
    first: Optional[str] = Field(None, alias="first")
    prev: Optional[str] = Field(None, alias="prev")
    next: Optional[str] = Field(None, alias="next")
    last: Optional[str] = Field(None, alias="last")


class TFCList(TFCModel):
    """
    Base class for all TFC
    """

    agent_pools: Optional[list] = Field(None, alias="data")
    links: Optional[TFCLinks]
    meta: Optional[dict]


class TFCAgentPoolAttributes(TFCModel):
    """
    Attributes for a Terraform Cloud agent pool.
    """

    organization_scoped: bool = Field(
        default=True,
        alias="organization-scoped",
        description="Whether the agent pool is scoped to the organization.",
    )
    created_at: Optional[datetime] = Field(
        default=None, alias="created-at", exclude=True
    )
    name: str = Field(default=None, alias="name")


class Workspaces(TypedDict):
    """
    Workspaces relationship for a Terraform Cloud agent pool.
    """

    id: str
    type: Literal["workspaces"]


class TFCAgentPoolRelationships(TFCModel):
    """
    The allowed workspaces for the tfc agent pool.
    """

    allowed_workspaces: Optional[Dict[Literal["data"], List[Workspaces]]] = Field(
        default=None, alias="allowed-workspaces"
    )


class TFCAgentPool(TFCModel):
    """
    `Agents Create Pool API Doc Reference \
        <https://www.terraform.io/docs/cloud/api/agents.html#create-an-agent-pool>`_
    """

    id: Optional[str] = Field(default=None)
    type: Literal["agent-pools"] = Field(default="agent-pools")
    attributes: Optional[TFCAgentPoolAttributes] = Field(
        default=None,
        alias="attributes",
    )
    relationships: Optional[TFCAgentPoolRelationships] = Field(
        default=None, alias="relationships"
    )
    links: Optional[TFCLinks] = Field(default=None, alias="links")


class TFCAgentPools(TFCList):
    """
    `Agents List Pools API Doc Reference \
        <https://www.terraform.io/docs/cloud/api/agents.html#list-agent-pools>`_
    """

    agent_pools: Optional[list[TFCAgentPool]] = Field(alias="data")
    links: Optional[TFCLinks] = Field(alias="links")
    meta: Optional[dict] = Field(alias="meta")

    def __len__(self) -> int:
        if self.agent_pools is None:
            return 0
        return len(self.agent_pools)

    def __iter__(self):
        if self.agent_pools is None:
            return iter([])
        return iter(self.agent_pools)

    def __getitem__(self, index: int) -> TFCAgentPool:
        if self.agent_pools is None:
            raise IndexError("No agent pools found.")
        return self.agent_pools[index]
