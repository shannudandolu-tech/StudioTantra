# Studio Tantra v0.1

AI-powered ad creative platform for Indian SMBs and ad shops.

**One-line pitch:** Upload your brand mascot. We generate consistent ad variants across 6 Indian languages, 3 aspect ratios, and 4 hooks — billed per finished asset.

## Project Structure

```
studio-tantra/
├── frontend/          # Next.js web app
├── backend/           # Python LangGraph orchestration
├── config/            # Shared configuration
├── .env.example       # Environment variables template
└── package.json       # Root workspace config
```

## Quick Start

### Prerequisites

- **Node.js** 18+
- **Python** 3.10+
- **FFmpeg** (for video compositing)
- **Git**

### 1. Install System Dependencies

**Windows (using Chocolatey):**
```bash
choco install nodejs ffmpeg python
```

**Or manually:**
- Node.js: https://nodejs.org/
- Python: https://www.python.org/
- FFmpeg: https://ffmpeg.org/download.html

### 2. Setup Environment

```bash
# Clone API keys from template
cp .env.example .env.local

# Add your actual API keys to .env.local
```

### 3. Install Dependencies

```bash
# From root directory
npm install

# This installs dependencies for both frontend and backend
```

### 4. Start Development

```bash
# Terminal 1 - Start both frontend and backend concurrently
npm run dev

# OR individually:
npm run dev:frontend  # http://localhost:3000
npm run dev:backend   # http://localhost:8000
```

## Architecture

### Frontend (`/frontend`)
- **Next.js 14** with TypeScript
- Brief upload, review, approval flow
- Razorpay payment integration
- Real-time asset delivery via Slack/WhatsApp

### Backend (`/backend`)
- **Python 3.10+** with FastAPI
- **LangGraph** orchestration engine
- 6 specialist agents (v1):
  - Brief Parser
  - Identity Lock (character consistency)
  - Scene Renderer
  - Voice/Dub (regional languages)
  - Editor/Mux (aspect variants)
  - Critique/QA (quality gate)

### Database
- **Supabase** (PostgreSQL)
  - Jobs, briefs, audit trails
  - API credentials management

### Storage
- **Cloudflare R2**
  - Assets, references, finished work
  - No egress fees vs S3

## Key Technologies

| Layer | Primary | Backup |
|-------|---------|--------|
| Orchestration | LangGraph | CrewAI |
| LLM | Claude Sonnet 4.6 | GPT-5 |
| Image Gen | Flux 1.1 Pro | Ideogram |
| Video Gen | Runway Gen-4 / Kling | Pika |
| TTS/Dub | Sarvam AI | ElevenLabs |
| Lip-sync | Sync Labs API | Wav2Lip |
| Audio | ElevenLabs + Suno | — |
| Compositing | Remotion + FFmpeg | — |
| App | Next.js + Supabase | — |
| Payments | Razorpay | — |

## Development Workflow

1. **Pull main branch** and ensure `.env.local` is configured
2. **Run `npm run dev`** to start frontend + backend
3. **Frontend**: http://localhost:3000
4. **Backend API**: http://localhost:8000/docs

## Kill Criteria

- No paying customer by 90 days from start date (July 26, 2026)
- LLM costs exceed 40% of ticket price
- Character consistency < 85% user satisfaction

## Status

**Current:** Pre-decision (as of April 26, 2026)
**Target:** First paying customer by August 26, 2026

---

For full strategic context, see `../agent_studio_strategy_memo.html`
