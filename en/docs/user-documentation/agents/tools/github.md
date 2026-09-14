# GitHub

GitHub tools let an Agent search repositories, issues, and pull requests and, where authorized, create or update issues, comments, and pull requests. A GitHub Connection for synchronized code search is a separate setup from the live GitHub Tool.

A workspace administrator installs or approves the GitHub application, selects the repositories, and makes the resulting tool available to the intended Space. Decide whether the tool uses workspace credentials or personal credentials. Workspace credentials act as the configured app identity; personal credentials are also bounded by the user's own GitHub membership. Add GitHub to the Agent and specify the repositories it should use in the Agent instructions.

Start with one known repository file or issue and verify its owner/repository. Before creating an issue or pull request, ask the Agent to summarize the proposed change and target repository. If a repository is missing, check app installation scope and the acting user's membership; authentication alone does not grant repository access.
