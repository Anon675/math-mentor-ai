import sys
from pathlib import Path
from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {message}",
)

logger.add(
    LOG_FILE,
    rotation="10 MB",
    retention="7 days",
    compression="zip",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
)

def get_logger():
    return logger