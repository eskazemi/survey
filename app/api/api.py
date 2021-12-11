from fastapi import APIRouter
from app.api.routers import poll, container
api_router = APIRouter()
api_router.include_router(poll.router, prefix="/survey/poll", tags=["poll"])
api_router.include_router(container.router, prefix="/survey", tags=["container"])




