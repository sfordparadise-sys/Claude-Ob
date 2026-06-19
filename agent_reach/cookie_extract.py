# -*- coding: utf-8 -*-
"""Auto-extract cookies from local browsers for all supported platforms.

Supports: Chrome, Firefox, Edge, Brave, Opera
Extracts: Twitter, XiaoHongShu, Bilibili, Xueqiu cookies.

Usage:
    agent-reach configure --from-browser chrome
"""

import sys
from typing import Dict, List, Optional, Tuple


PLATFORM_SPECS = [
    {
        "name": "Twitter/X",
        "domains": [".x.com", ".twitter.com"],
        "cookies": ["auth_token", "ct0"],
        "config_key": "twitter",
    },
    {
        "name": "XiaoHongShu",
        "domains": [".xiaohongshu.com"],
        "cookies": None,
        "config_key": "xhs",
    },
    {
        "name": "Bilibili",
        "domains": [".bilibili.com"],
        "cookies": ["SESSDATA", "bili_jct"],
        "config_key": "bilibili",
    },
    {
        "name": "Xueqiu",
        "domains": [".xueqiu.com", "xueqiu.com"],
        "cookies": None,
        "config_key": "xueqiu",
    },
]


def extract_all(browser: str = "chrome") -> Dict[str, dict]:
    use_rookiepy = False
    try:
        import rookiepy
        use_rookiepy = True
    except ImportError:
        try:
            import browser_cookie3
        except ImportError:
            raise RuntimeError(
                "Cookie extraction requires rookiepy or browser_cookie3.\n"
                "Install: pip install rookiepy  (recommended)\n"
                "     or: pip install browser-cookie3"
            )

    browser = browser.lower()
    supported = ["chrome", "firefox", "edge", "brave", "opera"]
    if browser not in supported:
        raise ValueError(f"Unsupported browser: {browser}. Supported: {', '.join(supported)}")

    if use_rookiepy:
        try:
            browser_funcs = {
                "chrome": rookiepy.chrome,
                "firefox": rookiepy.firefox,
                "edge": rookiepy.edge,
                "brave": rookiepy.brave,
                "opera": rookiepy.opera,
            }
            raw_cookies = browser_funcs[browser]()
            class _Cookie:
                def __init__(self, d):
                    self.name = d.get("name", "")
                    self.value = d.get("value", "")
                    self.domain = d.get("domain", "")
            cookie_jar = [_Cookie(c) for c in raw_cookies]
        except Exception as e:
            raise RuntimeError(f"Could not read {browser} cookies via rookiepy: {e}")
    else:
        browser_funcs = {
            "chrome": browser_cookie3.chrome,
            "firefox": browser_cookie3.firefox,
            "edge": browser_cookie3.edge,
            "brave": browser_cookie3.brave,
            "opera": browser_cookie3.opera,
        }
        try:
            cookie_jar = browser_funcs[browser]()
        except Exception as e:
            raise RuntimeError(f"Could not read {browser} cookies: {e}")

    results = {}

    for spec in PLATFORM_SPECS:
        platform_cookies = {}
        all_cookies_for_domain = []

        for cookie in cookie_jar:
            domain_match = any(
                cookie.domain.endswith(d) or cookie.domain == d.lstrip(".")
                for d in spec["domains"]
            )
            if not domain_match:
                continue

            all_cookies_for_domain.append(cookie)

            if spec["cookies"] is not None:
                if cookie.name in spec["cookies"]:
                    platform_cookies[cookie.name] = cookie.value

        if spec["cookies"] is None:
            if all_cookies_for_domain:
                cookie_str = "; ".join(f"{c.name}={c.value}" for c in all_cookies_for_domain)
                results[spec["config_key"]] = {"cookie_string": cookie_str}
        else:
            if platform_cookies:
                results[spec["config_key"]] = platform_cookies

    return results


