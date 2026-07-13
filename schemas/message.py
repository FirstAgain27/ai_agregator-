from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field

# Определяем тип для ролей ИИ. Pydantic V2 отвалидирует строку 
# и не пропустит ничего, кроме этих трех значений.
AIRole = Literal["user", "assistant", "system"]


class MessageBase(BaseModel):
    """Базовые поля сообщения."""
    content: str = Field(..., description="Текст самого сообщения")


class MessageCreate(MessageBase):
    """Схема для отправки нового сообщения пользователем.
    
    Сюда не включаются conversation_id (берется из URL) и tokens_used (считается бэкендом).
    По умолчанию роль ставится как 'user', но мы оставляем возможность передать 'system',
    если нужно будет динамически подкидывать системные промты.
    """
    role: AIRole = Field(default="user", description="Роль отправителя сообщения")


class MessageResponse(MessageBase):
    """Схема для отдачи сообщения наружу. 
    Именно этот формат будет использоваться внутри списка историй диалога.
    """
    id: int = Field(..., description="Уникальный ID сообщения в базе")
    role: AIRole = Field(..., description="Роль (user, assistant, system)")
    conversation_id: int = Field(..., description="ID диалога, к которому привязано сообщение")
    tokens_used: Optional[int] = Field(
        None, 
        description="Количество затраченных токенов (заполняется бэкендом после ответа модели)"
    )
    created_at: datetime = Field(..., description="Время создания сообщения")

    # Включаем совместимость с моделями SQLAlchemy (ORM)
    model_config = ConfigDict(from_attributes=True)