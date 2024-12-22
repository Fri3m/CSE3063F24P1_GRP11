import logging

import UserInformation


logger = logging.getLogger(__name__)

class User():
    def __init__(self, user_information):
        logger.info('User initialized')
        self._user_information = user_information

    def getUserInformation(self):
        logger.info('getUserInformation called')
        return self._user_information


class Staff(User):
    def __init__(self, user_information):
        logger.info('Staff initialized')
        super().__init__(user_information)
        self._staffId = StaffId()

    def get_staffId(self):
        logger.info(f'get_staffId called: {str(self._staffId)}')
        return self._staffId


class StaffId:
    _staffIdCounter = 1

    def __init__(self):
        logger.info('StaffId initialized')
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
        logger.info('Staff ID generated, Current staffIdCounter: ' + str(StaffId._staffIdCounter))

    def get_staff_id(self):
        logger.info(f'get_staffId called: {str(self._staffId)}')
        return self._staffId

    @staticmethod
    def changeStaticCounter(newCounter):
        logger.info('changeStaticCounter called')
        if newCounter > StaffId._staffIdCounter:
            StaffId._staffIdCounter = newCounter


class Lecturer(Staff):
    def __init__(self, user_information):
        logger.info('Lecturer initialized')
        super().__init__(user_information)
        self._departmentId = ""
        self._facultyId = ""

    @staticmethod
    def from_dict(data):
        lec =Lecturer(UserInformation.UserInformation.from_dict(data["_user_information"]))
        lec._staffId = StaffId.from_dict(data["_staffId"])
        return lec

    def get_departmentId(self):
        logger.info('get_departmentId called')
        return self._departmentId


class Advisor(Lecturer):
    def __init__(self, user_information):
        logger.info('Advisor initialized')
        super().__init__(user_information)

    @staticmethod
    def from_dict(data):
        ad = Advisor(UserInformation.UserInformation.from_dict(data["_user_information"]))
        ad._staffId = StaffId.from_dict(data["_staffId"])
        return ad

    def checkCourseRequest(self, courseRequest):
        logger.info('checkCourseRequest called')
        pre = courseRequest.get_course().getCourseRequirements()
        return pre.isStudentQualified(courseRequest.get_student())

    def approveCourseRequest(self, courseRequest):
        logger.info('approveCourseRequest called')
        courseRequest.get_student().get_current_courses().append(courseRequest.get_course().getCourseInformation())
        courseRequest.get_course().incrementCurrentStudentCount()



class Admin(Staff):
    def __init__(self, user_information):
        logger.info('Admin initialized')
        super().__init__(user_information)


class DepartmentScheduler(Staff):
    def __init__(self, user_information):

        logger.info('DepartmentScheduler initialized')
        super().__init__(user_information)

    @staticmethod
    def from_dict(data):
        ds = DepartmentScheduler(UserInformation.UserInformation.from_dict(data["_user_information"]))
        ds._staffId = StaffId.from_dict(data["_staffId"])
        return ds


    def returnCoursesForDepartment(self, courses, department):

        logger.info('returnCoursesForDepartment called')
        departmentCourses = []
        logger.info("Control if the courses are in the given department")
        for course in courses:
            if course.getCourseRequirements().get_departmentID().getDepartmentName().equalsIgnoreCase(
                    department.getDepartmentID().getDepartmentName()):
                departmentCourses.append(course)
                logger.info("Course: {} added to the departmentCourses list".format(course.getCourseName()))
        return departmentCourses

    def changeCourseSectionDayAndTime(self, courseSection, day, time):

        logger.info('changeCourseSectionDayAndTime called')
        courseSection._day = day
        courseSection._sectionTime = time


class StudentsAffairs(Staff):
    def __init__(self, user_information):
        logger.info('StudentsAffairs initialized')
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
