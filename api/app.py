from fastapi import FastAPI

# Internal Modules
from routes.currencies_routes import currencies_endpoint
from routes.criptos_routes import criptos_endpoint


# Init FastAPI
app = FastAPI(
    title = "CriptoHouse API",
    description = "Enpoints para gestionar toda la información de la aplicación CriptoHouse",
    version = "0.1",
    contact = {
        "name": "Helmcode",
        "url": "https://helmcode.com/contact",
    },
    openapi_tags = [
        {
            "name": "Currencies",
            "description": "Enpoint de Currencies"
        },
        {
            "name": "Criptos",
            "description": "Enpoint de Criptos"
        },
    ]
)


# Include Routes to FastAPI
app.include_router(currencies_endpoint)
app.include_router(criptos_endpoint)