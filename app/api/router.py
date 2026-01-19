from fastapi import APIRouter
from app.api.routes import report1, transaction1, user1

api_router = APIRouter()
api_router.include_router(user1.router)
api_router.include_router(transaction1.router)
api_router.include_router(report1.router)