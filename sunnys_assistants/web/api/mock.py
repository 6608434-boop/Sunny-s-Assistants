"""
Mock API endpoints for Sunny's Assistants admin interface.
Provides fake data for frontend development until real backends are ready.
"""

from fastapi import APIRouter, Query
import logging
from typing import Optional, List, Dict, Any

from sunnys_assistants.web.api.mock_data import (
    SOLAR_SYSTEM,
    EARTH_GATES,
    LOGAN_PROFILE,
    LOGAN_CONTEXT,
    FAVORITES,
    HISTORY,
    SEARCH_RESULTS,
    PLANET_GATES,
)

logger = logging.getLogger(__name__)
router = APIRouter()


# ============================================================================
# УРОВЕНЬ 0: Солнечная система
# ============================================================================

@router.get("/solar/system")
async def get_solar_system():
    """
    Возвращает данные Солнечной системы:
    - Солнце с главными метриками
    - Все планеты с их характеристиками
    """
    logger.debug("GET /solar/system - returning solar system data")
    return SOLAR_SYSTEM


# ============================================================================
# УРОВЕНЬ 1: Планеты и их соты
# ============================================================================

@router.get("/planet/{planet_id}/gates")
async def get_planet_gates(planet_id: str):
    """
    Возвращает все соты для указанной планеты.

    - planet_id: mercury, venus, earth, mars, jupiter, saturn, deep-space
    """
    logger.debug(f"GET /planet/{planet_id}/gates")

    if planet_id in PLANET_GATES:
        return PLANET_GATES[planet_id]

    # Заглушка для неизвестной планеты
    return {
        "planet_id": planet_id,
        "gates": [],
        "message": "No gates available for this planet (mock)",
    }


@router.get("/planet/earth/gates")
async def get_earth_gates_only():
    """Быстрый доступ к сотам Земли"""
    return EARTH_GATES


# ============================================================================
# УРОВЕНЬ 2: Профили и их категории
# ============================================================================

@router.get("/profile/{profile_id}/categories")
async def get_profile_categories(profile_id: str):
    """
    Возвращает категории настроек для указанного профиля.

    - profile_id: logan, harper, dorian, sam, ray, liam, ellie, flynn, luna,
                  alice, kai, ira, mark, jace, vera
    """
    logger.debug(f"GET /profile/{profile_id}/categories")

    if profile_id == "logan":
        return LOGAN_PROFILE

    # Заглушка для других профилей
    return {
        "profile_id": profile_id,
        "categories": [],
        "message": "No categories available for this profile (mock)",
    }


# ============================================================================
# УРОВЕНЬ 3: Категории и их настройки
# ============================================================================

@router.get("/category/{category_id}/settings")
async def get_category_settings(category_id: str):
    """
    Возвращает детальные настройки для указанной категории.

    - category_id: logan_basic, logan_context, logan_ai, logan_security,
                  logan_integrations, logan_debug, folder_1_king, etc.
    """
    logger.debug(f"GET /category/{category_id}/settings")

    if category_id == "logan_context":
        return LOGAN_CONTEXT

    # Заглушка для других категорий
    return {
        "category_id": category_id,
        "settings": [],
        "message": "No settings available for this category (mock)",
    }


# ============================================================================
# ИЗБРАННОЕ
# ============================================================================

@router.get("/favorites")
async def get_favorites():
    """Возвращает избранные соты пользователя"""
    logger.debug("GET /favorites")
    return FAVORITES


@router.post("/favorites/add/{cell_id}")
async def add_to_favorites(cell_id: str):
    """Добавляет соту в избранное"""
    logger.debug(f"POST /favorites/add/{cell_id}")
    return {"status": "added", "cell_id": cell_id}


@router.delete("/favorites/remove/{cell_id}")
async def remove_from_favorites(cell_id: str):
    """Удаляет соту из избранного"""
    logger.debug(f"DELETE /favorites/remove/{cell_id}")
    return {"status": "removed", "cell_id": cell_id}


# ============================================================================
# ПОИСК
# ============================================================================

@router.get("/search")
async def search(
        query: str = Query(..., min_length=1, description="Поисковый запрос"),
        limit: int = Query(10, ge=1, le=50, description="Максимальное количество результатов")
):
    """
    Глобальный поиск по всем сотам системы.
    Ищет по названию соты и её метрикам.
    """
    logger.debug(f"GET /search?q={query}&limit={limit}")

    # Простейшая фильтрация (в реальности будет полнотекстовый поиск)
    results = []
    for cell in SEARCH_RESULTS:
        if query.lower() in cell["name"].lower():
            results.append(cell)
        elif "beams" in cell:
            for beam in cell.get("beams", []):
                if query.lower() in str(beam.get("value", "")).lower():
                    results.append(cell)
                    break

    return {
        "query": query,
        "total": len(results[:limit]),
        "results": results[:limit],
    }


# ============================================================================
# ИСТОРИЯ
# ============================================================================

@router.get("/history")
async def get_history(limit: int = Query(20, ge=1, le=100)):
    """Возвращает историю действий пользователя"""
    logger.debug(f"GET /history?limit={limit}")
    return {
        "total": len(HISTORY[:limit]),
        "history": HISTORY[:limit],
    }


@router.get("/history/search")
async def search_history(
        query: str = Query(..., min_length=1),
        limit: int = Query(20, ge=1, le=100)
):
    """Поиск по истории действий"""
    logger.debug(f"GET /history/search?q={query}&limit={limit}")

    results = [
        item for item in HISTORY
        if query.lower() in item["action"].lower()
    ]

    return {
        "query": query,
        "total": len(results[:limit]),
        "results": results[:limit],
    }


# ============================================================================
# НАСТРОЙКИ ВИЗУАЛА
# ============================================================================

@router.get("/settings/visual")
async def get_visual_settings():
    """Возвращает текущие настройки визуала"""
    return {
        "animation_mode": "living_cosmos",  # storm, living_cosmos, work, static, eco
        "theme": "milky_way",  # milky_way, andromeda, triangle, whirlpool, sombrero
        "glitch_intensity": 0.7,
        "beam_delay": 2000,  # миллисекунды
        "cache_interval": 60,  # секунды
    }


@router.post("/settings/visual")
async def update_visual_settings(settings: dict):
    """Обновляет настройки визуала"""
    logger.debug(f"POST /settings/visual - {settings}")
    # В мок-версии просто возвращаем то же
    return {
        **settings,
        "status": "saved",
        "message": "Visual settings updated (mock)",
    }