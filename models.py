from sqlalchemy import Column, Integer, String, Float, Date
from datetime import date
from database import Base

class Gasto(Base):
    __tablename__ = "gastos"
    id=Column(Integer, primary_key=True, autoincrement=True)
    descripcion=Column(String, nullable=False)
    monto=Column(Float, nullable=False)
    categoria=Column(String, nullable=False)
    fecha=Column(Date, default=date.today)
    
    
