# 社交媒体 & 社区

小红书、Twitter/X、B站、V2EX、Reddit。

## 小红书 / XiaoHongShu（多后端）

### 后端 A：OpenCLI（桌面首选）

```bash
opencli xiaohongshu search "query" -f yaml
opencli xiaohongshu note "NOTE_URL" -f yaml
opencli xiaohongshu comments NOTE_ID -f yaml
opencli xiaohongshu feed -f yaml
opencli xiaohongshu user USER_ID -f yaml
```

### 后端 B：xiaohongshu-mcp（服务器场景）

```bash
mcporter call 'xiaohongshu.search_feeds(keyword: "query")' --timeout 120000
mcporter call 'xiaohongshu.get_feed_detail(feed_id: "...", xsec_token: "...")' --timeout 120000
```

### 后端 C：xhs-cli（存量备选）

```bash
xhs search "query"
xhs read NOTE_ID_OR_URL
xhs comments NOTE_ID_OR_URL
```

## Twitter/X

```bash
twitter feed -n 20
twitter tweet URL_OR_ID
twitter user-posts @username -n 20
twitter search "query" -n 10
```

### search 失败重试链

1. 直接重试：`twitter search "query" -n 10`
2. 升级：`pipx upgrade twitter-cli && twitter search "query" -n 10`
3. OpenCLI：`opencli twitter search "query" -f yaml`
4. 绕路：`twitter feed` / `twitter user-posts @somebody`

## B站 / Bilibili

```bash
bili search "query" --type video -n 5
bili hot -n 10
bili video BVxxx
opencli bilibili subtitle BVxxx
```

## V2EX

```bash
curl -s "https://www.v2ex.com/api/topics/hot.json" -H "User-Agent: agent-reach/1.0"
curl -s "https://www.v2ex.com/api/topics/show.json?node_name=python&page=1" -H "User-Agent: agent-reach/1.0"
```

## Reddit（多后端）

### 后端 A：OpenCLI（桌面首选）

```bash
opencli reddit search "query" -f yaml
opencli reddit read POST_ID -f yaml
opencli reddit hot -f yaml
```

### 后端 B：rdt-cli

```bash
rdt search "query" --limit 10
rdt read POST_ID
rdt sub python --limit 20
```
