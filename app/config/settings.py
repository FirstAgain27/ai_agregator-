from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or a .env file."""

    app_name: str = Field(default="ai-agregator", description="Application name")
    debug: bool = Field(default=False, description="Enable debug mode")
    database_url: str = Field(
        default="postgresql://user:password@localhost:5432/dbname",
        description="Database connection URL",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()