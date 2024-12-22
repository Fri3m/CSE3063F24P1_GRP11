class FacultyID:
    def __init__(self, facultyID, facultyName):
        print(f"Creating FacultyID with ID: {facultyID}, Name: {facultyName}")
        self._FacultyID = facultyID
        self._FacultyName = facultyName

    def get_faculty_id(self):
        print(f"Getting FacultyID: {self._FacultyID}")
        return self._FacultyID

    def get_faculty_name(self):
        print(f"Getting FacultyName: {self._FacultyName}")
        return self._FacultyName


class Faculty:
    def __init__(self, facultyID):
        print(f"Creating Faculty with FacultyID: {facultyID.get_faculty_id()}")
        self._facultyID = facultyID
        self._departments = list()

    def addDepartment(self, department):
        print(f"Adding department: {department}")
        self._departments.append(department)
        return True

    def removeDepartment(self, department):
        if department in self._departments:
            print(f"Removing department: {department}")
            self._departments.remove(department)
            return True
        print(f"Department not found: {department}")
        return False

    def getFacultyID(self):
        print(f"Getting FacultyID for Faculty: {self._facultyID.get_faculty_id()}")
        return self._facultyID