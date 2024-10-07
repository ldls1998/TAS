from pydantic import BaseModel

class EstadoAula(BaseModel):
    nuevo_estado: str
    