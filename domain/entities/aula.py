from pydantic import BaseModel
from typing import List, Optional

class Aula(BaseModel):
    id: int
    capacidad: int
    recursos: List[str]  # Lista de recursos disponibles en el aula
    disponible: bool = True

    def is_available(self) -> bool:
        return self.disponible

    def can_accommodate(self, numero_de_estudiantes: int) -> bool:
        return numero_de_estudiantes <= self.capacidad