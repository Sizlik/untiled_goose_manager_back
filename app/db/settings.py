import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
import redis.asyncio
from fastapi_users.authentication import RedisStrategy

SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONNECTION_LINK", "postgresql+asyncpg://root:qwerty@postgres:5432/goose")

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

redis = redis.asyncio.from_url(os.getenv("REDIS_URL", "redis://redis_db:6379"), decode_responses=True)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=os.getenv("TOKEN_LIFE_TIME", 3600))


class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

