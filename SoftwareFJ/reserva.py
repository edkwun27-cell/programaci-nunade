"""
reserva.py
Clase Reserva que integra cliente, servicio, duración y estado.
Implementa confirmación, cancelación y procesamiento con excepciones (requerido).
"""

from cliente import Cliente
from servicio import Servicio
from exceptions import ReservaInvalidaError, OperacionNoPermitidaError, ParametrosInvalidosError
from logger import logger

class Reserva:
    def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio, duracion: float):
        if not id_reserva:
            raise ReservaInvalidaError("ID de reserva inválido")
        if not isinstance(cliente, Cliente) or not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("Cliente o servicio inválido")
        if duracion <= 0:
            raise ParametrosInvalidosError("Duración debe ser mayor a 0")
        if not servicio.disponible:
            raise ReservaInvalidaError("Servicio no disponible")

        self.id = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"
        self.costo_final = None
        logger.info(f"Reserva {self.id} creada")

    def confirmar(self):
        if self.estado != "pendiente":
            raise OperacionNoPermitidaError("Solo se pueden confirmar reservas pendientes")
        self.estado = "confirmada"
        logger.info(f"Reserva {self.id} confirmada")

    def cancelar(self):
        if self.estado in ["cancelada", "procesada"]:
            raise OperacionNoPermitidaError("No se puede cancelar esta reserva")
        self.estado = "cancelada"
        logger.info(f"Reserva {self.id} cancelada")

    def procesar(self, con_impuesto=True, descuento=0.0):
        if self.estado not in ["pendiente", "confirmada"]:
            raise OperacionNoPermitidaError("No se puede procesar esta reserva")
        try:
            self.servicio.validar_parametros()
            if con_impuesto:
                self.costo_final = self.servicio.calcular_costo_con_impuestos(self.duracion, descuento=descuento)
            else:
                self.costo_final = self.servicio.calcular_costo(self.duracion)
            self.estado = "procesada"
            logger.info(f"Reserva {self.id} procesada - Costo: {self.costo_final}")
            return self.costo_final
        except Exception as e:
            logger.error(f"Error al procesar {self.id}: {e}")
            raise ReservaInvalidaError(f"Error al procesar reserva {self.id}") from e

    def obtener_info(self):
        return f"Reserva[{self.id}] {self.cliente.nombre} - {self.servicio.nombre} - {self.estado}"
