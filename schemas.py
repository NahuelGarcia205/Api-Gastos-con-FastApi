from pydantic import BaseModel
from datetime import date
from typing import Optional


class GastoCreate(BaseModel):
    descripcion: str
    monto: float
    categoria: str


class GastoCreate(GastoCreate):
    pass


class GastoResponse(GastoCreate):
    id: int
    fecha: date

    class Config:
        from_attributes = True
        
class GastoUpdate(BaseModel):
    descripcion: Optional[str]= None
    monto: Optional[float]= None
    categoria: Optional[str]= None