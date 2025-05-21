import logging
import sys
from pathlib import Path
from typing import Optional

from .config import LOG_COLORS
from .levels import register_custom_levels
from .loop import loop_status

# Bind loop_status method to Logger
logging.Logger.loop_status = loop_status
register_custom_levels()


def get_logger(
    name: str,
    level: int = logging.DEBUG,
    log_to_file: bool = False,
    log_file_path: Optional[str] = None,
    use_colors: bool = True,
    overwrite_handlers: bool = False,
    show_seconds: bool = True
) -> logging.Logger:
    """
    Creates a logger with color and file output support.

    Args:
        name: Logger name (usually script/module name).
        level: Logging level (e.g., logging.INFO).
        log_to_file: If True, writes logs to a file.
        log_file_path: Path to the file for log output.
        use_colors: Enables ANSI color output (terminal only).
        overwrite_handlers: If True, clears existing handlers.
        show_seconds: Include seconds in the log timestamp.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if overwrite_handlers:
        logger.handlers.clear()

    if not logger.handlers:
        time_format = "%H:%M:%S" if show_seconds else "%H:%M"

        try:
            import colorlog

            formatter = colorlog.ColoredFormatter(
                fmt=f"%(log_color)s[%(asctime)s] [{name}] [%(levelname)s] : %(message)s",
                datefmt=time_format,
                log_colors=LOG_COLORS,
            )
        except ImportError:
            formatter = logging.Formatter(
                fmt=f"[%(asctime)s] [{name}] [%(levelname)s] : %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        if log_to_file and log_file_path:
            log_path = Path(log_file_path)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_path, encoding="utf-8")
            file_handler.setFormatter(logging.Formatter(
                fmt=f"[{name}][%(asctime)s] [%(levelname)s] : %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            ))
            logger.addHandler(file_handler)

    logger.propagate = False
    return logger
