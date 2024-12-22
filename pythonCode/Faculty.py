class FacultyID:
    def __init__(self, facultyID, facultyName):
        logging.info(f"Creating FacultyID with ID: {facultyID}, Name: {facultyName}")
        self._FacultyID = facultyID
        self._FacultyName = facultyName

    @staticmethod
    def from_dict(data):
        return FacultyID(data["_FacultyID"], data["_FacultyName"])

    def get_faculty_id(self):
        logging.info(f"Getting FacultyID: {self._FacultyID}")
        return self._FacultyID

    def get_faculty_name(self):
        logging.info(f"Getting FacultyName: {self._FacultyName}")
        return self._FacultyName


class Faculty:
    def __init__(self, facultyID):
        logging.info(f"Creating Faculty with FacultyID: {facultyID.get_faculty_id()}")
        self._facultyID = facultyID
        self._departments = list()

    @staticmethod
    def from_dict(data):
        return Faculty(FacultyID.from_dict(data["_facultyID"]))

    def addDepartment(self, department):
        logging.info(f"Adding department: {department}")
        self._departments.append(department)
        return True

    def removeDepartment(self, department):
        if department in self._departments:
            logging.info(f"Removing department: {department}")
            self._departments.remove(department)
            return True
        logging.info(f"Department not found: {department}")
        return False

    def getFacultyID(self):
        logging.info(f"Getting FacultyID for Faculty: {self._facultyID.get_faculty_id()}")
        return self._facultyID