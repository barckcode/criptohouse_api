from typing import Optional
from pydantic import BaseModel


class PreferencesModel(BaseModel):
    id: Optional[int]
    id_user: int
    id_cripto: str
    id_currency: str
