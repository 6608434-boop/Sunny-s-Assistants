"""
Mock data for Sunny's Assistants admin interface.
All data is static for frontend development.
"""

from typing import List, Dict, Any

# ============================================================================
# УРОВЕНЬ 0: СОЛНЕЧНАЯ СИСТЕМА
# ============================================================================

SOLAR_SYSTEM = {
    "sun": {
        "id": "sun",
        "name": "Солнце",
        "metrics": [
            {"label": "Активных сессий", "value": 1247, "change": "+12%"},
            {"label": "Доход сегодня", "value": 84300, "unit": "₽", "change": "+5%"},
            {"label": "Новых пользователей", "value": 45, "change": "+3%"},
            {"label": "Здоровье системы", "value": "98%", "status": "healthy"}
        ]
    },
    "planets": [
        {
            "id": "mercury",
            "name": "Меркурий",
            "display_name": "Коммуникации",
            "color": "#A9A9A9",
            "position": 1,
            "gates_count": 6,
            "description": "Каналы связи с пользователями"
        },
        {
            "id": "venus",
            "name": "Венера",
            "display_name": "Финансы",
            "color": "#DAA520",
            "position": 2,
            "gates_count": 9,
            "description": "Платежи, подписки, транзакции"
        },
        {
            "id": "earth",
            "name": "Земля",
            "display_name": "Внутренняя кухня",
            "color": "#4169E1",
            "position": 3,
            "gates_count": 20,
            "description": "Команда и процессы разработки"
        },
        {
            "id": "mars",
            "name": "Марс",
            "display_name": "Профили ассистентов",
            "color": "#B22222",
            "position": 4,
            "gates_count": 16,
            "description": "Ассистенты для пользователей"
        },
        {
            "id": "jupiter",
            "name": "Юпитер",
            "display_name": "Инфраструктура",
            "color": "#D2B48C",
            "position": 5,
            "gates_count": 9,
            "description": "Техническая начинка"
        },
        {
            "id": "saturn",
            "name": "Сатурн",
            "display_name": "Внешние интеграции",
            "color": "#F4A460",
            "position": 6,
            "gates_count": 7,
            "description": "Банки, госорганы, API"
        },
        {
            "id": "deep-space",
            "name": "Дальний космос",
            "display_name": "Будущее",
            "color": "#483D8B",
            "position": 7,
            "gates_count": 4,
            "description": "R&D, Энцелат, блокчейн"
        }
    ]
}

# ============================================================================
# УРОВЕНЬ 1: ЗЕМЛЯ (20 сот)
# ============================================================================

