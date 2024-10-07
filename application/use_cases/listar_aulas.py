from typing import List
from app.domain.entities.aula import Aula

class ListarAulasDisponibles:
    def __init__(self, aulas: List[Aula]):
        self.aulas = aulas

    def ejecutar(self) -> List[Aula]:
        return [aula for aula in self.aulas if aula.is_available()]