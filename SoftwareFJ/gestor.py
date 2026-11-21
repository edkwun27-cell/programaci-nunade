"""
gestor.py
Gestor del sistema. Maneja listas de clientes, servicios y reservas en memoria.
"""

from cliente import Cliente
from servicio import Servicio
from reserva import Reserva
from exceptions import *
from logger import logger

class GestorSistema:
    def __init__(self):
        self.clientes = {}
        self.servicios = {}
        self.reservas = {}
        logger.info("Gestor inicializado")

    def registrar_cliente(self, id_c, nombre, email, telefono):
        try:
            if id_c in self.clientes:
                raise ClienteInvalidoError("Cliente ya existe")
            cliente = Cliente(id_c, nombre, email, telefono)
            self.clientes[id_c] = cliente
            logger.info(f"Cliente registrado: {id_c}")
            return cliente
        except Exception as e:
            logger.error(f"Error al registrar cliente: {e}")
            raise

    def registrar_servicio(self, servicio: Servicio):
        if servicio.id in self.servicios:
            raise ServicioInvalidoError("Servicio ya existe")
        self.servicios[servicio.id] = servicio
        logger.info(f"Servicio registrado: {servicio.id}")
        return servicio

    def crear_reserva(self, id_r, id_cliente, id_servicio, duracion):
        try:
            if id_r in self.reservas:
                raise ReservaInvalidaError("Reserva ya existe")
            cliente = self.clientes.get(id_cliente)
            servicio = self.servicios.get(id_servicio)
            if not cliente:
                raise ReservaInvalidaError("Cliente no encontrado")
            if not servicio:
                raise ReservaInvalidaError("Servicio no encontrado")
            reserva = Reserva(id_r, cliente, servicio, duracion)
            self.reservas[id_r] = reserva
            return reserva
        except Exception as e:
            logger.error(f"Error al crear reserva: {e}")
            raise
