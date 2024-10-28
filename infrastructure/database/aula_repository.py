from resources.domain.entities.aula import Aula
from typing import List, Optional
from resources.infrastructure.database.mongo_db import db_recursos

class AulaRepository:
    def __init__(self):
        self.coleccion_aulas = db_recursos['aula']

    def obtener_todas_las_aulas(self) -> List[Aula]:
        aulas = self.coleccion_aulas.find() 
        return [Aula(**aula) for aula in aulas]
    
    def obtener_aula_por_id(self, aula_id: int) -> Optional[dict]:
        return self.coleccion_aulas.find_one({"id": aula_id})

    def actualizar_aula(self, aula: Aula):
        resultado = self.coleccion_aulas.update_one(
            {"id": aula.id},
            {"$set": aula.to_dict()}
        )
        if resultado.matched_count == 0:
            raise ValueError(f"No se encontró el aula con id {aula.id}")
        elif resultado.modified_count == 0:
            print(f"Aula con id {aula.id} ya estaba actualizada")
