from typing import Any

from fastapi import status

class AppException(Exception):
    """Базовый класс для всех ошибок приложения."""
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "Произошла ошибка приложения"

    def __init__(self, message: str | None = None):
        if message:
            self.message = message

class InvalidCredentialsError(AppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Неверный логин или пароль"

class ProfileNotFoundError(AppException):
    status_code = status.HTTP_404_NOT_FOUND
    message = "Пользователь не найден"

class UserAlreadyExistsError(AppException):
    status_code = status.HTTP_409_CONFLICT
    message = "Пользователь с таким email уже зарегистрирован"

    