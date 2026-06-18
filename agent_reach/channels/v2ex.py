# -*- coding: utf-8 -*-
"""V2EX — public API channel for topics, nodes, users, and replies."""

import json
import urllib.request
from typing import Any
from .base import Channel

_UA = "agent-reach/1.0"
_TIMEOUT = 10


def _get_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


class V2EXChannel(Channel):
    name = "v2ex"
    description = "V2EX 节点、主题与回复"
    backends = ["V2EX API (public)"]
    tier = 0

    def can_handle(self, url: str) -> bool:
        from urllib.parse import urlparse
        d = urlparse(url).netloc.lower()
        return "v2ex.com" in d

    def check(self, config=None):
        try:
            _get_json("https://www.v2ex.com/api/topics/show.json?node_name=python&page=1")
            self.active_backend = self.backends[0]
            return "ok", "公开 API 可用（热门主题、节点浏览、主题详情、用户信息）"
        except Exception as e:
            self.active_backend = None
            return "warn", f"V2EX API 连接失败（可能需要代理）：{e}"

    def get_hot_topics(self, limit: int = 20) -> list:
        data = _get_json("https://www.v2ex.com/api/topics/hot.json")
        results = []
        for item in data[:limit]:
            node = item.get("node") or {}
            content = item.get("content", "") or ""
            results.append({"id": item.get("id", 0), "title": item.get("title", ""), "url": item.get("url", ""), "replies": item.get("replies", 0), "node_name": node.get("name", ""), "node_title": node.get("title", ""), "content": content[:200], "created": item.get("created", 0)})
        return results

    def get_node_topics(self, node_name: str, limit: int = 20) -> list:
        url = f"https://www.v2ex.com/api/topics/show.json?node_name={node_name}&page=1"
        data = _get_json(url)
        results = []
        for item in data[:limit]:
            node = item.get("node") or {}
            content = item.get("content", "") or ""
            results.append({"id": item.get("id", 0), "title": item.get("title", ""), "url": item.get("url", ""), "replies": item.get("replies", 0), "node_name": node.get("name", node_name), "node_title": node.get("title", ""), "content": content[:200], "created": item.get("created", 0)})
        return results

    def get_topic(self, topic_id: int) -> dict:
        topic_data = _get_json(f"https://www.v2ex.com/api/topics/show.json?id={topic_id}")
        if isinstance(topic_data, list):
            topic = topic_data[0] if topic_data else {}
        else:
            topic = topic_data
        node = topic.get("node") or {}
        member = topic.get("member") or {}
        try:
            replies_raw = _get_json(f"https://www.v2ex.com/api/replies/show.json?topic_id={topic_id}&page=1")
        except Exception:
            replies_raw = []
        replies = [{"author": (r.get("member") or {}).get("username", ""), "content": r.get("content", ""), "created": r.get("created", 0)} for r in (replies_raw or [])]
        return {"id": topic.get("id", topic_id), "title": topic.get("title", ""), "url": topic.get("url", f"https://www.v2ex.com/t/{topic_id}"), "content": topic.get("content", ""), "replies_count": topic.get("replies", 0), "node_name": node.get("name", ""), "node_title": node.get("title", ""), "author": member.get("username", ""), "created": topic.get("created", 0), "replies": replies}

    def get_user(self, username: str) -> dict:
        data = _get_json(f"https://www.v2ex.com/api/members/show.json?username={username}")
        return {"id": data.get("id", 0), "username": data.get("username", username), "url": data.get("url", f"https://www.v2ex.com/member/{username}"), "website": data.get("website", ""), "twitter": data.get("twitter", ""), "github": data.get("github", ""), "location": data.get("location", ""), "bio": data.get("bio", ""), "avatar": data.get("avatar_large", data.get("avatar_normal", "")), "created": data.get("created", 0)}

    def search(self, query: str, limit: int = 10) -> list:
        return [{"error": f"V2EX 公开 API 不提供搜索端点。建议改用：https://www.v2ex.com/?q={query} 或通过 Exa channel 使用 site:v2ex.com 搜索。"}]
