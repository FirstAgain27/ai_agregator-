from repositories.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from core.security import hash_password, verify_password, create_access_token
from core.exceptions import UserAlreadyExistsError, InvalidCredentialsError
from schemas.user import UserCreate, UserResponse, UserLogin
from schemas.token import TokenResponse
from models.user import User


class AuthService:
    def __init__(self, session: AsyncSession, user_repo: UserRepository) -> None:
        self.user_repo = user_repo
        self.session = session

    async def register_new_user(self, user_data: UserCreate) -> UserResponse:
        # Пробуем получить объект по email
        existing = await self.user_repo.get_by_email(user_data.email)
        if existing:
            raise UserAlreadyExistsError("Пользователь с таким email уже существует!")

        hashed_pwd = hash_password(user_data.password)

        user = User(
            email=user_data.email,
            hashed_password=hashed_pwd
        )

        user = await self.user_repo.add(user)

        await self.session.commit()

        return UserResponse.model_validate(user)
    
    async def login(self, credentials: UserLogin):
        user = await self.user_repo.get_by_email(credentials.email)

        if not user or not verify_password(credentials.password, user.hashed_password):
            raise InvalidCredentialsError()

        access_token = create_access_token(data={"sub" : str(user.id)})

        return TokenResponse(
            access_token=access_token,
            token_type="bearer"
        )


    

        





        
        