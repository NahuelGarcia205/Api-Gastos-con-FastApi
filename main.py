from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return print("message: backend activo")
