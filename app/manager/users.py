import uuid

from fastapi import Depends
from fastapi_users import UUIDIDMixin, BaseUserManager

from app.db.models.users import User, get_user_db


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    pass


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)



