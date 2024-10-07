from fastapi import APIRouter, HTTPException
from app.application.use_cases.listar_aulas import ListarAulasDisponibles
from app.domain.entities.estado_aula import EstadoAula
from app.infrastructure.database.aula_repository import AulaRepository

router = APIRouter()

aula_repository = AulaRepository()

@router.get("/aulas")
def obtener_aulas():
    listar_aulas_disponibles = ListarAulasDisponibles(aulas=aula_repository.obtener_todas_las_aulas())
    aulas_disponibles = listar_aulas_disponibles.ejecutar()
    return aulas_disponibles

@router.put("/aulas/{aula_id}/estado")
def actualizar_estado_aula(aula_id: int, estado: EstadoAula):
    aulas = aula_repository.obtener_todas_las_aulas()
    for aula in aulas:
        if aula.id == aula_id:
            if estado.nuevo_estado == "available":
                aula.marcar_disponible()
            elif estado.nuevo_estado == "reserved":
                aula.marcar_reservada()
            elif estado.nuevo_estado == "occupied":
                aula.marcar_ocupada()
            elif estado.nuevo_estado == "maintenance":
                aula.marcar_mantenimiento()
            else:
                raise HTTPException(status_code=400, detail="Estado no válido")
            aula_repository.actualizar_aula(aula)
            return {"mensaje": f"Estado del aula {aula_id} actualizado a {estado.nuevo_estado}"}
    raise HTTPException(status_code=404, detail="Aula no encontrada")
