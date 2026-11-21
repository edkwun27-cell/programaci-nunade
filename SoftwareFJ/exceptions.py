"""
exceptions.py
Excepciones personalizadas requeridas por el trabajo.
"""

class SoftwareFJError(Exception):
    """Excepción base del sistema."""
    pass

class ClienteInvalidoError(SoftwareFJError):
    """Error en datos de cliente."""
    pass

class ServicioInvalidoError(SoftwareFJError):
    """Error en servicio."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Error en reserva."""
    pass

class ParametrosInvalidosError(SoftwareFJError):
    """Parámetros incorrectos o faltantes."""
    pass

class OperacionNoPermitidaError(SoftwareFJError):
    """Operación no permitida según el estado."""
    pass
