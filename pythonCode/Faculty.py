import logging

from pythonCode.Logger import setup_logger
logger = setup_logger("Faculty")

class FacultyID:
    def __init__(self, facultyID, facultyName):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._FacultyID = facultyID
        self._FacultyName = facultyName

    @staticmethod
    def from_dict(data):
        return FacultyID(data["_FacultyID"], data["_FacultyName"])

    def getFacultyID(self):
        logger.info(f"The getFacultyID method in the {self.__class__.__name__} class is called.")
        return self._FacultyID

    def getFacultyName(self):
        logger.info(f"The getFacultyName method in the {self.__class__.__name__} class is called.")
        return self._FacultyName


class Faculty:
    def __init__(self, facultyID):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._facultyID = facultyID
        self._departments = list()

    @staticmethod
    def from_dict(data):
        return Faculty(FacultyID.from_dict(data["_facultyID"]))

    def addDepartment(self, department):
        logger.info("Adding department to faculty")
        self._departments.append(department)
        return True

    def removeDepartment(self, department):
        logger.info("Removing department from faculty")
        if department in self._departments:

            self._departments.remove(department)
            return True

        return False

    def getFacultyID(self):
        logger.info(f"The getFacultyID method in the {self.__class__.__name__} class is called.")
        return self._facultyID