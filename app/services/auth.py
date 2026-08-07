from repositories.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from core.security import hash_password
from schemas.user import UserCreate, UserResponse
from models.user import User


class AuthService:
    def __init__(self, session: AsyncSession, user_repo: UserRepository) -> None:
        self.user_repo = user_repo
        self.session = session

    async def register_new_user(self, user_data: UserCreate) -> UserResponse:
        # Пробуем получить объект по email
        existing = await self.user_repo.get_by_email(user_data.email)
        if existing:
            raise UserAlreadyExistsError()

        hashed_pwd = hash_password(user_data.password)

        user = User(
            email=user_data.email,
            hashed_password=hashed_pwd
        )

        user = await self.user_repo.add(user)

        await self.session.commit()

        return UserResponse.model_validate(user)
    





        
        