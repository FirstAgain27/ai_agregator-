from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or a .env file."""

    APP_NAME: str = Field(default="ai-agregator", description="Application name")
    DEBUG: bool = Field(default=False, description="Debug mode")
    ASYNC_DATABASE_URL: str = Field(
        default="sqlite+aiosqlite:///:memory:", description="Async database URL"
    )

    SECRET_KEY: str = Field(
        ...,
        description="Secret key for signing JWT tokens",
    )
    ALGORITHM: str = Field(default="HS256", description="JWT signing algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=30, description="Access token lifespan in minutes"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,  # Автоматически свяжет SECRET_KEY из .env с SECRET_KEY в классе
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()