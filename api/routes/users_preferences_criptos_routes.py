from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.exc import ProgrammingError

# Internal Modules
from config.db import db_connection
from models.users_model import users_table
from models.users_preferences_criptos_model import preferences_criptos_table
from schemas.users_preferences_criptos_schema import PreferencesCriptosModel


# Init Route
users_preferences_cripto_endpoint = APIRouter()


# Routes
"""
Get All Preferences per user
"""
@users_preferences_cripto_endpoint.get("/users/{id_user}/preferences", tags=["User Preferences: Criptos"])
async def get_all_preferences_per_user(id_user: int):
    try:
        return db_connection.execute(preferences_criptos_table.select().where(preferences_criptos_table.c.id_user == id_user)).fetchall()
    except ProgrammingError:
        return {
            "ERROR": f"User: {id_user} does not exist."
        }


"""
Get Favorite Cripto by user
"""
@users_preferences_cripto_endpoint.get("/users/{id_user}/preferences/cripto/{id_cripto}", tags=["User Preferences: Criptos"])
async def get_cripto_preference_per_user(id_user: int, id_cripto: str):
    try:
        return db_connection.execute(preferences_criptos_table.select().where(
            preferences_criptos_table.c.id_user == id_user, preferences_criptos_table.c.id_cripto == id_cripto
        )).first()
    except ProgrammingError:
        return {
            "ERROR": f"User: {id_user} does not exist or Cripto: {id_cripto} does not exist."
        }


@users_preferences_cripto_endpoint.post("/users/{id_user}/preferences/cripto", tags=["User Preferences: Criptos"])
async def new_cripto_preference_per_user(id_user: int, preference: PreferencesCriptosModel):
    validation = db_connection.execute(users_table.select().where(users_table.c.id == id_user)).first()

    if validation == None:
        return {
            "ERROR": f"User: {id_user} does not exist."
        }
    else:
        new_preference = {
            "id": preference.id,
            "id_user": preference.id_user,
            "id_cripto": preference.id_cripto,
            "id_currency": preference.id_currency
        }

        db_connection.execute(preferences_criptos_table.insert().values(new_preference))
        return db_connection.execute(preferences_criptos_table.select().where(
            preferences_criptos_table.c.id_user == id_user, preferences_criptos_table.c.id_cripto == preference.id_cripto
        )).first()


@users_preferences_cripto_endpoint.delete("/users/{id_user}/preferences/cripto/{id_cripto}", status_code=HTTP_204_NO_CONTENT, tags=["User Preferences: Criptos"])
async def delete_cripto_preference_by_id(id_user: int, id_cripto: str):
    db_connection.execute(users_table.delete().where(
        preferences_criptos_table.c.id_user == id_user, preferences_criptos_table.c.id_cripto == id_cripto
    ))
    return Response(status_code=HTTP_204_NO_CONTENT)


@users_preferences_cripto_endpoint.put("/users/{id_user}/preferences/cripto/{id_cripto}", status_code=HTTP_204_NO_CONTENT, tags=["User Preferences: Criptos"])
async def update_cripto_preference_by_id(id_user: int, id_cripto: str, preference: PreferencesCriptosModel):
    db_connection.execute(preferences_criptos_table.update().values(
        id_user = preference.id_user,
        id_cripto = preference.id_cripto,
        id_currency = preference.id_currency
    ).where(
        preferences_criptos_table.c.id_user == id_user, preferences_criptos_table.c.id_cripto == id_cripto
    ))

    return db_connection.execute(preferences_criptos_table.select().where(
        preferences_criptos_table.c.id_user == id_user, preferences_criptos_table.c.id_cripto == id_cripto
    )).first()
