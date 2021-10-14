from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

# Internal Modules
from config.db import db_connection
from models.criptos_model import criptos_table
from schemas.criptos_schema import CriptosModel


# Init Route
criptos_endpoint = APIRouter()


# Routes
@criptos_endpoint.get("/criptos", tags=["Criptos"])
async def get_all_criptos():
    return db_connection.execute(criptos_table.select()).fetchall()


@criptos_endpoint.get("/criptos/{id}", response_model=CriptosModel, tags=["Criptos"])
async def get_cripto_by_id(id: str):
    return db_connection.execute(criptos_table.select().where(criptos_table.c.id == id)).first()


@criptos_endpoint.post("/criptos", response_model=CriptosModel, tags=["Criptos"])
async def add_new_cripto(cripto: CriptosModel):
    new_cripto = {
        "id": cripto.id,
        "symbol": cripto.symbol,
        "name": cripto.name
    }

    db_connection.execute(criptos_table.insert().values(new_cripto))
    return db_connection.execute(criptos_table.select().where(criptos_table.c.id == cripto.id)).first()


@criptos_endpoint.delete("/criptos/{id}", status_code=HTTP_204_NO_CONTENT, tags=["Criptos"])
async def delete_cripto_by_id(id: str):
    db_connection.execute(criptos_table.delete().where(criptos_table.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@criptos_endpoint.put("/criptos/{id}", response_model=CriptosModel, tags=["Criptos"])
async def update_cripto_by_id(id: str, cripto: CriptosModel):
    db_connection.execute(criptos_table.update().values(
        id = cripto.id,
        symbol = cripto.symbol,
        name = cripto.name
    ).where(criptos_table.c.id == id))

    return db_connection.execute(criptos_table.select().where(criptos_table.c.id == cripto.id)).first()
