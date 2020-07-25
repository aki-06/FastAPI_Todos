from fastapi import APIRouter

from cruds.todos import TodoCrud
from models.todo import TodoResponse

todos_router = APIRouter()


@todos_router.get("/")
async def get_all_todos():
    """
    todo一覧取得
    """
    todo_crud = TodoCrud()
    response = todo_crud.get_all_todos()
    return response


@todos_router.post("/")
async def create_todo():
    """
    todoを登録
    """
    pass


@todos_router.put("/{user_id}/{todo_id}")
async def update_todo():
    """
    todoを編集
    """
    pass


@todos_router.get("/{user_id}/{todo_id}")
async def get_detail_todo():
    """
    todo詳細取得
    """
    pass


@todos_router.delete("/{user_id}/{todo_id}")
async def delete_todo():
    """
    todoを削除
    """
    pass
