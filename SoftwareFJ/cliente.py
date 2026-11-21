"""
cliente.py
Clase Cliente con validaciones robustas y encapsulación (requerido).
"""

import re
from entidad import Entidad
from exceptions import ClienteInvalidoError

class Cliente(Entidad):
    def __init__(self, id_cliente: str, nombre: str, email: str, telefono: str):
        super().__init__(id_cliente)
        self._validar(nombre, email, telefono)
        self._nombre = nombre.strip()
        self._email = email.strip().lower()
        self._telefono = telefono.strip()

    def _validar(self, nombre, email, telefono):
        if not nombre or len(nombre.strip()) < 3:
            raise ClienteInvalidoError("El nombre debe tener al menos 3 caracteres")
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email.strip()):
            raise ClienteInvalidoError("Email inválido")
        if not telefono or not telefono.strip().isdigit() or len(telefono.strip()) < 7:
            raise ClienteInvalidoError("Teléfono inválido")

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @property
    def telefono(self):
        return self._telefono

    def obtener_info(self) -> str:
        return f"Cliente[{self.id}] - {self.nombre} | {self.email}"
