from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """Базовые поля пользователя, которые используются и на вход, и на выход."""
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    username: str = Field(
        ..., 
        min_length=3, 
        max_length=50, 
        pattern=r"^[a-zA-Z0-9_-]+$",
        description="Уникальное имя пользователя (только латиница, цифры, подчёркивания и дефисы)"
    )


class UserCreate(UserBase):
    """Схема для регистрации нового пользователя.
    Принимает сырой пароль, который бэкенд затем захэширует.
    """
    password: str = Field(..., min_length=8, max_length=100, description="Сырой пароль пользователя")


class UserUpdate(BaseModel):
    """Схема для частичного обновления профиля (PATCH-запрос).
    Все поля необязательны, чтобы можно было обновить только то, что изменилось.
    """
    email: Optional[EmailStr] = Field(None, description="Новая электронная почта")
    username: Optional[str] = Field(None, min_length=3, max_length=50, description="Новое имя пользователя")
    password: Optional[str] = Field(None, min_length=8, max_length=100, description="Новый пароль")


class UserResponse(UserBase):
    """Схема для отдачи данных клиента наружу.
    Пароль сюда не включается из соображений безопасности.
    """
    id: int = Field(..., description="Уникальный ID пользователя из базы данных")
    is_active: bool = Field(..., description="Статус активности аккаунта")
    created_at: datetime = Field(..., description="Дата и время регистрации")

    # Позволяет Pydantic автоматически парсить объекты SQLAlchemy (ORM)
    model_config = ConfigDict(from_attributes=True)
