from terrasnek.models.agent_pool import (
    TFCAgentPool,
    TFCAgentPools,
    TFCAgentPoolAttributes,
    TFCAgentPoolRelationships,
)

import json

agent_pool_data = json.loads(
    """
{
  "data": [
    {
      "id": "apool-yoGUFz5zcRMMz53i",
      "type": "agent-pools",
      "attributes": {
        "name": "example-pool",
        "created-at": "2020-08-05T18:10:26.964Z",
        "organization-scoped": false
      },
      "relationships": {
        "agents": {
          "links": {
            "related": "/api/v2/agent-pools/apool-yoGUFz5zcRMMz53i/agents"
          }
        },
        "authentication-tokens": {
          "links": {
            "related": "/api/v2/agent-pools/apool-yoGUFz5zcRMMz53i/authentication-tokens"
          }
        },
        "workspaces": {
          "data": [
            {
              "id": "ws-9EEkcEQSA3XgWyGe",
              "type": "workspaces"
            }
          ]
        },
        "allowed-workspaces": {
          "data": [
            {
              "id": "ws-x9taqV23mxrGcDrn",
              "type": "workspaces"
            }
          ]
        }
      },
      "links": {
        "self": "/api/v2/agent-pools/apool-yoGUFz5zcRMMz53i"
      }
    }
  ],
  "links": {
    "self": "https://app.terraform.io/api/v2/organizations/my-organization/agent-pools?page%5Bnumber%5D=1&page%5Bsize%5D=20",
    "first": "https://app.terraform.io/api/v2/organizations/my-organization/agent-pools?page%5Bnumber%5D=1&page%5Bsize%5D=20",
    "prev": null,
    "next": null,
    "last": "https://app.terraform.io/api/v2/organizations/my-organization/agent-pools?page%5Bnumber%5D=1&page%5Bsize%5D=20"
  },
  "meta": {
    "pagination": {
      "current-page": 1,
      "prev-page": null,
      "next-page": null,
      "total-pages": 1,
      "total-count": 1
    },
    "status-counts": {
      "total": 1,
      "matching": 1
    }
  }
}
"""
)

# get agent pools
agent_pools = TFCAgentPools(**agent_pool_data)

# create an agent pool

new_agent_pool = TFCAgentPool(
    attributes=TFCAgentPoolAttributes(
        name="example-pool",
        organization_scoped=False,
    ),
    relationships=TFCAgentPoolRelationships(
        allowed_workspaces=[
            {
                "id": "ws-x9taqV23mxrGcDrn",
                "type": "workspaces",
            },
            {
                "id": "ws-9EEkcEQSA",
                "type": "workspaces",
            },
        ]
    ),
)

# create an agent pool with a workspace
print("balloons")

# modify the agent pool name in place
