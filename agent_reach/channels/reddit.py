# -*- coding: utf-8 -*-
"""Reddit — multi-backend: OpenCLI / rdt-cli. Login is mandatory."""

import json
import shutil
import subprocess

from agent_reach.utils.process import utf8_subprocess_env

from .base import Channel

_CREDENTIAL_FILE = "~/.config/rdt-cli/credential.json"
_RDT_GIT_SOURCE = "git+https://github.com/public-clis/rdt-cli.git@5e4fb3720d5c174e976cd425ccc3b879d52cac66"
_BROKEN_EXIT_CODES = (126, 127)
_RDT_BROKEN_HINT = (
    "rdt 命令存在但无法执行——通常是系统 Python 升级后 venv 解释器丢失。\n"
    "PyPI 版本落后，推荐用固定 git 源强制重装：\n"
    f"  pipx install --force '{_RDT_GIT_SOURCE}'"
)


class RedditChannel(Channel):
    name = "reddit"
    description = "Reddit 帖子和评论"
    backends = ["OpenCLI", "rdt-cli"]
    tier = 1

    def can_handle(self, url: str) -> bool:
        from urllib.parse import urlparse
        d = urlparse(url).netloc.lower()
        return "reddit.com" in d or "redd.it" in d

    def check(self, config=None):
        self.active_backend = None
        findings = []

        for backend in self.ordered_backends(config):
            if backend == "OpenCLI":
                result = self._check_opencli()
            else:
                result = self._check_rdt()
            if result is None:
                continue
            findings.append((backend, *result))

        for wanted in ("ok", "warn"):
            for backend, status, message in findings:
                if status == wanted:
                    self.active_backend = backend
                    return status, message

        if findings:
            return "error", "\n".join(m for _, _, m in findings)

        return "off", (
            "未安装任何 Reddit 后端。注意：Reddit 没有零配置路径"
            "（匿名 .json 已被封，官方 API 需人工审批），必须用登录态。推荐：\n"
            "  桌面：agent-reach install --channels opencli\n"
            "       （复用 Chrome 登录态，登录过 reddit.com 即可用）\n"
            f"  服务器/存量：pipx install '{_RDT_GIT_SOURCE}'\n"
            "       然后 `rdt login` 或手动写入 Cookie（见 doctor 提示）\n"
            "中国大陆访问 Reddit 需要代理"
        )

    def _check_opencli(self):
        from agent_reach.backends import opencli_status
        st = opencli_status()
        if not st.installed:
            return None
        if st.broken:
            return "error", st.hint
        if st.ready:
            return "ok", (
                "OpenCLI 可用（复用浏览器登录态）。用法："
                "opencli reddit search/read/subreddit/hot -f yaml"
            )
        return "warn", st.hint

    def _check_rdt(self):
        rdt = shutil.which("rdt")
        if not rdt:
            return None
        try:
            r = subprocess.run(
                [rdt, "status", "--json"],
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=10,
                env=utf8_subprocess_env(),
            )
        except subprocess.TimeoutExpired:
            return "error", "rdt 响应超时（>10s），Reddit 状态未知。稍后重试或运行 `rdt status` 查看详情"
        except OSError:
            return "error", _RDT_BROKEN_HINT

        if r.returncode in _BROKEN_EXIT_CODES:
            return "error", _RDT_BROKEN_HINT

        if r.returncode != 0:
            detail = (r.stderr or r.stdout or "").strip().splitlines()
            tail = detail[-1] if detail else "无输出"
            return "error", f"rdt 异常退出（exit {r.returncode}）：{tail}。运行 `rdt status` 查看详情"

        try:
            data = json.loads(r.stdout or "")
        except json.JSONDecodeError:
            data = None
        if not isinstance(data, dict):
            return "warn", "rdt-cli 可用但状态输出无法解析，运行 `rdt status` 查看登录状态"

        info = data.get("data")
        if not isinstance(info, dict):
            info = {}
        authenticated = info.get("authenticated", False)
        username = info.get("username") or ""

        if authenticated:
            suffix = f"（已登录：{username}）" if username else ""
            return "ok", (
                f"rdt-cli 可用{suffix}（搜索帖子、阅读全文、查看评论；"
                "上游 2026-03 起停更，桌面用户建议迁移到 OpenCLI）"
            )

        return "warn", (
            "rdt-cli 已安装但未登录。Reddit 自 2024 年起要求认证，"
            "未登录时所有请求均返回 403。\n\n"
            "方法一（自动）：运行 `rdt login`\n"
            "  先在浏览器登录 reddit.com，再运行此命令自动提取 Cookie。\n\n"
            "方法二（手动）：\n"
            "  1. 安装 Cookie-Editor 扩展\n"
            "  2. 在浏览器打开 reddit.com（确保已登录）\n"
            "  3. 找到 `reddit_session`，复制其 Value\n"
            f"  4. 写入 {_CREDENTIAL_FILE}"
        )