EARTH_GATES = [
    # Профили команды (14 шт)
    {
        "id": "logan",
        "name": "Логан",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.8,
        "glitch_intensity": 0.7,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "2 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Рефакторинг storage"},
            {"angle": -15, "label": "Коммитов сегодня", "value": 3},
            {"angle": -30, "label": "Ошибок", "value": 0},
            {"angle": -45, "label": "Связан с", "value": "Харпер, Дориан"}
        ],
        "path": ["solar", "earth", "logan"]
    },
    {
        "id": "harper",
        "name": "Харпер",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.6,
        "glitch_intensity": 0.5,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "15 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Настройка Яндекс.Диска"},
            {"angle": -15, "label": "Коммитов сегодня", "value": 1},
            {"angle": -30, "label": "Ошибок", "value": 0}
        ],
        "path": ["solar", "earth", "harper"]
    },
    {
        "id": "dorian",
        "name": "Дориан",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.7,
        "glitch_intensity": 0.6,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "5 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Оптимизация контекста"},
            {"angle": -15, "label": "Коммитов сегодня", "value": 2}
        ],
        "path": ["solar", "earth", "dorian"]
    },
    {
        "id": "sam",
        "name": "Сэм",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.5,
        "glitch_intensity": 0.5,
        "status": "idle",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟡 Ожидание"},
            {"angle": 30, "label": "Последняя активность", "value": "1 час назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Ждёт задачу"}
        ],
        "path": ["solar", "earth", "sam"]
    },
    {
        "id": "ray",
        "name": "Рэй",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.9,
        "glitch_intensity": 0.8,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "1 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "GitHub sync"},
            {"angle": -15, "label": "Коммитов сегодня", "value": 5}
        ],
        "path": ["solar", "earth", "ray"]
    },
    {
        "id": "liam",
        "name": "Лиам",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.6,
        "glitch_intensity": 0.5,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "10 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Сканирование проектов"}
        ],
        "path": ["solar", "earth", "liam"]
    },
    {
        "id": "ellie",
        "name": "Элли",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.7,
        "glitch_intensity": 0.6,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "3 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Чистка чатов"}
        ],
        "path": ["solar", "earth", "ellie"]
    },
    {
        "id": "flynn",
        "name": "Флинн",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.5,
        "glitch_intensity": 0.4,
        "status": "idle",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟡 Ожидание"},
            {"angle": 30, "label": "Последняя активность", "value": "30 мин назад"}
        ],
        "path": ["solar", "earth", "flynn"]
    },
    {
        "id": "luna",
        "name": "Луна",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.8,
        "glitch_intensity": 0.7,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "5 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Рисует админку"}
        ],
        "path": ["solar", "earth", "luna"]
    },
    {
        "id": "alice",
        "name": "Алиса",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.6,
        "glitch_intensity": 0.5,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "7 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Пишет тесты"}
        ],
        "path": ["solar", "earth", "alice"]
    },
    {
        "id": "kai",
        "name": "Кай",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.4,
        "glitch_intensity": 0.3,
        "status": "idle",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "⚪ Офлайн"},
            {"angle": 30, "label": "Последняя активность", "value": "2 часа назад"}
        ],
        "path": ["solar", "earth", "kai"]
    },
    {
        "id": "ira",
        "name": "Ира",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.7,
        "glitch_intensity": 0.6,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "12 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Пишет документацию"}
        ],
        "path": ["solar", "earth", "ira"]
    },
    {
        "id": "mark",
        "name": "Марк",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.6,
        "glitch_intensity": 0.5,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟢 Активен"},
            {"angle": 30, "label": "Последняя активность", "value": "20 мин назад"},
            {"angle": 15, "label": "Текущая задача", "value": "Анализ требований"}
        ],
        "path": ["solar", "earth", "mark"]
    },
    {
        "id": "jace",
        "name": "Джейс",
        "planet": "earth",
        "type": "profile",
        "color": "gold",
        "glitch_speed": 0.5,
        "glitch_intensity": 0.4,
        "status": "idle",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Статус", "value": "🟡 Ожидание"},
            {"angle": 30, "label": "Последняя активность", "value": "45 мин назад"}
        ],
        "path": ["solar", "earth", "jace"]
    },

    # Инструменты (6 шт)
    {
        "id": "adr",
        "name": "Архитектурные решения",
        "planet": "earth",
        "type": "tool",
        "color": "blue",
        "glitch_speed": 0.3,
        "glitch_intensity": 0.4,
        "status": "idle",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Всего ADR", "value": 12},
            {"angle": 30, "label": "Последнее", "value": "2026-03-14"},
            {"angle": 15, "label": "Автор", "value": "Логан"}
        ],
        "path": ["solar", "earth", "adr"]
    },
    {
        "id": "tasks",
        "name": "Задачи",
        "planet": "earth",
        "type": "tool",
        "color": "blue",
        "glitch_speed": 0.6,
        "glitch_intensity": 0.5,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "В работе", "value": 7},
            {"angle": 30, "label": "На проверке", "value": 3},
            {"angle": 15, "label": "Просрочено", "value": 1}
        ],
        "path": ["solar", "earth", "tasks"]
    },
    {
        "id": "releases",
        "name": "Релизы",
        "planet": "earth",
        "type": "tool",
        "color": "blue",
        "glitch_speed": 0.2,
        "glitch_intensity": 0.3,
        "status": "idle",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Текущая версия", "value": "1.2.0"},
            {"angle": 30, "label": "Следующий релиз", "value": "1.3.0"},
            {"angle": 15, "label": "Дата", "value": "2026-04-01"}
        ],
        "path": ["solar", "earth", "releases"]
    },
    {
        "id": "tests",
        "name": "Тесты",
        "planet": "earth",
        "type": "tool",
        "color": "green",
        "glitch_speed": 0.7,
        "glitch_intensity": 0.6,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Покрытие", "value": "87%"},
            {"angle": 30, "label": "Всего тестов", "value": 342},
            {"angle": 15, "label": "Упало", "value": 2}
        ],
        "path": ["solar", "earth", "tests"]
    },
    {
        "id": "docs",
        "name": "Документация",
        "planet": "earth",
        "type": "tool",
        "color": "blue",
        "glitch_speed": 0.3,
        "glitch_intensity": 0.3,
        "status": "idle",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Документов", "value": 24},
            {"angle": 30, "label": "Последнее обновление", "value": "2026-03-13"}
        ],
        "path": ["solar", "earth", "docs"]
    },
    {
        "id": "logs",
        "name": "Логи системы",
        "planet": "earth",
        "type": "tool",
        "color": "purple",
        "glitch_speed": 0.9,
        "glitch_intensity": 0.8,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Ошибок за час", "value": 3},
            {"angle": 30, "label": "Warnings", "value": 12},
            {"angle": 15, "label": "Последняя ошибка", "value": "2026-03-15 10:32"}
        ],
        "path": ["solar", "earth", "logs"]
    }
]

