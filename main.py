from fastapi import FastAPI
from app.api import asignacion

app = FastAPI()

app.include_router(asignacion.router)

@app.get("/")
def read_root():
    return {"La app funciona!"}