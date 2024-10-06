from app.domain.entities.aula import Aula
from app.domain.entities.curso import Curso
from typing import List

class AsignacionDeAulasService:
    def asignar_aula(self, curso: Curso, lista_aulas: List[Aula]) -> Aula:
        numero_de_estudiantes = curso.numero_de_estudiantes()
        for aula in lista_aulas:
            if aula.can_accommodate(numero_de_estudiantes) and aula.is_available():
                return aula
        raise Exception("No hay aulas disponibles para este curso")