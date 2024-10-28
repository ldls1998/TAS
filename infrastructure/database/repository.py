from resources.domain.entities.aula import Aula

class AulaRepository:
    def __init__(self):
        # Para fines de ejemplo, usamos una lista simulando la base de datos
        self.aulas = [
            Aula(id=1, capacidad=30, recursos=["proyector"]),
            Aula(id=2, capacidad=20, recursos=["computadoras"])
        ]

    def obtener_aulas_disponibles(self):
        # Filtrar y devolver aulas que están disponibles
        return [aula for aula in self.aulas if aula.is_available()]

    def actualizar_aula(self, aula: Aula):
        # Actualizar la disponibilidad del aula (aquí sería una operación real en la base de datos)
        for a in self.aulas:
            if a.id == aula.id:
                a.disponible = aula.disponible