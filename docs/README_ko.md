<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>AI 에이전트가 인터넷 전체에 접근할 수 있도록 한 번에 설정해 드립니다</strong>
</p>

<p align="center">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#빠른-시작">빠른 시작</a> · 한국어 · <a href="../README.md">中文</a> · <a href="README_en.md">English</a> · <a href="README_ja.md">日本語</a> · <a href="#지원-플랫폼">지원 플랫폼</a> · <a href="#설계-철학">설계 철학</a>
</p>

---

## Agent Reach가 필요한 이유

AI 에이전트는 이미 인터넷에 접근할 수 있습니다 — 하지만 "인터넷에 접속할 수 있다"는 것은 시작에 불과합니다.

가장 가치 있는 정보는 소셜 미디어와 특화된 플랫폼에 분포되어 있습니다: Twitter 토론, Reddit 피드백, YouTube 튜토리얼, XiaoHongShu 리븷, Bilibili 비디오, GitHub 활동... **여기가 정보 밀도가 가장 높은 곳**이지만, 각 플랫폼은 고유한 진입장벽이 있습니다:

| 문제점 | 현실 |
|------------|----------|
| Twitter API | 유료 사용, 중간 정도 사용량 ~월 $215 |
| Reddit | 서버 IP가 403 오류 발생 |
| XiaoHongShu | 둘러보기 위해 로그인 필요 |
| Bilibili | 해외/서버 IP 차단 |

에이전트를 이 플랫폼에 연결하려면 도구를 찾고, 의존성을 설치하고, 설정을 디버깅해야 합니다 — 하나씩 직접.

**Agent Reach는 이를 하나의 명령으로 바꿉니다:**

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

이 명령을 에이전트에 복사해서 붙여넣으세요. 몇 분 뒤에는 트윗을 읽고, Reddit을 검색하고, Bilibili를 볼 수 있게 됩니다.

**이미 설치하셨나요? 한 번에 업데이트하세요:**

