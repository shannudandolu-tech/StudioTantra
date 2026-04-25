# Studio Tantra Development Guide

## ✅ Setup Complete

**System Requirements Installed:**
- Node.js v25.9.0
- Python 3.11.9
- FFmpeg 8.1

**Servers Running:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

---

## Starting Development

### Terminal 1: Backend (Python/FastAPI)
```powershell
cd studio-tantra/backend
.\venv\Scripts\python.exe main.py
```

### Terminal 2: Frontend (Next.js)
```powershell
cd studio-tantra
npm run dev:frontend
```

### Or both together:
```powershell
cd studio-tantra
npm run dev
```

---

## API Endpoints (v0.1)

### Health & Config
- `GET /health` — Service status
- `GET /config` — Platform configuration

### Jobs
- `POST /api/v1/jobs` — Create ad generation job
- `GET /api/v1/jobs/{job_id}` — Get job status

### API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## Project Structure

```
studio-tantra/
├── frontend/               # Next.js React app
│   ├── src/
│   │   ├── app/           # App router (Next.js 14)
│   │   └── styles/
│   └── package.json
├── backend/               # Python FastAPI
│   ├── main.py           # FastAPI entry point
│   ├── config.py         # Settings from .env
│   ├── agents.py         # LangGraph orchestration (6 agents)
│   ├── venv/             # Python virtual environment
│   └── pyproject.toml
└── .env.local            # Environment variables (DO NOT COMMIT)
```

---

## Environment Variables

**Location:** `.env.local` (already created)

**Key variables to fill in:**
```
ANTHROPIC_API_KEY=sk-ant-...
SUPABASE_URL=https://...
R2_ACCOUNT_ID=...
RAZORPAY_KEY_ID=...
```

Without API keys, the system will work but won't generate real ads. Placeholder responses will be returned.

---

## Development Workflow

1. **Make changes** to frontend (`src/`) or backend (`agents.py`, `main.py`)
2. **Frontend auto-reloads** — Next.js detects changes
3. **Backend auto-reloads** — Uvicorn with StatReload enabled
4. **Check API**: http://localhost:8000/docs (Swagger UI)
5. **Check Frontend**: http://localhost:3000

---

## LangGraph Agents (v1)

The orchestration workflow includes 6 specialist agents:

1. **Brief Parser** — Convert campaign brief → shot list
2. **Identity Lock** — Generate character with consistency (Flux + IP-Adapter)
3. **Scene Renderer** — Create video clips (Runway/Kling)
4. **Voice/Dub** — Multilingual voiceovers (Sarvam AI)
5. **Editor/Mux** — Compose variants (Remotion + FFmpeg)
6. **Critique/QA** — Quality gate (Claude as judge)

**Flow**: Brief → Parser → Lock → Render → Dub → Mux → Critique → Done

---

## Debugging

### Frontend Issues
```bash
# Check Next.js build
npm run build --workspace=frontend

# Lint TypeScript
npm run lint --workspace=frontend
```

### Backend Issues
```bash
# Check Python syntax
python -m py_compile backend/main.py backend/agents.py

# View detailed logs
# (Uvicorn is running with INFO level logging)
```

---

## Next Steps

1. **Add API Keys** to `.env.local` (Anthropic, Supabase, etc.)
2. **Test workflow** — POST to `/api/v1/jobs` with a brief
3. **Build UI** — Add brief upload form, results display
4. **Integrate Supabase** — Store jobs, audit trail
5. **Connect Razorpay** — Per-asset billing

---

## Kill Criteria (90 days from April 26)

- **Deadline**: July 26, 2026
- **Target**: First paying customer
- **Success metric**: ₹15k+ MRR from lead ICP

---

**Status**: v0.1 - Core infrastructure ready. Ready for feature development.
