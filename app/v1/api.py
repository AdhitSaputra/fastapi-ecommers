from fastapi import APIRouter

from . import user

api_router = APIRouter(user.router, prefix="/user", tags=["user"])
