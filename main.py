from fastapi import FastAPI, Depends, HTTPException, status, Query, Request
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db, engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return{"message": "backend activo"}

@app.post("/gastos",response_model=schemas.GastoResponse)
def crear_gasto(gasto:schemas.GastoCreate,db: Session = Depends(get_db)):
    try:
        nuevo_gasto=models.Gasto(
        descripcion=gasto.descripcion,
        monto=gasto.monto,
        categoria=gasto.categoria
        )

        db.add(nuevo_gasto)
        db.commit()
        db.refresh(nuevo_gasto)
    
        return nuevo_gasto
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"Error al crear el gasto: {str(e)}")
    
