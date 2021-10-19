from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.exc import ProgrammingError

# Internal Modules
from config.db import db_connection
from models.users_model import users_table
from models.users_preferences_currencies_model import preferences_currencies_table
from schemas.users_preferences_currencies_schema import PreferencesCurrenciesModel


# Init Route
users_preferences_currencies_endpoint = APIRouter()


#Routes
"""
Get Favorite Currency per user
"""
@users_preferences_currencies_endpoint.get("/users/{id_user}/preferences/currency/{id_currency}", tags=["User Preferences: Currencies"])
async def get_currency_preference_per_user(id_user: int, id_currency: str):
    try:
        return db_connection.execute(preferences_currencies_table.select().where(
            preferences_currencies_table.c.id_user == id_user, preferences_currencies_table.c.id_currency == id_currency
        )).first()
    except ProgrammingError:
        return {
            "ERROR": f"User: {id_user} does not exist or Currency: {id_currency} does not exist."
        }


@users_preferences_currencies_endpoint.post("/users/{id_user}/preferences/currency", tags=["User Preferences: Currencies"])
async def new_currency_preference_per_user(id_user: int, preference: PreferencesCurrenciesModel):
    validation = db_connection.execute(users_table.select().where(users_table.c.id == id_user)).first()

    if validation == None:
        return {
            "ERROR": f"User: {id_user} does not exist."
        }
    else:
        new_preference = {
            "id": preference.id,
            "id_user": preference.id_user,
            "id_currency": preference.id_currency
        }

        db_connection.execute(preferences_currencies_table.insert().values(new_preference))
        return db_connection.execute(preferences_currencies_table.select().where(
            preferences_currencies_table.c.id_user == id_user, preferences_currencies_table.c.id_currency == preference.id_currency
        )).first()


@users_preferences_currencies_endpoint.delete("/users/{id_user}/preferences/currency/{id_currency}", status_code=HTTP_204_NO_CONTENT, tags=["User Preferences: Currencies"])
async def delete_currency_preference_by_id(id_user: int, id_currency: str):
    db_connection.execute(users_table.delete().where(
        preferences_currencies_table.c.id_user == id_user, preferences_currencies_table.c.id_currency == id_currency
    ))
    return Response(status_code=HTTP_204_NO_CONTENT)


@users_preferences_currencies_endpoint.put("/users/{id_user}/preferences/currency/{id_currency}", status_code=HTTP_204_NO_CONTENT, tags=["User Preferences: Currencies"])
async def update_currency_preference_by_id(id_user: int, id_currency: str, preference: PreferencesCurrenciesModel):
    db_connection.execute(preferences_currencies_table.update().values(
        id_user = preference.id_user,
        id_currency = preference.id_currency,
    ).where(
        preferences_currencies_table.c.id_user == id_user, preferences_currencies_table.c.id_currency == id_currency
    ))

    return db_connection.execute(preferences_currencies_table.select().where(
        preferences_currencies_table.c.id_user == id_user, preferences_currencies_table.c.id_currency == id_currency
    )).first()
