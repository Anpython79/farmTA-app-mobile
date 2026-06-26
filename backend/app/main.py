"""FastAPI Main Application Entry Point"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import init_db
from app.routes import animals_router, hatchery_router, medicines_router, costs_router
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="Farm Management System API - Hệ thống quản lý trang trại",
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_credentials,
    allow_methods=settings.cors_methods,
    allow_headers=settings.cors_headers,
)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    try:
        init_db()
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.error(f"❌ Error initializing database: {e}")

# Health check endpoint
@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "✅ healthy",
        "app": settings.app_name,
        "version": settings.app_version,
        "message": "API is running smoothly!"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with welcome message"""
    return {
        "message": f"🎉 Welcome to {settings.app_name}",
        "version": settings.app_version,
        "description": "Farm Management System API",
        "docs": "/docs",
        "redoc": "/redoc",
        "api_prefix": settings.api_prefix,
        "endpoints": {
            "animals": "/api/v1/animals",
            "hatchery": "/api/v1/hatchery",
            "medicines": "/api/v1/medicines",
            "costs": "/api/v1/costs",
            "health": "/api/v1/health"
        }
    }

# Include routers with API prefix
app.include_router(
    animals_router,
    prefix="/api/v1",
    tags=["Animals"]
)

app.include_router(
    hatchery_router,
    prefix="/api/v1",
    tags=["Hatchery"]
)

app.include_router(
    medicines_router,
    prefix="/api/v1",
    tags=["Medicines"]
)

app.include_router(
    costs_router,
    prefix="/api/v1",
    tags=["Costs"]
)

# API Documentation Info
@app.get("/api/v1/docs-info")
async def docs_info():
    """API Documentation Info"""
    return {
        "api_version": "v1",
        "base_url": "http://localhost:8000/api/v1",
        "documentation": "http://localhost:8000/docs",
        "contact": {
            "name": "FarmTA Support",
            "email": "support@farmta.com"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug
    )
