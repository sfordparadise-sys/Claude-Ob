# CLAUDE.md

Guidance for AI assistants (Claude Code and others) working in this repository.

## What this repo is

`Claude-Ob` hosts the **BuilderPilot static marketing website** — the public
field-systems site and field-notes blog for BuilderPilot / Stephen Ford
(`sfordparadise-sys`). It is a plain static site with **no build step**, deployed
to GitHub Pages.

> Note: the larger `builderpilot` repo also contains a copy of this marketing
> site alongside the Next.js SaaS app and The Architect tool. This repo is the
> standalone marketing-site deployment. Keep shared pages consistent between the
> two when you change branding or shared content.

## Layout

```
.
├── index.html             # main BuilderPilot landing page
├── mentorship.html        # 1:1 mentorship offer page
├── blog/
│   ├── index.html         # blog index
│   ├── 25-drywall-killers.html
│   ├── backing-blocking-register.html
│   ├── on1call-locates-ontario.html
│   ├── pre-drywall-inspection.html
│   ├── tarion-pdo-reporting.html
│   └── walk-log-recap-track.html
├── images/                # site imagery (covers, portraits)
├── downloads/             # lead-magnet PDFs (e.g. 25 Drywall Killers)
├── .claude/skills/        # local Claude Code skill: ui-ux-pro-max
├── ponytail/              # git submodule (DietrichGebert/ponytail)
└── .github/workflows/deploy.yml  # GitHub Pages deploy
```

## How to work on it

- Pages are **hand-written HTML/CSS/JS** — edit the files directly, no compiler,
  bundler, or package manager. Open a file in a browser to preview.
- Keep the BuilderPilot brand: industrial, field-ready, written from real
  job-site experience. Audience is Ontario residential site supervisors and
  production builders — keep terminology accurate (TARION, ESA, TSSA, OBC,
  pre-drywall, PDO, locates).
- Blog posts are practical field notes. New posts: add an HTML file under `blog/`
  and link it from `blog/index.html`. Mirror the structure/styling of an existing
  post rather than inventing a new layout.
- Reference real construction workflow knowledge, but **never** use any specific
  builder's proprietary branding, logos, forms, or internal documents.

## Submodule

`ponytail` is a git submodule (`https://github.com/DietrichGebert/ponytail.git`,
see `.gitmodules`). It is the "lazy senior dev" working-philosophy reference and
is currently uninitialized — run `git submodule update --init` only if you
actually need its contents. Don't commit an accidental submodule pointer change.

## Skills

`.claude/skills/ui-ux-pro-max/` is a bundled Claude Code skill providing UI/UX
design intelligence (styles, palettes, font pairings, stacks). Its
`scripts/__pycache__/` is gitignored.

## Deployment

`.github/workflows/deploy.yml` deploys to **GitHub Pages** on every push to
`main` (or manual dispatch). It uploads the entire repo root (`path: '.'`), so
whatever is at the top level is what goes live — keep stray/working files out of
the root.

## Git workflow

- Active development branch: **`claude/claude-md-docs-bj9h1d`**. Develop and push
  there; do not push to `main` without explicit permission.
- Push with `git push -u origin <branch>`; retry network failures with backoff.
- Commit with clear, descriptive messages. Do **not** create pull requests unless
  the user explicitly asks.
