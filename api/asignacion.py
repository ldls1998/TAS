from fastapi import APIRouter, HTTPException
from app.application.use_cases.asignar_aula import AsignarAula
from app.domain.entities.curso import Curso
from app.infrastructure.database.aula_repository import AulaRepository

router = APIRouter()

aula_repository = AulaRepository()

@router.post("/asignar_aula")
def asignar_aula(curso: Curso):
    try:
        aulas_disponibles = aula_repository.obtener_todas_las_aulas()
        asignacion_service = AsignarAula(aulas=aulas_disponibles)
        aula_asignada = asignacion_service.ejecutar(curso)
        return {"mensaje": "Aula asignada exitosamente", "aula": aula_asignada.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))