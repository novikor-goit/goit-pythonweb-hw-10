from fastapi import APIRouter, Depends, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from src.api.schemas import UserResponse
from src.database.models import User
from src.services.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])
limiter = Limiter(key_func=get_remote_address)


@router.get(
    "/me",
    response_model=UserResponse,
    description="No more than 24 requests per minute",
)
@limiter.limit("24/minute")
async def me(request: Request, user: User = Depends(get_current_user)):
    return user
