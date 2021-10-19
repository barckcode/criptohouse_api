from fastapi import APIRouter, Response
from sqlalchemy.sql.expression import null
from starlette.status import HTTP_204_NO_CONTENT

# Internal Modules
from config.db import db_connection
from models.users_model import users_table
from schemas.users_schema import UsersModel


# Init Route
users_endpoint = APIRouter()


# Routes
@users_endpoint.get("/users", tags=["Users"])
async def get_all_users():
    return db_connection.execute(users_table.select()).fetchall()


@users_endpoint.get("/users/{id}", response_model=UsersModel, tags=["Users"])
async def get_user_by_id(id: str):
    return db_connection.execute(users_table.select().where(users_table.c.id == id)).first()


@users_endpoint.post("/users", response_model=UsersModel, tags=["Users"])
async def add_new_user(user: UsersModel):
    new_user = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "nickname": user.nickname
    }

    validation = db_connection.execute(users_table.select().where(users_table.c.id == user.id)).first()

    if validation == None:
        db_connection.execute(users_table.insert().values(new_user))
        return db_connection.execute(users_table.select().where(users_table.c.id == user.id)).first()
    else:
        return db_connection.execute(users_table.select().where(users_table.c.id == user.id)).first()


@users_endpoint.delete("/users/{id}", status_code=HTTP_204_NO_CONTENT, tags=["Users"])
async def delete_user_by_id(id: str):
    db_connection.execute(users_table.delete().where(users_table.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@users_endpoint.put("/users/{id}", response_model=UsersModel, tags=["Users"])
async def update_user_by_id(id: str, user: UsersModel):
    db_connection.execute(users_table.update().values(
        id = user.id,
        first_name = user.first_name,
        last_name = user.last_name,
        nickname = user.nickname
    ).where(users_table.c.id == id))

    return db_connection.execute(users_table.select().where(users_table.c.id == user.id)).first()
