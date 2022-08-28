import logging
import sys
from types import FrameType
from typing import cast

from loguru import logger

from app.core.config import Settings


class InterceptHandler(logging.Handler):
    """
    Intercepts Logs from python loggin lib and use loguru instead
    """

    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def configure_logger(settings: Settings):
    """
    Configure logger
    """
    logging.getLogger().handlers.clear()
    logging.getLogger().handlers = [InterceptHandler()]

    log_level = log_level_from_str(settings.log_level)
    for logger_name in settings.loggers:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=log_level)]
        logging_logger.propagate = False

    logger.configure(handlers=[{"sink": sys.stderr, "level": log_level}])


def log_level_from_str(log_level_str: str):
    """
    Load Log Level from environment
    """
    default_log = logging.INFO
    level_map: map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "ERROR": logging.ERROR,
    }

    if level_map[log_level_str] is None:
        return default_log
    else:
        return level_map[log_level_str]
