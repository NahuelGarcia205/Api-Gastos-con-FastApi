from pydantic import BaseModel
from datetime import date


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