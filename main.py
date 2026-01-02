from fastapi import FastAPI, Depends, HTTPException, status, Query, Request
from sqlalchemy.orm import Session
from models import Gasto
from database import get_db, engine, SessionLocal

app = FastAPI()

@app.get("/")
def root():
    return{"message: backend activo"}
