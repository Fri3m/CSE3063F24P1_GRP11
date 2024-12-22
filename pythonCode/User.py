

import UserInformation
from pythonCode.Logger import setup_logger



class User():
    def __init__(self, user_information):
        logger = setup_logger("file_logger")
        logger.info(f"{self.__class__.__name__} classes created.")
        self._user_information = user_information

    def getUserInformation(self):

        return self._user_information


class Staff(User):
    def __init__(self, user_information):

        super().__init__(user_information)
        self._staffId = StaffId()

    def get_staffId(self):

        return self._staffId


class StaffId:
    _staffIdCounter = 1

    def __init__(self):

        StaffId._generateStaffId(self)


    @staticmethod
    def from_dict(data):
        sid = StaffId()
        sid._staffId = int(data["_staffId"])
        return sid


    @staticmethod
    def _generateStaffId(staffId):
        staffId._staffId = StaffId._staffIdCounter
        StaffId._staffIdCounter += 1


    def get_staff_id(self):

        return self._staffId

    @staticmethod
    def changeStaticCounter(newCounter):

        if newCounter > StaffId._staffIdCounter:
            StaffId._staffIdCounter = newCounter


class Lecturer(Staff):
    def __init__(self, user_information):

        super().__init__(user_information)
        self._departmentId = ""
        self._facultyId = ""

    @staticmethod
    def from_dict(data):
        lec =Lecturer(UserInformation.UserInformation.from_dict(data["_user_information"]))
        lec._staffId = StaffId.from_dict(data["_staffId"])
        return lec

    def get_departmentId(self):

        return self._departmentId


class Advisor(Lecturer):
    def __init__(self, user_information):

        super().__init__(user_information)

    @staticmethod
    def from_dict(data):
        ad = Advisor(UserInformation.UserInformation.from_dict(data["_user_information"]))
        ad._staffId = StaffId.from_dict(data["_staffId"])
        return ad

    def checkCourseRequest(self, courseRequest):

        pre = courseRequest.get_course().getCourseRequirements()
        return pre.isStudentQualified(courseRequest.get_student())

    def approveCourseRequest(self, courseRequest):

        courseRequest.get_student().get_current_courses().append(courseRequest.get_course().getCourseInformation())
        courseRequest.get_course().incrementCurrentStudentCount()



class Admin(Staff):
    def __init__(self, user_information):

        super().__init__(user_information)


class DepartmentScheduler(Staff):
    def __init__(self, user_information):


        super().__init__(user_information)

    @staticmethod
    def from_dict(data):
        ds = DepartmentScheduler(UserInformation.UserInformation.from_dict(data["_user_information"]))
        ds._staffId = StaffId.from_dict(data["_staffId"])
        return ds


    def returnCoursesForDepartment(self, courses, department):


        departmentCourses = []

        for course in courses:
            if course.getCourseRequirements().get_departmentID().getDepartmentName().equalsIgnoreCase(
                    department.getDepartmentID().getDepartmentName()):
                departmentCourses.append(course)

        return departmentCourses

    def changeCourseSectionDayAndTime(self, courseSection, day, time):


        courseSection._day = day
        courseSection._sectionTime = time


class StudentsAffairs(Staff):
    def __init__(self, user_information):

        super().__init__(user_information)

    @staticmethod
    def from_dict(data):
        sa = StudentsAffairs(UserInformation.UserInformation.from_dict(data["_user_information"]))
        sa._staffId = StaffId.from_dict(data["_staffId"])
        return sa


    def addCourse(self, course, courses):
        courses.add(course)
        return True

    def removeCourse(self, course, courses):
        courses.remove(course)
        return True


class DepartmentHead(Staff):
    def __init__(self, user_information):
        super().__init__(user_information)

    def changeCourseSectionQuota(self, courseSection, quota):
        print(courseSection._quota)
        courseSection._quota = quota

    def from_dict(data):
        dh = DepartmentHead(UserInformation.UserInformation.from_dict(data["_user_information"]))
        dh._staffId = StaffId.from_dict(data["_staffId"])
        return dh


# staffId = StaffId()
# staffId2 = StaffId()
# staffId3 = StaffId()
# staffId4 = StaffId()
# staffId5 = StaffId()
# staffId6 = StaffId()
#
# print(staffId.get_staff_id())
# print(staffId5.get_staff_id())
