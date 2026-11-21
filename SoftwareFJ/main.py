"""
main.py
Simulación de al menos 10 operaciones (válidas e inválidas) según lo requerido.
El sistema continúa funcionando ante errores.
"""

from gestor import GestorSistema
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from exceptions import *
from logger import logger

def ejecutar(descripcion, funcion, *args, **kwargs):
    print(f"\n--- {descripcion} ---")
    try:
        resultado = funcion(*args, **kwargs)
    except Exception as e:
        logger.error(f"{descripcion}: {e}")
        print(f"ERROR: {e}")
    else:
        logger.info(f"{descripcion}: OK")
        print(f"OK: {resultado if resultado else 'Completado'}")
    finally:
        print("--- Fin ---")

def main():
    print("=== SISTEMA SOFTWARE FJ ===")
    gestor = GestorSistema()

    # Operaciones de clientes (válidas e inválidas)
    ejecutar("Cliente válido", gestor.registrar_cliente, "C001", "Juan Pérez", "juan@email.com", "3001234567")
    ejecutar("Cliente email inválido", gestor.registrar_cliente, "C002", "Ana", "ana-invalido", "3100000000")
    ejecutar("Cliente nombre corto", gestor.registrar_cliente, "C003", "Al", "al@email.com", "3155555555")
    ejecutar("Cliente válido 2", gestor.registrar_cliente, "C004", "María López", "maria@email.com", "3201112233")

    # Servicios
    sala = ReservaSala("S001", "Sala Norte", 80.0, 10, "Piso 2")
    ejecutar("Servicio sala válida", gestor.registrar_servicio, sala)

    equipo = AlquilerEquipo("S002", "Laptop", 25.0, "Laptop", 5)
    ejecutar("Servicio equipo válido", gestor.registrar_servicio, equipo)

    asesoria = AsesoriaEspecializada("S003", "Asesoría Software", 120.0, "avanzado", "Ing. Ruiz")
    ejecutar("Servicio asesoría válida", gestor.registrar_servicio, asesoria)

    # Servicio inválido
    try:
        mala = ReservaSala("S004", "Mala", 50, -1, "X")
        gestor.registrar_servicio(mala)
    except ServicioInvalidoError as e:
        print(f"ERROR servicio: {e}")
        logger.error(f"Servicio inválido: {e}")

    # Reservas
    ejecutar("Reserva válida", gestor.crear_reserva, "R001", "C001", "S001", 3)
    ejecutar("Reserva cliente inexistente", gestor.crear_reserva, "R002", "C999", "S002", 2)
    ejecutar("Reserva duración inválida", gestor.crear_reserva, "R003", "C004", "S003", -1)
    ejecutar("Reserva válida 2", gestor.crear_reserva, "R004", "C004", "S003", 2)

    # Procesar reservas
    r1 = gestor.reservas.get("R001")
    if r1:
        ejecutar("Confirmar R001", r1.confirmar)
        ejecutar("Procesar R001 con impuestos", r1.procesar, True, 0.1)
        ejecutar("Cancelar ya procesada", r1.cancelar)

    r4 = gestor.reservas.get("R004")
    if r4:
        ejecutar("Procesar R004 sin impuestos", r4.procesar, False)

    print("\n=== RESUMEN ===")
    print(f"Clientes: {len(gestor.clientes)}")
    print(f"Servicios: {len(gestor.servicios)}")
    print(f"Reservas: {len(gestor.reservas)}")
    print("Sistema finalizado. Revisar logs.txt")
    logger.info("Simulación terminada")

if __name__ == "__main__":
    main()
