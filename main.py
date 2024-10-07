from fastapi import FastAPI
from app.api import asignacion
from app.api import aulas

app = FastAPI()

app.include_router(asignacion.router)
app.include_router(aulas.router)

@app.get("/")
def read_root():
    return {"La app funciona!"}