"""
logger.py
Registro de eventos y errores en archivo (requerido por el trabajo).
"""

import logging
from pathlib import Path

LOG_FILE = Path(__file__).parent / "logs.txt"

logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    logger.addHandler(handler)
    logger.info("Sistema iniciado")
