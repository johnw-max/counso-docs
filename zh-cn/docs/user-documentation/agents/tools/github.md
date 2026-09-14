# GitHub

GitHub 工具可让 Agent 搜索代码仓库、Issue 和 Pull Request；获得授权后，也可创建或更新 Issue、评论和 PR。用于同步代码搜索的 GitHub Connection 与实时 GitHub Tool 是两种不同配置。

工作区管理员安装或批准 GitHub 应用，选择仓库，并向目标 Space 开放工具。先决定采用工作区凭据还是个人凭据：工作区凭据使用已配置的应用身份；个人凭据还受调用者自身 GitHub 成员权限限制。将 GitHub 加入 Agent，并在指令中明确它可处理的仓库范围。

先读取一份已知仓库文件或 Issue，并核对仓库所有者和名称。创建 Issue 或 PR 前，请 Agent 先概述拟执行的改动和目标仓库。仓库缺失时，检查应用安装范围和实际操作用户的成员身份；完成认证并不等于获得仓库访问权。
