from fastapi import APIRouter, HTTPException
from resources.application.use_cases.listar_aulas import ListarAulasDisponibles
from resources.application.use_cases.actualizar_aulas import ActualizarEstadoAula
from resources.infrastructure.database.aula_repository import AulaRepository
from resources.infrastructure.messaging.rabbitmq import RabbitMQClient
from resources.api.schemas.estado_update_request import EstadoUpdateRequest

router = APIRouter()

aula_repository = AulaRepository()
actualizar_estado_aula = ActualizarEstadoAula(aula_repository)
rabbitmq_client = RabbitMQClient(queue_name='estado_aulas')

@router.get("/aulas")
def obtener_aulas():
    listar_aulas_disponibles = ListarAulasDisponibles(aulas=aula_repository.obtener_todas_las_aulas())
    aulas_disponibles = listar_aulas_disponibles.ejecutar()
    return aulas_disponibles

@router.put("/aulas/{aula_id}/estado")
def actualizar_estado(aula_id: int, request: EstadoUpdateRequest):

    try:
        aula_actualizada = actualizar_estado_aula.ejecutar(aula_id, request.estado)
        
        mensaje = {
            "aula_id": aula_id,
            "nuevo_estado": request.estado.value
        }
        rabbitmq_client.publish(mensaje)
        print(aula_actualizada)
        return {"mensaje": f"Estado del aula {aula_id} actualizado a {request.estado.value}"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))