# ============================================================================
# УРОВЕНЬ 2: ПРОФИЛЬ ЛОГАНА (6 категорий)
# ============================================================================

LOGAN_PROFILE = [
    {
        "id": "logan_basic",
        "name": "Базовые",
        "profile_id": "logan",
        "type": "category",
        "color": "gold",
        "glitch_speed": 0.5,
        "glitch_intensity": 0.5,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Роль", "value": "Главный инженер"},
            {"angle": 30, "label": "Версия", "value": "1.3"},
            {"angle": 15, "label": "Статус", "value": "🟢 Активен"},
            {"angle": -15, "label": "Создан", "value": "2022-08-04"}
        ],
        "path": ["solar", "earth", "logan", "basic"]
    },
    {
        "id": "logan_context",
        "name": "Контекст",
        "profile_id": "logan",
        "type": "category",
        "color": "blue",
        "glitch_speed": 0.6,
        "glitch_intensity": 0.5,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Папок", "value": 16},
            {"angle": 30, "label": "Внешних источников", "value": 2},
            {"angle": 15, "label": "Обновление", "value": "ежедневно"},
            {"angle": -15, "label": "Приоритет", "value": "1_КИНГ: 100"}
        ],
        "path": ["solar", "earth", "logan", "context"]
    },
    {
        "id": "logan_ai",
        "name": "AI параметры",
        "profile_id": "logan",
        "type": "category",
        "color": "orange",
        "glitch_speed": 0.4,
        "glitch_intensity": 0.4,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Модель", "value": "deepseek-chat"},
            {"angle": 30, "label": "Температура", "value": "0.7"},
            {"angle": 15, "label": "Max tokens", "value": "32000"},
            {"angle": -15, "label": "Tone", "value": "mixed"}
        ],
        "path": ["solar", "earth", "logan", "ai"]
    },
    {
        "id": "logan_security",
        "name": "Безопасность",
        "profile_id": "logan",
        "type": "category",
        "color": "red",
        "glitch_speed": 0.3,
        "glitch_intensity": 0.3,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Доступ", "value": "Только админ"},
            {"angle": 30, "label": "Лимит запросов", "value": "1000/день"},
            {"angle": 15, "label": "Последний вход", "value": "2026-03-15"}
        ],
        "path": ["solar", "earth", "logan", "security"]
    },
    {
        "id": "logan_integrations",
        "name": "Интеграции",
        "profile_id": "logan",
        "type": "category",
        "color": "purple",
        "glitch_speed": 0.5,
        "glitch_intensity": 0.4,
        "status": "idle",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "GitHub", "value": "Подключено"},
            {"angle": 30, "label": "Яндекс.Диск", "value": "Подключено"},
            {"angle": 15, "label": "Библиотека", "value": "Не подключено"}
        ],
        "path": ["solar", "earth", "logan", "integrations"]
    },
    {
        "id": "logan_debug",
        "name": "Отладка",
        "profile_id": "logan",
        "type": "category",
        "color": "green",
        "glitch_speed": 0.8,
        "glitch_intensity": 0.7,
        "status": "active",
        "is_loading": False,
        "beams": [
            {"angle": 45, "label": "Ошибок сегодня", "value": 0},
            {"angle": 30, "label": "Последний лог", "value": "2026-03-15 09:15"},
            {"angle": 15, "label": "Уровень", "value": "DEBUG"}
        ],
        "path": ["solar", "earth", "logan", "debug"]
    }
]

