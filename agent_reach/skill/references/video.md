# 视频/播客

YouTube、B站、小宇宙播客的字幕和转录。

## YouTube (yt-dlp)

```bash
# 元数据
yt-dlp --dump-json "URL"

# 字幕
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --skip-download -o "/tmp/%(id)s" "URL"

# 搜索
yt-dlp --dump-json "ytsearch5:query"

# 无字幕兑底：Whisper 转写
agent-reach transcribe "https://www.youtube.com/watch?v=VIDEO_ID"
```

## B站 / Bilibili

> ⚠️ **不要用 yt-dlp 读 B站**（风控 412 拦截）。

```bash
bili video BVxxx
bili search "query" --type video -n 5
bili hot -n 10
bili audio BVxxx
opencli bilibili subtitle BVxxx
```

## 小宇宙播客

```bash
~/.agent-reach/tools/xiaoyuzhou/transcribe.sh --polish "https://www.xiaoyuzhoufm.com/episode/EPISODE_ID"
```
