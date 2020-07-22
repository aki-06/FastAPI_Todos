from fastapi import APIRouter

users_router = APIRouter()


@users_router.get('/')
async def get_all_users():
    return {'users': 'all'}