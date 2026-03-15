"""
FastAPI server for Sunny's Assistants web interfaces.
Currently serves admin dashboard with mock data.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from sunnys_assistants.core.config import settings
from sunnys_assistants.web.api import mock

# Настройка логирования
logger = logging.getLogger(__name__)

# Создание FastAPI приложения
app = FastAPI(
    title=f"{settings.app_name} API",
    description="Admin and user web interfaces",
    version="1.0.0",
    debug=settings.debug,
)

# Настройка CORS для разработки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение моковых роутов (временно)
app.include_router(mock.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    """Health check endpoint для мониторинга"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "mock_mode": settings.mock_mode,
        "debug": settings.debug,
    }

@app.get("/")
async def root():
    """Корневой endpoint, перенаправляет на документацию"""
    return {
        "message": f"Welcome to {settings.app_name}",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health",
    }

logger.info("Web server initialized with mock mode: %s", settings.mock_mode)