"""
servicio.py
Clase abstracta Servicio + 3 servicios especializados con polimorfismo (requerido).
Incluye métodos sobrecargados para cálculo de costos.
"""

from abc import abstractmethod
from entidad import Entidad
from exceptions import ServicioInvalidoError, ParametrosInvalidosError

class Servicio(Entidad):
    def __init__(self, id_servicio: str, nombre: str, costo_base: float):
        super().__init__(id_servicio)
        if not nombre or len(nombre.strip()) < 3:
            raise ServicioInvalidoError("Nombre de servicio inválido")
        if costo_base < 0:
            raise ServicioInvalidoError("Costo base no puede ser negativo")
        self._nombre = nombre.strip()
        self._costo_base = float(costo_base)
        self._disponible = True

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_base(self):
        return self._costo_base

    @property
    def disponible(self):
        return self._disponible

    @abstractmethod
    def calcular_costo(self, duracion: float, **kwargs) -> float:
        pass

    @abstractmethod
    def describir(self) -> str:
        pass

    @abstractmethod
    def validar_parametros(self, **kwargs) -> None:
        pass

    # Método sobrecargado (parámetros opcionales)
    def calcular_costo_con_impuestos(self, duracion: float, impuesto: float = 0.19, descuento: float = 0.0) -> float:
        costo = self.calcular_costo(duracion)
        if not (0 <= descuento <= 1):
            raise ParametrosInvalidosError("Descuento inválido")
        return round(costo * (1 - descuento) * (1 + impuesto), 2)

    def obtener_info(self) -> str:
        return f"Servicio[{self.id}] - {self.nombre} | ${self.costo_base}"


class ReservaSala(Servicio):
    def __init__(self, id_servicio, nombre, costo_base, capacidad, ubicacion):
        super().__init__(id_servicio, nombre, costo_base)
        if capacidad <= 0:
            raise ServicioInvalidoError("Capacidad inválida")
        self._capacidad = capacidad
        self._ubicacion = ubicacion

    def calcular_costo(self, duracion: float, **kwargs) -> float:
        if duracion <= 0:
            raise ParametrosInvalidosError("Duración inválida")
        return round(self.costo_base * duracion, 2)

    def describir(self) -> str:
        return f"Sala {self.nombre} (Cap: {self._capacidad}, {self._ubicacion})"

    def validar_parametros(self, **kwargs) -> None:
        personas = kwargs.get("personas")
        if personas and (personas <= 0 or personas > self._capacidad):
            raise ParametrosInvalidosError("Número de personas inválido")


class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre, costo_base, tipo_equipo, cantidad):
        super().__init__(id_servicio, nombre, costo_base)
        if cantidad <= 0:
            raise ServicioInvalidoError("Cantidad inválida")
        self._tipo = tipo_equipo
        self._cantidad = cantidad

    def calcular_costo(self, duracion: float, **kwargs) -> float:
        if duracion <= 0:
            raise ParametrosInvalidosError("Duración inválida")
        cant = kwargs.get("cantidad", 1)
        if cant > self._cantidad:
            raise ServicioInvalidoError("Cantidad insuficiente")
        return round(self.costo_base * duracion * cant, 2)

    def describir(self) -> str:
        return f"Alquiler {self._tipo} - {self.nombre}"

    def validar_parametros(self, **kwargs) -> None:
        cant = kwargs.get("cantidad", 1)
        if cant <= 0:
            raise ParametrosInvalidosError("Cantidad inválida")


class AsesoriaEspecializada(Servicio):
    def __init__(self, id_servicio, nombre, costo_base, nivel, especialista):
        super().__init__(id_servicio, nombre, costo_base)
        if nivel.lower() not in ["básico", "intermedio", "avanzado"]:
            raise ServicioInvalidoError("Nivel inválido")
        self._nivel = nivel.lower()
        self._especialista = especialista

    def calcular_costo(self, duracion: float, **kwargs) -> float:
        if duracion <= 0:
            raise ParametrosInvalidosError("Duración inválida")
        mult = {"básico": 1.0, "intermedio": 1.3, "avanzado": 1.6}[self._nivel]
        return round(self.costo_base * duracion * mult, 2)

    def describir(self) -> str:
        return f"Asesoría {self._nivel} - {self.nombre}"

    def validar_parametros(self, **kwargs) -> None:
        pass
