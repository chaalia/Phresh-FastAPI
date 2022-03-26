from sys import prefix
from fastapi import APIRouter
from app.api.routes.cleanings import router as cleanings_roiuter

router = APIRouter()

router.include_router(cleanings_roiuter, prefix="/cleanings", tags=["cleanings"])
