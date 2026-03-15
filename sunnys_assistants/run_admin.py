#!/usr/bin/env python
"""
Development server runner for Sunny's Assistants admin interface.
Starts the FastAPI server with auto-reload for development.
"""

import uvicorn
import logging
from sunnys_assistants.core.config import settings

# Настройка логирования
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info(f"Starting {settings.app_name} admin interface")
    logger.info(f"Debug mode: {settings.debug}")
    logger.info(f"Mock mode: {settings.mock_mode}")

    uvicorn.run(
        "sunnys_assistants.web.server:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )