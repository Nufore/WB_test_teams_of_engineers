from fastapi import APIRouter

from .engineers.views import router as engineers_router
from .teams.views import router as teams_router

router = APIRouter()
router.include_router(router=engineers_router, prefix="/engineers")
router.include_router(router=teams_router, prefix="/teams")
