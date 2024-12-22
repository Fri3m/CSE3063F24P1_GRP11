import Faculty


class Department:
    def __init__(self, departmentID, facultyID):
        self._departmentID = departmentID
        self._facultyID = facultyID
        self._lecturers = list()

    @staticmethod
    def from_dict(data):
        return Department(DepartmentID.from_dict(data["_departmentID"]), Faculty.FacultyID.from_dict(data["_facultyID"]) )


    def addLecturer(self, lecturer):
        self._lecturers.append(lecturer)
        return True

    def getDepartmentID(self):
        return self._departmentID

    def get_facultyID(self):
        return self._facultyID


class DepartmentID:
    def __init__(self, departmentID, departmentName):
        self._departmentID = departmentID
        self._departmentName = departmentName

    @staticmethod
    def from_dict(data):
        return  DepartmentID(data["_departmentID"], data["_departmentName"])

    def getDepartmentID(self):
        return self._departmentID

    def getDepartmentName(self):
        return self._departmentName
