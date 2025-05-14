from fastapi import APIRouter
from .EndPoint import ImageEdit
api_router = APIRouter()

api_router.include_router(ImageEdit.router, prefix='/img-edit', tags=['Image Edit'])