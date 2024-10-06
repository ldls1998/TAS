from fastapi import APIRouter, HTTPException
from app.application.use_cases.asignar_aula import AsignarAula
from app.domain.entities.curso import Curso
from app.domain.entities.aula import Aula

router = APIRouter()

# Aulas en crudo, falta implementar conexión
aulas_disponibles = [
    Aula(id=1, capacidad=30, recursos=["proyector"]),
    Aula(id=2, capacidad=20, recursos=["computadoras"]),
]

@router.post("/asignar_aula")
def asignar_aula(curso: Curso):
    try:
        asignacion_service = AsignarAula(aulas=aulas_disponibles)
        aula_asignada = asignacion_service.ejecutar(curso)
        return {"mensaje": "Aula asignada exitosamente", "aula": aula_asignada.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))