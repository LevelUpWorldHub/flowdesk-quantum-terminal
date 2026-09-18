# flowdesk-quantum-terminal

AI-DIS FlowDesk Quantum Terminal — institutional-grade real-time trading terminal with live volatility regime tracking, IV surface, and **Alpaca paper** order routing.

`gh_login=LevelUpWorldHub` · `owner/name=LevelUpWorldHub/flowdesk-quantum-terminal`

## Status
Foundation scaffold (2026-09-16 PT). Paper trading stubs only — no live brokerage until Mark names that Act.

## Layout
- `apps/api` — FastAPI: health, regime, IV surface mock, paper order stub
- `apps/web` — Next.js shell: terminal panes
- `docs/ARCHITECTURE.md`

## Quickstart
```bash
cd apps/api && pip install -e ".[dev]" && pytest -q && uvicorn app.main:app --reload --port 8090
cd apps/web && npm i && npm run dev
```
