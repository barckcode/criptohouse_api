from pydantic import BaseModel


class CriptosModel(BaseModel):
    id: str
    symbol: str
    name: str
