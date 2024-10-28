from pydantic import BaseModel, Field
from resources.domain.entities.estado_aula import EstadoAula
from typing import List

class Aula(BaseModel):
    id: int
    tipo: str # Tipo de aula (Normal, Magna, laboratorio)
    capacidad: int
    recursos: List[str]
    estado: EstadoAula = Field(default=EstadoAula.AVAILABLE)  # Estado del aula

    def is_available(self) -> bool:
        return self.estado == EstadoAula.AVAILABLE
    
    def marcar_reservada(self) -> bool:
        self.estado = EstadoAula.RESERVED
    
    def marcar_ocupada(self) -> bool:
        self.estado = EstadoAula.OCCUPIED
    
    def marcar_disponible(self) -> bool:
        self.estado = EstadoAula.AVAILABLE
    
    def marcar_mantenimiento(self) -> bool:
        self.estado = EstadoAula.MAINTENANCE

    def can_accommodate(self, numero_de_estudiantes: int) -> bool:
        return numero_de_estudiantes <= self.capacidad
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "tipo": self.tipo,
            "capacidad": self.capacidad,
            "recursos": self.recursos,
            "estado": self.estado.value,
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            tipo=data.get("tipo"),
            capacidad=data.get("capacidad"),
            recursos=data.get("recursos", []),
            estado=EstadoAula(data.get("estado", EstadoAula.AVAILABLE)),
        )
        