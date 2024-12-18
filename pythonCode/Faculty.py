class FacultyID:
    def __init__(self, FacultyID, FacultyName):
        self._FacultyID = facultyID
        self._FacultyName = facultyName

    def get_faculty_id(self):
        return self._faculty_id

    def get_faculty_name(self):
        return self._faculty_name


class Faculty:
    def __init__(self, faculty_id):
        self._FacultyID = facultyID
        self._departments = []

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
