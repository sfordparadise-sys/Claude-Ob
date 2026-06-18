# -*- coding: utf-8 -*-
"""GitHub — check if gh CLI is available."""

from agent_reach.probe import probe_command

from .base import Channel


class GitHubChannel(Channel):
    name = "github"
    description = "GitHub 仓库和代码"
    backends = ["gh CLI"]
    tier = 0

    def can_handle(self, url: str) -> bool:
        from urllib.parse import urlparse
        return "github.com" in urlparse(url).netloc.lower()

    def check(self, config=None):
        probe = probe_command("gh", ["auth", "status"], timeout=10, package="gh")
        if probe.status == "missing":
            self.active_backend = None
            return "warn", "gh CLI 未安装。安装：https://cli.github.com"
        if probe.status == "broken":
            self.active_backend = None
            return "error", (
                "gh 命令存在但无法执行——安装已损坏。重装即可修复：\n"
                "  brew reinstall gh\n"
                "或从 https://cli.github.com 重新安装 gh CLI"
            )
        if probe.status == "timeout":
            self.active_backend = "gh CLI"
            return "warn", "gh CLI 状态检查超时，运行 gh auth status 查看详情"
        if probe.ok:
            self.active_backend = "gh CLI"
            return "ok", "完整可用（读取、搜索、Fork、Issue、PR 等）"
        self.active_backend = "gh CLI"
        return "warn", "gh CLI 已安装但未认证。运行 gh auth login 可解锁完整功能"