def _open_owner_only(path: str):
    import os
    import stat
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, stat.S_IRUSR | stat.S_IWUSR)
        return os.fdopen(fd, "w", encoding="utf-8")
    except OSError:
        return open(path, "w", encoding="utf-8")


def _sync_xfetch_session(auth_token: str, ct0: str) -> None:
    import json
    import os
    try:
        xfetch_dir = os.path.join(os.path.expanduser("~"), ".config", "xfetch")
        os.makedirs(xfetch_dir, exist_ok=True)
        session_path = os.path.join(xfetch_dir, "session.json")
        session_data: dict = {}
        if os.path.exists(session_path):
            try:
                with open(session_path, "r", encoding="utf-8") as sf:
                    session_data = json.load(sf)
            except (json.JSONDecodeError, OSError):
                session_data = {}
        session_data["authToken"] = auth_token
        session_data["ct0"] = ct0
        with _open_owner_only(session_path) as sf:
            json.dump(session_data, sf, indent=2)
    except Exception:
        pass


def _sync_bird_env(auth_token: str, ct0: str) -> None:
    import os
    import shlex
    try:
        bird_dir = os.path.join(os.path.expanduser("~"), ".config", "bird")
        os.makedirs(bird_dir, exist_ok=True)
        env_path = os.path.join(bird_dir, "credentials.env")
        with _open_owner_only(env_path) as f:
            f.write(f"AUTH_TOKEN={shlex.quote(auth_token)}\n")
            f.write(f"CT0={shlex.quote(ct0)}\n")
    except Exception:
        pass


_sync_bird_credentials = _sync_bird_env


def configure_from_browser(browser: str, config) -> List[Tuple[str, bool, str]]:
    results_list = []

    try:
        extracted = extract_all(browser)
    except Exception as e:
        return [("Browser", False, str(e))]

    if not extracted:
        return [("All platforms", False,
                 f"No platform cookies found in {browser}. "
                 f"Make sure you're logged into Twitter, XiaoHongShu, etc. in {browser}.")]

    if "twitter" in extracted:
        tc = extracted["twitter"]
        if "auth_token" in tc and "ct0" in tc:
            config.set("twitter_auth_token", tc["auth_token"])
            config.set("twitter_ct0", tc["ct0"])
            _sync_xfetch_session(tc["auth_token"], tc["ct0"])
            results_list.append(("Twitter/X", True, "auth_token + ct0"))
        else:
            found = ", ".join(tc.keys())
            missing = [k for k in ["auth_token", "ct0"] if k not in tc]
            results_list.append(("Twitter/X", False,
                                 f"Found {found}, but missing: {', '.join(missing)}."))

    if "xhs" in extracted:
        cookie_str = extracted["xhs"].get("cookie_string", "")
        if cookie_str:
            config.set("xhs_cookie", cookie_str)
            n_cookies = len(cookie_str.split(";"))
            results_list.append(("XiaoHongShu", True, f"{n_cookies} cookies"))

    if "bilibili" in extracted:
        bc = extracted["bilibili"]
        if "SESSDATA" in bc:
            config.set("bilibili_sessdata", bc["SESSDATA"])
            if "bili_jct" in bc:
                config.set("bilibili_csrf", bc["bili_jct"])
            results_list.append(("Bilibili", True, "SESSDATA" +
                                 (" + bili_jct" if "bili_jct" in bc else "")))
        else:
            results_list.append(("Bilibili", False, f"No SESSDATA found."))

    if "xueqiu" in extracted:
        cookie_str = extracted["xueqiu"].get("cookie_string", "")
        if cookie_str and "xq_a_token" in cookie_str:
            config.set("xueqiu_cookie", cookie_str)
            n_cookies = len(cookie_str.split(";"))
            results_list.append(("Xueqiu", True, f"{n_cookies} cookies"))
        elif cookie_str:
            results_list.append(("Xueqiu", False, f"Found cookies but missing xq_a_token"))

    return results_list
