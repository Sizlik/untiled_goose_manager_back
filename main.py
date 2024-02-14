from fastapi import FastAPI
from app.route.users import router as users_router

app = FastAPI()

app.include_router(users_router)

