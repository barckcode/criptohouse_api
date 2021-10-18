from fastapi import APIRouter, Response
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


