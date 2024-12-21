
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
        return self._staffId

class StaffId():
    _staffIdCounter = 1

    def __init__(self):
        _staffId = self._generateStaffId()

    @staticmethod
    def _generateStaffId():
        _staffId = StaffId._staffIdCounter
        StaffId._staffIdCounter += 1
        return _staffId

    def get_staff_id(self):
        return self._staffId

    @staticmethod
    def changeStaticCounter( newCounter):
        if newCounter > StaffId._staffIdCounter:
            StaffId._staffIdCounter = newCounter

class Lecturer(Staff):
    def __init__(self, user_information):
        super().__init__(user_information)
        self._departmentId = ""
        self._facultyId = ""

    def get_departmentId(self):
        return self._departmentId
class Advisor(Lecturer):
    def __init__(self, user_information):
        super().__init__(user_information)

    def checkCourseRequest(self, courseRequest):
        pre = courseRequest.get_course().getCourseRequirements()
        return pre.pre.isStudentQualified(courseRequest.get_student())
    def approveCourseRequest(self, courseRequest):
        courseRequest.get_student().get_current_courses().add(courseRequest.get_course())


class Admin(Staff):
    def __init__(self, user_information):
        super().__init__(user_information)

class DepartmentScheduler(Staff):
    def __init__(self, user_information):
        super().__init__(user_information)
    def returnCoursesForDepartment(self, courses, department):
        departmentCourses = []
        for course in courses:
            if course.getCourseRequirements().get_departmentID().getDepartmentName().equalsIgnoreCase(department.getDepartmentID().getDepartmentName()):
                departmentCourses.append(course)
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


