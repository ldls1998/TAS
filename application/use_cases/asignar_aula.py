from app.domain.services.asignacion_service import AsignacionDeAulasService
from app.domain.entities.curso import Curso
from app.domain.entities.aula import Aula
from typing import List

class AsignarAula:
    def __init__(self, aulas: List[Aula]):
        self.aulas = aulas
        self.asignacion_service = AsignacionDeAulasService()

    def ejecutar(self, curso: Curso) -> Aula:
        for aula in self.aulas:
            if aula.is_available() and aula.can_accommodate(curso.numero_de_estudiantes()):
                return aula
        raise Exception("No hay aulas disponibles que cumplan los requisitos")