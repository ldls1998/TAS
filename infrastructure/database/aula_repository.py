from app.domain.entities.aula import Aula
from typing import List

# Simulación de aulas en crudo, falta implementar la base de datos
class AulaRepository:
    def __init__(self):
        self.aulas = [
            Aula(id=1, tipo="Normal", capacidad=50, recursos=["proyector"], estado="available"),
            Aula(id=2, tipo="Laboratorio", capacidad=30, recursos=["computadoras"], estado="available"),
            Aula(id=3, tipo="Magna", capacidad=80, recursos=["proyector"], estado="available"),
        ]

    def obtener_todas_las_aulas(self) -> List[Aula]:
        return self.aulas

    def actualizar_aula(self, aula: Aula):
        for idx, a in enumerate(self.aulas):
            if a.id == aula.id:
                self.aulas[idx] = aula