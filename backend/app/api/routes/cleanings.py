from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_cleanings() -> List[dict]:
    cleanings = [
        {"id": 1, "name": "My house", "cleaning_type": "ful_clean", "price_per_hour": 25},
        {"id": 2, "name": "My City", "cleaning_type": "Not lean", "price_per_hour": 56.23},
    ]