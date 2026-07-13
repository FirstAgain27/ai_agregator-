from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime 
from app.schemas.message import MessageResponse


class ConversationBase(BaseModel):
    title: Optional[str] = Field(
        default="Новый диалог", 
        max_length=80,
        description="Название чата, отображаемое в истории"
        )
    provider_name: str = Field(
        ..., 
        min_length=2, 
        max_length=50, 
        description="ИИ-провайдер, к которому привязан чат (openai, deepseek и т.д.)"
    )
    model_id: str = Field(
        ..., 
        min_length=1, 
        max_length=100, 
        description="Конкретная модель ИИ (например, gpt-4o, claude-3-5-sonnet)"
    )


class ConversationCreate(ConversationBase):
    """Схема для создания нового диалога.
    user_id не передается в теле запроса, бэкенд возьмет его из JWT-токена.
    """
    pass


class ConversationUpdate(BaseModel):
    """Схема для редактирования диалога (например, переименование чата пользователем).
    Провайдера и модель менять посреди чата запрещено, поэтому меняем только title.
    """
    title: str = Field(..., min_length=1, max_length=80, description="Новое название диалога")


class ConversationResponse(ConversationBase):
    """Схема для отдачи информации о диалоге наружу (например, для списка чатов в сайдбаре)."""
    id: int = Field(..., description="Уникальный ID диалога")
    user_id: int = Field(..., description="ID владельца диалога")
    created_at: datetime = Field(..., description="Время создания чата")
    updated_at: datetime = Field(..., description="Время последнего обновления (нового сообщения)")

    model_config = ConfigDict(from_attributes=True)


class ConversationDetailResponse(ConversationResponse):
    """Расширенная схема диалога, включающая в себя список всех сообщений.
    Используется при открытии конкретного чата.
    """
    messages: list[MessageResponse] = Field(
        default=[], 
        description="Список всех сообщений внутри этого диалога"
    )
    
    model_config = ConfigDict(from_attributes=True)