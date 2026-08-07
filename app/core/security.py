from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
import jwt
from app.config import settings

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    # 1. Копируем словарь с полезными данными (Payload)
    to_encode = data.copy()

    # 2. Высчитываем время тухлости токена (exp)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})

    # 3. PyJWT берет Header, берет Payload (to_encode), подписывает SECRET_KEY
    #    и возвращает готовую строку Header.Payload.Signature
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    
    return encoded_jwt 
