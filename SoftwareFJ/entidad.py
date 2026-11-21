"""
entidad.py
Clase abstracta que representa entidades generales del sistema (requerido).
"""

from abc import ABC, abstractmethod

class Entidad(ABC):
    """Clase abstracta base."""

    def __init__(self, id_entidad: str):
        if not id_entidad or not id_entidad.strip():
            raise ValueError("El ID no puede estar vacío")
        self._id = id_entidad.strip()

    @property
    def id(self):
        return self._id

    @abstractmethod
    def obtener_info(self) -> str:
        pass

    def __str__(self):
        return self.obtener_info()
