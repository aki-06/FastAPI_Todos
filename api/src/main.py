from fastapi import FastAPI

from routers.todos import todos_router
from routers.users import users_router

app = FastAPI()

app.include_router(
    todos_router,
    prefix='/todos',
    tags=['todos']
)

app.include_router(
    users_router,
    prefix='/users',
    tags=['users']
)

@app.get('/')
async def get_hello():
    return {'text': 'hello'}