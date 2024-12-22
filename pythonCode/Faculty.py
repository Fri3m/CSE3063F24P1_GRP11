class FacultyID:
    def __init__(self, facultyID, facultyName):
        self._FacultyID = facultyID
        self._FacultyName = facultyName

    def get_faculty_id(self):
        return self._FacultyID

    def get_faculty_name(self):
        return self._FacultyName


class Faculty:
    def __init__(self, facultyID):
        self._facultyID = facultyID
        self._departments = list()

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
