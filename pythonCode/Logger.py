import logging


def setup_logger(name: str, log_file: str = "../Logs/app.log", level: int = logging.INFO):

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logger = logging.getLogger(name)
    logger.setLevel(level)


    if not logger.handlers:

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setFormatter(formatter)


        logger.addHandler(file_handler)

    return logger
