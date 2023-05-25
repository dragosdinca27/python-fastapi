from fastapi import APIRouter

from apis.version1 import route_user
from apis.version1 import route_job

api_router = APIRouter()

api_router.include_router(route_user.router,prefix="/users",tags=["users"])
api_router.include_router(route_job.router,prefix="/job",tags=["jobs"])