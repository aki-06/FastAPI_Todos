from fastapi import APIRouter

todos_router = APIRouter()

@todos_router.get('/')
async def get_all_todos():
    return {"todo": "test"}