# ============================================================================
# УРОВЕНЬ 3: КАТЕГОРИЯ КОНТЕКСТА (настройки)
# ============================================================================

LOGAN_CONTEXT = [
    # Папки (первые 8 из 16 для примера)
    {
        "id": "folder_1_king",
        "name": "1_КИНГ",
        "category_id": "logan_context",
        "type": "folder_setting",
        "priority": 100,
        "controls": [
            {"type": "slider", "label": "Приоритет", "min": 0, "max": 100, "value": 100},
            {"type": "checkboxes", "label": "Форматы",
             "options": [".txt", ".md", ".pdf", ".jpg", ".json", ".py"],
             "selected": [".txt", ".md", ".json", ".py"]},
            {"type": "slider", "label": "Макс. файлов", "min": 10, "max": 500, "value": 100},
            {"type": "radio", "label": "Кэширование",
             "options": ["Нет", "1 час", "1 день"], "selected": "1 час"}
        ]
    },
    {
        "id": "folder_2_profi",
        "name": "2_ПРОФИ",
        "category_id": "logan_context",
        "type": "folder_setting",
        "priority": 90,
        "controls": [
            {"type": "slider", "label": "Приоритет", "min": 0, "max": 100, "value": 90},
            {"type": "checkboxes", "label": "Форматы",
             "options": [".txt", ".md", ".pdf", ".jpg", ".json", ".py"],
             "selected": [".txt", ".md", ".json"]},
            {"type": "slider", "label": "Макс. файлов", "min": 10, "max": 500, "value": 80},
        ]
    },
    {
        "id": "folder_3_soft",
        "name": "3_СОФТ",
        "category_id": "logan_context",
        "type": "folder_setting",
        "priority": 85,
        "controls": [
            {"type": "slider", "label": "Приоритет", "min": 0, "max": 100, "value": 85},
            {"type": "checkboxes", "label": "Форматы",
             "options": [".txt", ".md", ".pdf", ".jpg", ".json", ".py"],
             "selected": [".txt", ".md"]},
        ]
    },
    {
        "id": "folder_4_memory",
        "name": "4_ПАМЯТЬ",
        "category_id": "logan_context",
        "type": "folder_setting",
        "priority": 80,
        "controls": [
            {"type": "slider", "label": "Приоритет", "min": 0, "max": 100, "value": 80},
            {"type": "checkboxes", "label": "Форматы",
             "options": [".txt", ".md", ".pdf", ".jpg", ".json", ".py"],
             "selected": [".md", ".json"]},
        ]
    },
    {
        "id": "folder_5_base",
        "name": "5_БАЗА",
        "category_id": "logan_context",
        "type": "folder_setting",
        "priority": 70,
        "controls": [
            {"type": "slider", "label": "Приоритет", "min": 0, "max": 100, "value": 70},
        ]
    },
    {
        "id": "folder_6_relations",
        "name": "6_ОТНОШЕНИЯ",
        "category_id": "logan_context",
        "type": "folder_setting",
        "priority": 75,
        "controls": [
            {"type": "slider", "label": "Приоритет", "min": 0, "max": 100, "value": 75},
        ]
    },
    {
        "id": "folder_7_evolution",
        "name": "7_ЭВОЛЮЦИЯ",
        "category_id": "logan_context",
        "type": "folder_setting",
        "priority": 60,
        "controls": [
            {"type": "slider", "label": "Приоритет", "min": 0, "max": 100, "value": 60},
        ]
    },
    {
        "id": "folder_8_borders",
        "name": "8_ГРАНИЦЫ",
        "category_id": "logan_context",
        "type": "folder_setting",
        "priority": 95,
        "controls": [
            {"type": "slider", "label": "Приоритет", "min": 0, "max": 100, "value": 95},
        ]
    },

    # Внешние источники
    {
        "id": "source_github",
        "name": "GitHub",
        "category_id": "logan_context",
        "type": "external_source",
        "enabled": True,
        "controls": [
            {"type": "toggle", "label": "Включено", "value": True},
            {"type": "slider", "label": "Вес источника", "min": 0, "max": 100, "value": 60},
            {"type": "textarea", "label": "Репозитории", "value": "sunnys-assistants/core\nsunnys-assistants/web"}
        ]
    },
    {
        "id": "source_library",
        "name": "Библиотека",
        "category_id": "logan_context",
        "type": "external_source",
        "enabled": True,
        "controls": [
            {"type": "toggle", "label": "Включено", "value": True},
            {"type": "slider", "label": "Вес источника", "min": 0, "max": 100, "value": 40},
        ]
    },
    {
        "id": "update_frequency",
        "name": "Частота обновления",
        "category_id": "logan_context",
        "type": "global_setting",
        "controls": [
            {"type": "radio", "label": "Обновление контекста",
             "options": ["Каждый час", "Каждый день", "По запросу"],
             "selected": "Каждый день"}
        ]
    }
]

