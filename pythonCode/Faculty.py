

class FacultyID:
    def __init__(self, facultyID, facultyName):

        self._FacultyID = facultyID
        self._FacultyName = facultyName

    @staticmethod
    def from_dict(data):
        return FacultyID(data["_FacultyID"], data["_FacultyName"])

    def getFacultyID(self):

        return self._FacultyID

    def getFacultyName(self):

        return self._FacultyName


class Faculty:
    def __init__(self, facultyID):

        self._facultyID = facultyID
        self._departments = list()

    @staticmethod
    def from_dict(data):
        return Faculty(FacultyID.from_dict(data["_facultyID"]))

    def addDepartment(self, department):

        self._departments.append(department)
        return True

    def removeDepartment(self, department):
        if department in self._departments:

            self._departments.remove(department)
            return True

        return False

    def getFacultyID(self):

        return self._facultyID