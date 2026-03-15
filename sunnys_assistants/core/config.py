"""
Configuration management for Sunny's Assistants.
Uses Pydantic Settings for type-safe environment variables.
"""

from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    All values can be overridden in .env file.
    """

    # Application info
    app_name: str = "Sunny's Assistants"
    debug: bool = False
    log_level: str = "INFO"

    # Mode flags
    mock_mode: bool = True  # If True, use mock data instead of real services

    # Database
    database_url: Optional[str] = None

    # Яндекс.Диск
    yandex_client_id: Optional[str] = None
    yandex_client_secret: Optional[str] = None
    yandex_refresh_token: Optional[str] = None
    yandex_grpc_address: str = "localhost:50051"

    # GitHub
    github_token: Optional[str] = None
    github_grpc_address: str = "localhost:50052"

    # DeepSeek
    deepseek_api_key: Optional[str] = None
    deepseek_api_url: str = "https://api.deepseek.com"
    deepseek_grpc_address: str = "localhost:50053"

    # Telegram
    telegram_bot_token: Optional[str] = None
    telegram_webhook_secret: Optional[str] = None
    telegram_webhook_url: Optional[str] = None
    telegram_grpc_address: str = "localhost:50054"

    # Storage type (local or yandex)
    storage_type: str = "local"
    local_storage_path: str = "./data"

    # Payment gateways
    alfa_api_url: str = "https://alfabank.ru/api"
    alfa_api_key: Optional[str] = None
    alfa_webhook_secret: Optional[str] = None

    ozon_api_url: str = "https://ozon.ru/api"
    ozon_api_key: Optional[str] = None
    ozon_webhook_secret: Optional[str] = None

    yookassa_shop_id: Optional[str] = None
    yookassa_secret_key: Optional[str] = None

    # Crypto
    solana_rpc_url: str = "https://api.mainnet-beta.solana.com"
    seller_wallet_private_key: Optional[str] = None

    # Monitoring
    prometheus_port: int = 9090
    grafana_port: int = 3000
    loki_url: str = "http://loki:3100"

    # Admin IDs
    owner_ids: List[int] = []
    vera_user_id: Optional[int] = None

    # Cache settings
    cache_ttl: int = 60  # seconds
    cache_enabled: bool = True

    # Visual settings (defaults)
    default_animation_mode: str = "living_cosmos"  # storm, living_cosmos, work, static, eco
    default_theme: str = "milky_way"  # milky_way, andromeda, triangle, whirlpool, sombrero

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()