from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

# Internal Modules
from config.db import db_connection
from models.currencies_model import currencies_table
from schemas.currencies_schema import CurrenciesModel


# Init Route
currencies_endpoint = APIRouter()


# Routes
@currencies_endpoint.get("/currencies", tags=["Currencies"])
async def get_all_currencies():
    return db_connection.execute(currencies_table.select()).fetchall()


@currencies_endpoint.get("/currencies/{id}", response_model=CurrenciesModel, tags=["Currencies"])
async def get_currency_by_id(id: str):
    return db_connection.execute(currencies_table.select().where(currencies_table.c.id == id)).first()


@currencies_endpoint.post("/currencies", response_model=CurrenciesModel, tags=["Currencies"])
async def add_new_currency(currency: CurrenciesModel):
    new_currency = {
        "id": currency.id,
        "symbol": currency.symbol,
        "name": currency.name
    }

    db_connection.execute(currencies_table.insert().values(new_currency))
    return db_connection.execute(currencies_table.select().where(currencies_table.c.id == currency.id)).first()


@currencies_endpoint.delete("/currencies/{id}", status_code=HTTP_204_NO_CONTENT, tags=["Currencies"])
async def delete_currency_by_id(id: str):
    db_connection.execute(currencies_table.delete().where(currencies_table.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@currencies_endpoint.put("/currencies/{id}", response_model=CurrenciesModel, tags=["Currencies"])
async def update_currency_by_id(id: str, currency: CurrenciesModel):
    db_connection.execute(currencies_table.update().values(
        id = currency.id,
        symbol = currency.symbol,
        name = currency.name
    ).where(currencies_table.c.id == id))

    return db_connection.execute(currencies_table.select().where(currencies_table.c.id == currency.id)).first()
