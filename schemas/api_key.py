from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, SecretStr


class ApiKeyBase(BaseModel):
    """Базовая схема с общими полями для API-ключа."""
    provider_name: str = Field(
        ..., 
        min_length=2, 
        max_length=50, 
        description="Название ИИ-провайдера (например: 'openai', 'anthropic', 'yandex')"
    )


class ApiKeyCreate(ApiKeyBase):
    """Схема для добавления нового API-ключа.
    Использует SecretStr, чтобы сырой ключ не попал в логи приложения.
    """
    api_key: SecretStr = Field(
        ..., 
        min_length=10, 
        max_length=500, 
        description="Сырой API-ключ, полученный от провайдера"
    )


class ApiKeyUpdate(BaseModel):
    """Схема для обновления ключа (например, если пользователь решил его перевыпустить)."""
    api_key: Optional[SecretStr] = Field(None, min_length=10, max_length=500)


class ApiKeyResponse(ApiKeyBase):
    """Схема для безопасного вывода информации о ключе.
    В целях безопасности мы ВООБЩЕ не возвращаем зашифрованный ключ наружу,
    даже в формате хэша. Фронтенду достаточно знать, что ключ для этого провайдера существует.
    """
    id: int = Field(..., description="ID записи в базе данных")
    user_id: int = Field(..., description="ID владельца ключа")
    created_at: datetime = Field(..., description="Дата и время добавления ключа")

    # Включаем чтение из ORM моделей SQLAlchemy
    model_config = ConfigDict(from_attributes=True)