# ============================================================================
# ИЗБРАННОЕ
# ============================================================================

FAVORITES = {
    "categories": [
        {
            "name": "Часто используемые",
            "cells": [
                {"id": "logan", "name": "Логан", "depth": 2, "size": "large", "usage_count": 150},
                {"id": "venus_revenue", "name": "Доход", "depth": 1, "size": "large", "usage_count": 120},
                {"id": "tasks", "name": "Задачи", "depth": 1, "size": "medium", "usage_count": 85},
            ]
        },
        {
            "name": "Недавние",
            "cells": [
                {"id": "folder_1_king", "name": "1_КИНГ", "depth": 4, "size": "medium", "usage_count": 45},
                {"id": "logs", "name": "Логи системы", "depth": 1, "size": "small", "usage_count": 30},
                {"id": "tests", "name": "Тесты", "depth": 1, "size": "small", "usage_count": 25},
            ]
        }
    ]
}

# ============================================================================
# ИСТОРИЯ
# ============================================================================

HISTORY = [
    {"action": "Просмотр профиля Логан", "timestamp": "2026-03-15T10:32:00Z", "user": "admin"},
    {"action": "Изменение приоритета папки 1_КИНГ", "timestamp": "2026-03-15T10:15:00Z", "user": "admin"},
    {"action": "Загрузка данных с Венеры", "timestamp": "2026-03-15T09:58:00Z", "user": "system"},
    {"action": "Создание промо-ключа", "timestamp": "2026-03-15T09:22:00Z", "user": "admin"},
    {"action": "Запуск тестов", "timestamp": "2026-03-15T08:45:00Z", "user": "alice"},
    {"action": "Деплой версии 1.2.0", "timestamp": "2026-03-14T23:10:00Z", "user": "system"},
    {"action": "Обновление контекста Логана", "timestamp": "2026-03-14T22:30:00Z", "user": "system"},
    {"action": "Синхронизация с GitHub", "timestamp": "2026-03-14T21:15:00Z", "user": "ray"},
    {"action": "Ошибка: таймаут Яндекс.Диска", "timestamp": "2026-03-14T20:05:00Z", "user": "system", "type": "error"},
    {"action": "Новый пользователь: @vera", "timestamp": "2026-03-14T19:30:00Z", "user": "system"},
]

# ============================================================================
# ПОИСК (агрегированные данные для индексации)
# ============================================================================

SEARCH_RESULTS = EARTH_GATES + LOGAN_PROFILE + LOGAN_CONTEXT

# ============================================================================
# ДАННЫЕ ДЛЯ ВСЕХ ПЛАНЕТ (кратко)
# ============================================================================

