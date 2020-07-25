from pydantic import BaseModel, SecretStr
from pydantic.types import EmailStr, Any


class TodoResponse(BaseModel):
    # _id: Any
    # todoName: str
    # description: str
    # isDone: bool = False
    # createUserId: Any
    # createdAt: str = None
    # updaredAt: str = None
    pass


class CreateTodoRequest(BaseModel):
    # _id: Any
    # todoName: str
    # description: str
    # isDone: bool = False
    # createUserId: Any
    # createdAt: str
    # updaredAt: str
    pass
