from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from models.user import User
from repositories.base import BaseRepository
from typing import Sequence


class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=User, session=session)

    async def get_by_email(self, email: str) -> User | None:
        return await self.session.scalar(
            select(User).where(User.email == email)
        )

    async def get_by_username(self, username: str) -> User | None:
        return await self.session.scalar(
            select(User).where(User.username == username)
        )


    async def get_existing_for_registration(self, email: str, username: str) -> Sequence[User]:
        """
        Метод используется для оптимизации выполнения двух последовательных await к БД.
        """
        conditions = [User.email == email]
        if username:
            conditions.append(User.username == username)
            
        stmt = select(User).where(or_(*conditions))
        result = await self.session.scalars(stmt)
        return result.all()
