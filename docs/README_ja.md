<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>AIエージェントにワンクリックでインターネット全体へのアクセスを</strong>
</p>

<p align="center">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#クイックスタート">クイックスタート</a> · <a href="../README.md">中文</a> · <a href="README_en.md">English</a> · <a href="README_ko.md">한국어</a> · <a href="#対応プラットフォーム">プラットフォーム</a> · <a href="#設計思想">設計思想</a>
</p>

---

## なぜ Agent Reach？

AIエージェントはすでにインターネットにアクセスできます。しかし「ネットに繋がる」はほんの始まりに過ぎません。

最も価値のある情報は、さまざまなSNSやニッチなプラットフォームに散らばっています：Twitterの議論、Redditのフィードバック、YouTubeのチュートリアル、小红书のレビュー、Bilibiliの動画、GitHubのアクティビティ… **これらこそ情報密度が最も高い場所です**。しかし、各プラットフォームにはそれぞれ障壁があります：

| 課題 | 現実 |
|------|------|
| Twitter API | 従量課金、中程度の利用で月額約$215 |
| Reddit | サーバー IPが403でブロックされる |
| 小红书 | 閲覧にログインが必要 |
| Bilibili | 海外/サーバー IPをブロック |

エージェントをこれらのプラットフォームに接続するには、ツールを探し、依存関係をインストールし、設定をデバッグする必要があります — ひとつずつ。

**Agent Reach はこれを１つのコマンドにまとめます：**

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

これをエージェントにコピーするだけ。数分後には、ツイートの閲覧、Redditの検索、Bilibiliの視聴が可能になります。

**すでにインストール済み？１コマンドでアップデート：**

```
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

### ✅ 始める前に知っておきたいこと

| | |
|---|---|
| 💰 **完全無料** | すべてのツールはオープンソース、すべての API は無料。唱一のコストはサーバープロキシ（月額$1）の可能性のみ — ローカル PCでは不要 |
| 🔒 **プライバシー安全** | Cookieはローカルに保存。アップロードされることはありません。完全オープンソース — いつでも監査可能 |
| 🔄 **常に最新** | 上流ツール（yt-dlp、twitter-cli、rdt-cli、Jina Reader等）を定期的に追跡・更新 |
| 🤖 **あらゆるエージェントに対応** | Claude Code、OpenClaw、Cursor、Windsurf… コマンドを実行できるすべてのエージェント |
| 🩺 **組み込み診断** | `agent-reach doctor` — 1コマンドで何が動き、何が動かないか、どう修正するかを表示 |

---

## 対応プラットフォーム

| プラットフォーム | 機能 | セットアップ | 備考 |
|-----------------|------|:----------:|------|
| 🌐 **Web** | 閲覧 | 設定不要 | 任意のURL → クリーンなMarkdown（[Jina Reader](https://github.com/jina-ai/reader) ⭐9.8K） |
| 🐦 **Twitter/X** | 閲覧・検索 | 設定不要 / Cookie | 単一ツイートはすぐに閲覧可能。Cookieで検索、タイムライン、投稿が解放（[twitter-cli](https://github.com/public-clis/twitter-cli)） |
| 📕 **小红书** | 閲覧・検索・**投稿・コメント・いいね** | Cookie | `pipx install xiaohongshu-cli` + `xhs login`（[xhs-cli](https://github.com/jackwener/xiaohongshu-cli)） |
| 🎥 **抖音** | 動画解析・ウォーターマークなしダウンロード | mcporter | [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)、ログイン不要 |
| 💼 **LinkedIn** | Jina Reader（公開ページ） | プロフィール、企業、求人検索 | エージェントに「LinkedInの設定を手伝って」と伝えてください |
| 💬 **WeChat記事** | 検索 + 閲覧 | 設定不要 | WeChat公式アカウント記事の検索+閲覧（完全Markdown）（[Exa](https://exa.ai) + [Camoufox](https://github.com/daijro/camoufox)（オプション）） |
| 📰 **Weibo** | トレンド・検索・フィード・コメント | 設定不要 | ホット検索、コンテンツ/ユーザー/トピック検索、フィード、コメント（[mcp-server-weibo](https://github.com/Panniantong/mcp-server-weibo)） |
| 💻 **V2EX** | 人気トピック・ノードトピック・トピック詳細+返信・ユーザープロフィール | 設定不要 | 公開JSON API、認証不要。技術コミュニティのコンテンツに最適 |
| 📈 **雪球（Xueqiu）** | 株価・検索・人気投稿・人気銘柄 | 設定不要 | 公開APIで自動セッションCookie、ログイン不要 |
| 🎤 **小宇宙Podcast** | 文字起こし | 無料APIKey | Podcast音声 → Groq Whisper（無料）による完全テキスト文字起こし |
| 🔍 **Web検索** | 検索 | 自動設定 | インストール時に自動設定、無料、APIKey不要（[Exa](https://exa.ai)、[mcporter](https://github.com/nicepkg/mcporter)経由） |
| 📦 **GitHub** | 閲覧・検索 | 設定不要 | [gh CLI](https://cli.github.com) 搭載。公開リポジトリはすぐ使える。`gh auth login`でFork、Issue、PRが解放 |
| 📺 **YouTube** | 閲覧・**検索** | 設定不要 | 字幕 + 1800以上の動画サイトでの検索（[yt-dlp](https://github.com/yt-dlp/yt-dlp) ⭐148K） |
| 📺 **Bilibili** | 閲覧・**検索** | 設定不要 / プロキシ | 動画情報 + 字幕 + 検索。ローカルはすぐ動作、サーバーはプロキシが必要（[yt-dlp](https://github.com/yt-dlp/yt-dlp)） |
| 📡 **RSS** | 閲覧 | 設定不要 | 任意のRSS/Atomフィード（[feedparser](https://github.com/kurtmckee/feedparser) ⭐2.3K） |
| 📖 **Reddit** | 検索・閲覧 | Cookie | 2024年以降認証が必要 — インストール後 `rdt login` を実行（[rdt-cli](https://github.com/public-clis/rdt-cli)） |

---

## クイックスタート

以下をAIエージェント（Claude Code、OpenClaw、Cursor等）にコピーしてください：

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

エージェントが自動でインストールし、環境を検出し、何が使えるかを教えてくれます。

<details>
<summary>手動インストール</summary>

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```
</details>

---

## 設計思想

**Agent Reach はスキャフォールディングツールであり、フレームワークではありません。**

インストール後、エージェントは上流ツール（twitter-cli、rdt-cli、xhs-cli、yt-dlp、mcporter、gh CLI等）を直接呼び出します — 間にラッパーレイヤーはありません。

## クレジット

[twitter-cli](https://github.com/public-clis/twitter-cli) · [rdt-cli](https://github.com/public-clis/rdt-cli) · [xhs-cli](https://github.com/jackwener/xiaohongshu-cli) · [Jina Reader](https://github.com/jina-ai/reader) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [Exa](https://exa.ai) · [feedparser](https://github.com/kurtmckee/feedparser) · [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) · [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server)

## ライセンス

[MIT](../LICENSE)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date&v=20260309)](https://star-history.com/#Panniantong/Agent-Reach&Date)