PLANET_GATES = {
    "mercury": [
        {"id": "telegram_bot", "name": "Telegram бот", "type": "communication", "status": "active"},
        {"id": "telegram_channels", "name": "Telegram каналы", "type": "communication", "status": "idle"},
        {"id": "whatsapp", "name": "WhatsApp", "type": "communication", "status": "coming_soon"},
        {"id": "email", "name": "Email шлюз", "type": "communication", "status": "idle"},
        {"id": "push", "name": "Push уведомления", "type": "communication", "status": "idle"},
    ],
    "venus": [
        {"id": "subscriptions", "name": "Подписки", "type": "finance", "status": "active"},
        {"id": "pay_per_request", "name": "Pay-per-request", "type": "finance", "status": "active"},
        {"id": "transactions", "name": "Транзакции", "type": "finance", "status": "active"},
        {"id": "promo_keys", "name": "Промо-ключи", "type": "finance", "status": "active"},
        {"id": "holds", "name": "Холды", "type": "finance", "status": "idle"},
        {"id": "crypto", "name": "Криптовалюты", "type": "finance", "status": "idle"},
        {"id": "alfa", "name": "Альфа-банк", "type": "finance", "status": "idle"},
        {"id": "ozon", "name": "Озон-банк", "type": "finance", "status": "idle"},
        {"id": "yookassa", "name": "ЮKassa", "type": "finance", "status": "idle"},
    ],
    "mars": [
        {"id": "logan_user", "name": "Логан", "type": "profile", "status": "active"},
        {"id": "harper_user", "name": "Харпер", "type": "profile", "status": "active"},
        {"id": "dorian_user", "name": "Дориан", "type": "profile", "status": "active"},
        {"id": "sam_user", "name": "Сэм", "type": "profile", "status": "active"},
        {"id": "ray_user", "name": "Рэй", "type": "profile", "status": "active"},
        {"id": "liam_user", "name": "Лиам", "type": "profile", "status": "active"},
        {"id": "ellie_user", "name": "Элли", "type": "profile", "status": "active"},
        {"id": "flynn_user", "name": "Флинн", "type": "profile", "status": "active"},
        {"id": "luna_user", "name": "Луна", "type": "profile", "status": "active"},
        {"id": "alice_user", "name": "Алиса", "type": "profile", "status": "active"},
        {"id": "kai_user", "name": "Кай", "type": "profile", "status": "active"},
        {"id": "ira_user", "name": "Ира", "type": "profile", "status": "active"},
        {"id": "mark_user", "name": "Марк", "type": "profile", "status": "active"},
        {"id": "jace_user", "name": "Джейс", "type": "profile", "status": "active"},
        {"id": "vera_user", "name": "Вера", "type": "profile", "status": "active"},
    ],
    "jupiter": [
        {"id": "yandex", "name": "Яндекс.Диск", "type": "infra", "status": "active"},
        {"id": "github", "name": "GitHub", "type": "infra", "status": "active"},
        {"id": "deepseek", "name": "DeepSeek", "type": "infra", "status": "active"},
        {"id": "postgres", "name": "PostgreSQL", "type": "infra", "status": "active"},
        {"id": "redis", "name": "Redis", "type": "infra", "status": "active"},
        {"id": "prometheus", "name": "Prometheus", "type": "infra", "status": "active"},
        {"id": "grafana", "name": "Grafana", "type": "infra", "status": "active"},
        {"id": "loki", "name": "Loki", "type": "infra", "status": "active"},
        {"id": "go_services", "name": "Go сервисы", "type": "infra", "status": "active"},
    ],
    "saturn": [
        {"id": "alfa_integration", "name": "Альфа-банк", "type": "integration", "status": "idle"},
        {"id": "ozon_integration", "name": "Озон-банк", "type": "integration", "status": "idle"},
        {"id": "yookassa_integration", "name": "ЮKassa", "type": "integration", "status": "idle"},
        {"id": "solana", "name": "Solana", "type": "integration", "status": "idle"},
        {"id": "trc20", "name": "TRC-20", "type": "integration", "status": "idle"},
    ],
    "deep-space": [
        {"id": "enceladus", "name": "Энцелат", "type": "future", "status": "research"},
        {"id": "blockchain", "name": "Блокчейн", "type": "future", "status": "research"},
        {"id": "ar_vr", "name": "AR/VR", "type": "future", "status": "coming_soon"},
        {"id": "quantum", "name": "Квантовые вычисления", "type": "future", "status": "easter_egg"},
    ]
}