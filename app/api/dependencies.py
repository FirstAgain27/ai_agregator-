from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.config.database import get_async_db
from repositories.user import UserRepository
from services.auth import AuthService

def get_user_repository(    # Делаем функцию синхронной, так как внутри нет ни одного await 
        db: AsyncSession = Depends(get_async_db)
    ) -> UserRepository: 
    
    return UserRepository(db)

def get_auth_service(   # Делаем функцию синхронной, так как внутри нет ни одного await
        db: AsyncSession = Depends(get_async_db),
        user_repo = Depends(get_user_repository)
    ) -> AuthService:
    return AuthService(db, user_repo)
    
