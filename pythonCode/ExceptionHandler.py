import logging
import sys
from Logger import setup_logger


exception_logger = setup_logger("exception", log_file="../Logs/exceptions.log")


def handle_exception(exc_type, exc_value, exc_traceback):
    exception_logger.error("An error occurred!", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception
