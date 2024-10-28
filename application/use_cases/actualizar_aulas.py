from resources.domain.entities.aula import Aula
from resources.domain.entities.estado_aula import EstadoAula
from resources.infrastructure.database.aula_repository import AulaRepository

class ActualizarEstadoAula:
    def __init__(self, aula_repository: AulaRepository):
        self.aula_repository = aula_repository

    def ejecutar(self, aula_id: int, nuevo_estado: EstadoAula):
        aula_data = self.aula_repository.obtener_aula_por_id(aula_id)
        if not aula_data:
            raise ValueError("Aula no encontrada")

        aula = Aula.from_dict(aula_data)

        if nuevo_estado == EstadoAula.AVAILABLE:
            aula.marcar_disponible()
        elif nuevo_estado == EstadoAula.RESERVED:
            aula.marcar_reservada()
        elif nuevo_estado == EstadoAula.OCCUPIED:
            aula.marcar_ocupada()
        elif nuevo_estado == EstadoAula.MAINTENANCE:
            aula.marcar_mantenimiento()
        else:
            raise ValueError("Estado no válido")

        self.aula_repository.actualizar_aula(aula)
        return aula
