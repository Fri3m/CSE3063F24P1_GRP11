import logging

from pythonCode.Logger import setup_logger
logger = setup_logger("Classroom")
class Classroom:
    def __init__(self, classroom_name, capacity):
        logging.getLogger().handlers.clear()

        logger.info(f"{self.__class__.__name__} classes created.")
        self._classroom_name = classroom_name
        self._capacity = capacity

    @staticmethod
    def from_dict(data):
        return Classroom(data["_classroom_name"], int(data["_capacity"]))

    def get_classroom_name(self):
        logger.info(f"The get_classroom_name method in the {self.__class__.__name__} class is called.")
        return self._classroom_name

    def get_capacity(self):
        logger.info(f"The get_capacity method in the {self.__class__.__name__} class is called.")
        return self._capacity