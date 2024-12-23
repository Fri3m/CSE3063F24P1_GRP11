import Faculty
import logging

from pythonCode.Logger import setup_logger
logger = setup_logger("Department")

class Department:
    def __init__(self, departmentID, facultyID):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._departmentID = departmentID
        self._facultyID = facultyID
        self._lecturers = list()

    @staticmethod
    def from_dict(data):
        return Department(DepartmentID.from_dict(data["_departmentID"]), Faculty.FacultyID.from_dict(data["_facultyID"]) )


    def addLecturer(self, lecturer):
        logger.info("Adding lecturer to the department.")
        self._lecturers.append(lecturer)
        return True

    def getDepartmentID(self):
        logger.info(f"The getDepartmentID method in the {self.__class__.__name__} class is called.")
        return self._departmentID

    def get_facultyID(self):
        logger.info(f"The get_facultyID method in the {self.__class__.__name__} class is called.")
        return self._facultyID


class DepartmentID:
    def __init__(self, departmentID, departmentName):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._departmentID = departmentID
        self._departmentName = departmentName

    @staticmethod
    def from_dict(data):
        return  DepartmentID(data["_departmentID"], data["_departmentName"])

    def getDepartmentID(self):
        logger.info(f"The getDepartmentID method in the {self.__class__.__name__} class is called.")
        return self._departmentID

    def getDepartmentName(self):
        logger.info(f"The getDepartmentName method in the {self.__class__.__name__} class is called.")
        return self._departmentName
