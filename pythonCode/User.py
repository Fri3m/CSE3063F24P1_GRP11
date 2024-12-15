
class User():
    def __init__(self, user_information):
        self._user_information = user_information

    def getUserInformation(self):
        return self._user_information

class Staff(User):
    def __init__(self, user_information):
        super().__init__(user_information)
        self._staffId = StaffId

    def get_staffId(self):
        return self._staff_id

class StaffId():
    _staffIdCounter = 1

    def __init__(self):
        _staffId = _generateStaffId()

    @staticmethod
    def _generateStaffId(self):
        self._staffId = _staffIdCounter
        staffId._staffIdCounter += 1
        return self._staffId

    def get_staff_id(self):
        return self._staff_id

    @staticmethod
    def changeStaticCounter(self, newCounter):
        if newCounter > _staffIdCounter:
            _staffIdCounter = newCounter

class Lecturer(staff):
    def __init__(self, user_information):
        super().__init__(user_information)
        self._departmentId = DepartmentId
        self._facultyId = FacultyId

    def get_departmentId(self):
        return self._departmentId
class Advisor(Lecturer):
    def __init__(self, user_information):
        super().__init__(user_information)

    def checkCourseRequest(self, courseRequest):
        pre = courseRequest.get_course().getCourseRequirements()
        return pre.pre.isStudentQualified(courseRequest.get_student())
    def approveCourseRequest(self, courseRequest):
        ccourseRequest.get_student().get_current_courses().add(courseRequest.get_course())

class Admin(staff):
    def __init__(self, user_information):
        super().__init__(user_information)

class DepartmentScheduler(Staff):
    def __init__(self, user_information):
        super().__init__(user_information)
    def returnCoursesForDepartment(self, courses, department):
        departmentCourses = []
        for course in courses:
            if course.getCourseRequirements().get_departmentID().getDepartmentName().equalsIgnoreCase(department.getDepartmentID().getDepartmentName()):
                departmentCourses.add(course)
        return departmentCourses
    def changeCourseSectionDayAndTime(self, courseSection, day, time):
        courseSection._day = day
        courseSection._sectionTime = time
class StudentsAffairs(Staff):
    def __init__(self, user_information):
        super().__init__(user_information)
    def addCourse(self, course, courses):
        courses.add(course)
        return True
    def removeCourse(self, course, courses):
        courses.remove(course)
        return True


