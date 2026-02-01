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
    
@app.get("/gastos")
def listar_gastos(db: Session = Depends(get_db)):
    try:
        gastos = db.query(models.Gasto).order_by(models.Gasto.fecha).all()
        
        if not gastos:
            return{"mensaje": "No hay gastos cargados"}
        
        gastos_agrupados={}
        
        for gasto in gastos:
            fecha = gasto.fecha.isoformat()
            
            if fecha not in gastos_agrupados:
                gastos_agrupados[fecha] = {
                    "fecha":fecha,
                    "gastos": [],
                    "total":0
                }
            
            gastos_agrupados[fecha]["gastos"].append({
                "id":gasto.id,
                "descripcion":gasto.descripcion,
                "categoria":gasto.categoria,
                "monto":gasto.monto
            })
            
            gastos_agrupados[fecha]["total"]+=gasto.monto
            
        resultado = list(gastos_agrupados.values())
        return resultado
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"Error al mostrar Gastos: {str(e)}")


@app.delete("/gastos/{gasto_id}",status_code=204)
def eliminar_gasto(gasto_id: int, db: Session=Depends(get_db)):
            
    gasto=db.query(models.Gasto).filter(models.Gasto.id == gasto_id).first()
        
    if not gasto:
        raise HTTPException(status_code=404, detail="el gasto no se encuentra")
        
    db.delete(gasto)
    db.commit()

        
    
        