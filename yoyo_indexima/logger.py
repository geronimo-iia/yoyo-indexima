"""Python logger definition."""
import logging
import os

from crayons import green, magenta, red, yellow


__all__ = ["init_root_logger"]


class CrayonsFormatter(logging.Formatter):
    """Colored Log Formater."""

    def __init__(self, fmt=None, datefmt=None, style='%'):
        logging.Formatter.__init__(self, fmt, datefmt, style)

    def format(self, record):
        s = super().format(record)
        if record.levelno == logging.DEBUG:
            return str(magenta(s))
        if record.levelno == logging.INFO:
            return str(green(s))
        if record.levelno == logging.WARN:
            return str(yellow(s))
        if record.levelno == logging.ERROR:
            return str(red(s))
        return s


default_log_level = int(os.getenv('LOG_LEVEL', str(logging.INFO)))


def init_root_logger(
    log_level=default_log_level,
    fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
):
    """Return a configured root logger."""

    _logger = logging.getLogger()
    _logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    formater_class = CrayonsFormatter
    if formater_class:
        console_handler.setFormatter(formater_class(fmt=fmt, datefmt=datefmt))
    _logger.addHandler(console_handler)

    """Configure Yoyo log"""
    logging.getLogger('yoyo.migrations').setLevel(logging.INFO)
    logging.getLogger('yoyo_indexima.cli').setLevel(logging.INFO)
    logging.getLogger('pyhive.hive').setLevel(logging.WARN)
    return _logger
