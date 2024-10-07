from pydantic import BaseModel
from typing import List, Optional

class Curso(BaseModel):
    id: str
    nombre: str
    estudiantes: List[str]
    profesor: str
    requisitos_tecnicos: Optional[List[str]] = []

    def numero_de_estudiantes(self) -> int:
        return len(self.estudiantes)

    def tiene_requisitos_tecnicos(self) -> bool:
        return len(self.requisitos_tecnicos) > 0