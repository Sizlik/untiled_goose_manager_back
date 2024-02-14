import os

from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from app.db.settings import get_redis_strategy

SECRET = os.getenv("SECRET", "Pa$$w0rd")

bearer_transport = BearerTransport(tokenUrl="/users/auth/jwt/login")


auth_backend = AuthenticationBackend(
    name="redis",
    transport=bearer_transport,
    get_strategy=get_redis_strategy,
)

