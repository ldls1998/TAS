from pydantic import BaseModel
from typing import List, Optional

class Aula(BaseModel):
    id: int
    tipo: str # Tipo de aula (Normal, Magna, laboratorio)
    capacidad: int
    recursos: List[str]
    estado: str = "available" # Estado del aula (disponible, en mantenimiento, ocupada, reservada)

    def is_available(self) -> bool:
        return self.estado == "available"
    
    def marcar_reservada(self) -> bool:
        return self.estado == "reserved"
    
    def marcar_ocupada(self) -> bool:
        return self.estado == "occupied"
    
    def marcar_disponible(self) -> bool:
        return self.estado == "available"
    
    def marcar_mantenimiento(self) -> bool:
        return self.estado == "maintenance"

    def can_accommodate(self, numero_de_estudiantes: int) -> bool:
        return numero_de_estudiantes <= self.capacidad