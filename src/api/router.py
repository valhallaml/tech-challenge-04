from fastapi import APIRouter
from src.api.v1.finance import router

api_router = APIRouter()
api_router.include_router(router, prefix='/finance', tags=[ 'finance' ])
