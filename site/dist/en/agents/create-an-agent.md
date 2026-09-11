# Create an Agent

# Create an Agent

You can create an Agent when your workspace gives you the required permission. Before you begin, define the task, the people who should use it, and the minimum data access it needs.

## Start the configuration

1. Open **Work** and go to **Agents**.
2. Open **Create**.
3. Choose a starting point: **Agent from scratch**, **Agent from template**, or **Agent from YAML**.
4. If you choose **Agent from scratch**, review the editor before entering any private data.
5. Add a clear name, description, and instructions. Configure access only after you understand which Spaces or Pods the Agent may use.
6. Select **Save** when the configuration is ready.

After saving, check the Agent list and reopen the configuration to confirm that the name, description, instructions, and access settings match what you intended. If the Agent is not visible, check its publication state and your role with a workspace administrator.

## Keep the first version small

Give the Agent one clear responsibility and a reviewable result. Add capabilities or knowledge only when they are needed. Start with a read-only task where possible, and explain what the Agent should do when information is missing or conflicting.

Saving a configuration does not make every external action safe or available. Before sharing an Agent, review its data and access settings and test the expected result with non-sensitive material. For instruction design, read [Write Agent instructions](/en/agents/write-instructions/#write-agent-instructions); for access scope, read [Manage Agent data and access](/en/agents/data-and-access/#manage-agent-data-and-access).
