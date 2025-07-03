# backend/app/api/v1/api.py
from fastapi import APIRouter
from app.api.v1.endpoints import users, members

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(members.router, prefix="/members", tags=["members"])