from fastapi import APIRouter


# Init Route
currencies_endpoint = APIRouter()


# Routes
@currencies_endpoint.get("/currencies", tags=["Currencies"])
async def get_all_currencies():
    return {
        "hello world"
    }
