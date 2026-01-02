from pydantic import BaseModel
from datetime import date


class GastoBase(BaseModel):
    descripcion: str
    monto: float
    categoria: str


class GastoCreate(GastoBase):
    pass


class GastoResponse(GastoBase):
    id: int
    fecha: date

    class Config:
        from_attributes = True