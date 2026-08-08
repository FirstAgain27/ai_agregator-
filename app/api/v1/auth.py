from fastapi import APIRouter, Depends, status
from schemas.user import UserCreate, UserResponse
from services.auth import AuthService
from api.dependencies import get_auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post(
        "/register", 
        response_model=UserResponse, 
        status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    user_service: AuthService = Depends(get_auth_service) 
    ):
    return await user_service.register_new_user(user_data)

@router.post("/login")
async def login():
    pass