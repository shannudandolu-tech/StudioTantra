from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config import settings

# Initialize FastAPI app
app = FastAPI(
    title="Studio Tantra API",
    description="AI ad creative platform orchestration engine",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "ok",
        "environment": settings.environment,
        "api_version": "0.1.0",
    }

@app.get("/config")
async def config():
    """Get non-sensitive configuration"""
    return {
        "environment": settings.environment,
        "api_url": settings.api_url,
        "features": {
            "brief_parser": True,
            "identity_lock": True,
            "scene_renderer": True,
            "voice_dub": True,
            "editor_mux": True,
            "critique_qa": True,
        },
    }

@app.post("/api/v1/jobs")
async def create_job(brief: dict):
    """Create a new ad generation job"""
    return {
        "job_id": "job_001",
        "status": "queued",
        "brief": brief,
    }

@app.get("/api/v1/jobs/{job_id}")
async def get_job_status(job_id: str):
    """Get job status"""
    return {
        "job_id": job_id,
        "status": "processing",
        "progress": 45,
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.environment == "development",
    )
