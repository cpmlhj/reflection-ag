from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import health

app = FastAPI(
    title="Reflection Agent API",
    description="Backend API for Reflection Agent application",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Reflection Agent API",
        "version": "0.1.0",
        "docs": "/docs",
    }
