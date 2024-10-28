from pydantic import BaseModel
from enum import Enum

class EstadoAula(str, Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    OCCUPIED = "occupied"
    MAINTENANCE = "maintenance"