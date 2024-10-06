from app.domain.services.asignacion_service import AsignacionDeAulasService
from app.domain.entities.curso import Curso
from app.domain.entities.aula import Aula
from typing import List

class AsignarAula:
    def __init__(self, aulas: List[Aula]):
        self.aulas = aulas
        self.asignacion_service = AsignacionDeAulasService()

    def ejecutar(self, curso: Curso) -> Aula:
        # Asignación del aula utilizando el servicio de dominio
        aula_asignada = self.asignacion_service.asignar_aula(curso, self.aulas)
        # Actualizar el estado del aula asignada
        aula_asignada.disponible = False
        return aula_asignada