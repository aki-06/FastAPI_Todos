from fastapi import FastAPI

from config import config
from routers.todos import todos_router
from routers.users import users_router


app = FastAPI()

# TODO: 環境変数化する
_COMMON_API_PREFIX = '/api/v1'

app.include_router(
    todos_router,
    prefix=f'{_COMMON_API_PREFIX}/todos',
    tags=['todos']
)

app.include_router(
    users_router,
    prefix=f'{_COMMON_API_PREFIX}/users',
    tags=['users']
)


@app.on_event('startup')
async def app_startup():
    config.load_config()


@app.on_event('shutdown')
async def app_shutdown():
    config.close_db_client()


@app.get('/')
async def get_hello():
    return {'text': 'hello'}
