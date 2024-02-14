import uuid

from fastapi import FastAPI, APIRouter
from fastapi_users import FastAPIUsers

from app.db.models.users import User
from app.db.schemas.users import UserRead, UserCreate, UserUpdate
from app.manager.users import get_user_manager
from app.utils.authorization import auth_backend

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

router = APIRouter(tags=["users"], prefix="/users")

router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt")
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


