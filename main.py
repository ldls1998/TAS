from fastapi import FastAPI
from resources.api import aula_api


resources = FastAPI()

resources.include_router(aula_api.router)

@resources.get("/")
def read_root():
    return {"La resources funciona!"}
