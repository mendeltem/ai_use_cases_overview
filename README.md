# AI Use Cases Overview

An interactive, single-page dashboard cataloguing concrete AI deployments running in the real world, current as of **August 2026**. Every use case is rated on three axes: how far it has scaled, how solid the evidence is, and how fast it is growing.

**Live demo:** https://mendeltem.github.io/ai_use_cases_overview/

## What's in it

91 use cases across 15 clusters, from robotaxis and warehouse robots to knowledge-work agents and weather forecasting. Each card shows a headline metric, a detail note with caveats, and a linked source. Interface is trilingual (English / German / Mongolian).

## Rating axes

- **Maturity** – production · early production · pilot · research
- **Evidence** – solid (primary / peer-reviewed) · medium (plausible claim) · thin (marketing / single source)
- **Growth** – explosive · strong · steady · nascent

## Clusters

Mobility & transport · Warehouse & energy · Industry & humanoids · Agriculture · Medicine & the body · Hazardous zones · Science & forecasting · Knowledge-work agents · Security & fraud · Back office & bureaucracy · The city in the background · Enablers · The compute & energy substrate · Consumer & home robots · Media & entertainment

## Features

- Filter by cluster, maturity, growth, and evidence
- Source link and official company pages on every card that has them
- Free-text search across provider, metric, and term
- EN/DE/MN language toggle
- No build step, no dependencies (one `index.html`; only Google Fonts loaded from CDN)

## Run locally

Open `index.html` directly, or serve the folder:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Sources & caveats

Claims are backed by web verification and primary sources where possible. Solid anchors include SEC filings (Intuitive Surgical, Aurora, Rio Tinto), peer-reviewed work (Insilico Rentosertib, Johns Hopkins SRT-H, John Deere See & Spray), and IFR World Robotics 2025. Efficiency figures not marked "solid" are mostly company-reported and directional rather than point-precise; where a growth figure is a company target rather than a realized number, the card says so.