```
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

### ✅ 시작하기 전에 알면 좋은 것들

| | |
|---|---|
| 💰 **완전 무료** | 모든 도구는 오픈 소스, 모든 API는 무료입니다. 유일한 비용은 서버 프록시(월 $1)일 수 있습니다 — 로컈 컴퓨터에서는 불필요 |
| 🔒 **프라이버시 안전** | Cookie는 로컈에 유지됩니다. 업로드되지 않습니다. 완전 오픈 소스 — 언제든지 감사 가능 |
| 🔄 **최신 상태 유지** | 업스트림 도구(yt-dlp, twitter-cli, rdt-cli, Jina Reader 등)를 추적하고 정기적으로 업데이트 |
| 🤖 **모든 에이전트와 호환** | Claude Code, OpenClaw, Cursor, Windsurf... 명령을 실행할 수 있는 모든 에이전트 |
| 🩺 **내장 진단 도구** | `agent-reach doctor` — 하나의 명령으로 작동 항목, 작동하지 않는 항목, 수정 방법 표시 |

---

## 지원 플랫폼

| 플랫폼 | 기능 | 설정 | 참고 |
|----------|-------------|:-----:|-------|
| 🌐 **Web** | 읽기 | 없음 | 모든 URL → 깨끗한 Markdown ([Jina Reader](https://github.com/jina-ai/reader) ⭐9.8K) |
| 🐦 **Twitter/X** | 읽기 · 검색 | Cookie | Cookie로 검색, 타임라인, 트윗 읽기, 아티클 읽기 가능 ([twitter-cli](https://github.com/public-clis/twitter-cli)) |
| 📕 **XiaoHongShu** | 읽기 · 검색 · **게시글 작성 · 댓글 · 좋아요** | Cookie | `pipx install xiaohongshu-cli` + `xhs login` ([xhs-cli](https://github.com/jackwener/xiaohongshu-cli)) |
| 🎥 **Douyin** | 비디오 파싱 · 워터마크 없는 다운로드 | mcporter | [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) 통해, 로그인 불필요 |
| 💼 **LinkedIn** | Jina Reader (공개 페이지) | Cookie | 전체 프로필, 회사, 악청 공고 검색 가능. 에이전트에 "LinkedIn 설정 도와줘"라고 말하세요 |
| 💬 **WeChat Articles** | 검색 + 읽기 | 없음 | Exa를 통한 WeChat 공식 계정 게시글 검색 + 읽기 (설정 없음) + 선택적 [Camoufox](https://github.com/daijro/camoufox) |
| 📰 **Weibo** | 인기 · 검색 · 피드 · 댓글 | 없음 | 핯 검색, 콘텐츠/사용자/주제 검색, 피드, 댓글 ([mcp-server-weibo](https://github.com/Panniantong/mcp-server-weibo)) |
| 💻 **V2EX** | 인기 주제 · 노드 주제 · 주제 상세 + 답글 · 사용자 프로필 | 없음 | 공개 JSON API, 인증 없음. 기술 커뮤니티 콘텐츠에 적합 |
| 📈 **Xueqiu (雪球)** | 주식 시세 · 검색 · 인기 글 · 인기 종목 | 브라우저 Cookie | 에이전트에 "Xueqiu 설정 도와줘"라고 말하세요 |
| 🎤 **Xiaoyuzhou Podcast** | 음성 변환 | 무료 API key | Groq Whisper를 통한 팟캐스트 오디오 → 전체 텍스트 변환 (무료) |
| 🔍 **Web Search** | 검색 | 자동 설정 | 설치 시 자동 설정, 무료, API key 불필요 ([Exa](https://exa.ai) via [mcporter](https://github.com/nicepkg/mcporter)) |
| 📦 **GitHub** | 읽기 · 검색 | 없음 | [gh CLI](https://cli.github.com) 기반. 공개 저장소는 즉시 사용 가능. `gh auth login`으로 Fork, Issue, PR 기능 활성화 |
| 📺 **YouTube** | 읽기 · **검색** | 없음 | 자막 + 1800+ 비디오 사이트 검색 ([yt-dlp](https://github.com/yt-dlp/yt-dlp) ⭐148K) |
| 📺 **Bilibili** | 읽기 · **검색** | 없음 / 프록시 | 비디오 정보 + 자막 + 검색. 로컈은 바로 작동, 서버는 프록시 필요 ([yt-dlp](https://github.com/yt-dlp/yt-dlp)) |
| 📡 **RSS** | 읽기 | 없음 | 모든 RSS/Atom 피드 ([feedparser](https://github.com/kurtmckee/feedparser) ⭐2.3K) |
| 📖 **Reddit** | 검색 · 읽기 | Cookie | 2024년부터 인증 필요 — 설치 후 `rdt login` 실행 ([rdt-cli](https://github.com/public-clis/rdt-cli)) |

---

## 빠른 시작

이 명령을 AI 에이전트(Claude Code, OpenClaw, Cursor 등)에 입력하세요:

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

에이전트가 자동으로 설치하고, 환경을 감지하고, 준비된 항목을 알려줍니다.

<details>
<summary>수동 설치</summary>

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```
</details>

---

## 설계 철학

**Agent Reach는 스캐폴딩(scaffolding) 도구이지, 프레임워크가 아닙니다.**

새 에이전트를 실행할 때마다 도구를 찾고, 의존성을 설치하고, 설정을 디버깅하는 데 시간을 보내게 됩니다. Agent Reach는 한 가지 간단한 작업을 수행합니다: **도구 선택 및 설정 결정을 대신 해줍니다.**

설치 후, 에이전트는 업스트림 도구(twitter-cli, rdt-cli, xhs-cli, yt-dlp, mcporter, gh CLI 등)를 직접 호출합니다 — 중간에 래퍼 계층이 없습니다.

## 크레딧

[twitter-cli](https://github.com/public-clis/twitter-cli) · [rdt-cli](https://github.com/public-clis/rdt-cli) · [xhs-cli](https://github.com/jackwener/xiaohongshu-cli) · [bili-cli](https://github.com/public-clis/bilibili-cli) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [Jina Reader](https://github.com/jina-ai/reader) · [Exa](https://exa.ai) · [mcporter](https://github.com/nicobailon/mcporter) · [feedparser](https://github.com/kurtmckee/feedparser) · [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) · [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server)

## 연락정보

- 📧 **이메일:** pnt01@foxmail.com
- 🐦 **Twitter/X:** [@Neo_Reidlab](https://x.com/Neo_Reidlab)

## 라이선스

[MIT](../LICENSE)

## 관련 프로젝트

[OpenClaw on Tencent Cloud](https://www.tencentcloud.com/act/pro/intl-openclaw?referral_code=G76Y819A&lang=en&pg=) — Tencent Cloud에서 원클릭 OpenClaw: 채팅으로 Agent Reach를 연결하고 인터넷 기능을 활성화하세요.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date&v=20260309)](https://star-history.com/#Panniantong/Agent-Reach&Date)
