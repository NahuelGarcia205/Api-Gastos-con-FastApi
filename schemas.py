from pydantic import BaseModel
from datetime import date

class GastoCreate():
    descripcion: str
    monto: float
    categoria: str
    
class GastoResponse(GastoCreate):
    id: int
    fecha: date
    
class Config:
    from_attributes = True