from pydantic import BaseModel


class UsersModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    nickname: str
