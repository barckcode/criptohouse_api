from pydantic import BaseModel


class CurrenciesModel(BaseModel):
    id: str
    symbol: str
    name: str
