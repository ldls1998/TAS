from pydantic import BaseModel
from resources.domain.entities.estado_aula import EstadoAula

class EstadoUpdateRequest(BaseModel):
    estado: EstadoAula
