from fastapi import FastAPI

# Internal Modules
from routes.currencies_routes import currencies_endpoint
from routes.criptos_routes import criptos_endpoint
from routes.users_routes import users_endpoint
from routes.users_preferences_criptos_routes import users_preferences_cripto_endpoint


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
        {
            "name": "Users",
            "description": "Enpoint de Users"
        },
        {
            "name": "Preferences",
            "description": "Enpoint de Preferences"
        },
    ]
)


# Include Routes to FastAPI
app.include_router(currencies_endpoint)
app.include_router(criptos_endpoint)
app.include_router(users_endpoint)
app.include_router(users_preferences_cripto_endpoint)
