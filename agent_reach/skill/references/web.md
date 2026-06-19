# 网页阅读

通用网页、RSS。

## 通用网页 (Jina Reader)

```bash
curl -s "https://r.jina.ai/URL"
```

## RSS

```python
python3 -c "
import feedparser
for e in feedparser.parse('FEED_URL').entries[:5]:
    print(f'{e.title} — {e.link}')
"
```
