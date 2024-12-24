import logging


logging.getLogger().handlers.clear()

import UserInformation
from pythonCode.Logger import setup_logger
logger = setup_logger("User")


class User():

    def __init__(self, user_information):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._user_information = user_information

    def getUserInformation(self):
        logger.info(f"The getUserInformation method in the {self.__class__.__name__} class is called.")
        return self._user_information


class Staff(User):
    def __init__(self, user_information):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        super().__init__(user_information)
        self._staffId = StaffId()

    def get_staffId(self):
        logger.info(f"The get_staffId method in the {self.__class__.__name__} class is called.")
        return self._staffId


class StaffId:
    _staffIdCounter = 1

    def __init__(self):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        StaffId._generateStaffId(self)


    @staticmethod
    def from_dict(data):
        sid = StaffId()
        sid._staffId = int(data["_staffId"])
        return sid


    @staticmethod
    def _generateStaffId(staffId):
        logger.info(f"The _generateStaffId method in the {staffId.__class__.__name__} class is called.")
        staffId._staffId = StaffId._staffIdCounter
        StaffId._staffIdCounter += 1


    def get_staff_id(self):
        logger.info(f"The get_staff_id method in the {self.__class__.__name__} class is called.")
        return self._staffId

    @staticmethod
    def changeStaticCounter(newCounter):
        logger.info(f"The changeStaticCounter method in the {StaffId.__class__.__name__} class is called.")
        if newCounter > StaffId._staffIdCounter:
            StaffId._staffIdCounter = newCounter


class Lecturer(Staff):
    def __init__(self, user_information):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        super().__init__(user_information)
        self._departmentId = ""
        self._facultyId = ""

    @staticmethod
    def from_dict(data):
        lec =Lecturer(UserInformation.UserInformation.from_dict(data["_user_information"]))
        lec._staffId = StaffId.from_dict(data["_staffId"])
        return lec

    def get_departmentId(self):
        logger.info(f"The get_departmentId method in the {self.__class__.__name__} class is called.")
        return self._departmentId


class Advisor(Lecturer):
    def __init__(self, user_information):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        super().__init__(user_information)

    @staticmethod
    def from_dict(data):
        ad = Advisor(UserInformation.UserInformation.from_dict(data["_user_information"]))
        ad._staffId = StaffId.from_dict(data["_staffId"])
        return ad

    def checkCourseRequest(self, courseRequest):
        logger.info("Checking course request in Advisor class")
        pre = courseRequest.get_course().getCourseRequirements()
        return pre.isStudentQualified(courseRequest.get_student())

    def approveCourseRequest(self, courseRequest):
        logger.info("Approving course request in Advisor class")
        courseRequest.get_student().get_current_courses().append(courseRequest.get_course().getCourseInformation())
        courseRequest.get_course().incrementCurrentStudentCount()



class Admin(Staff):
    def __init__(self, user_information):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        super().__init__(user_information)


class DepartmentScheduler(Staff):
    def __init__(self, user_information):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")

        super().__init__(user_information)

    @staticmethod
    def from_dict(data):
        ds = DepartmentScheduler(UserInformation.UserInformation.from_dict(data["_user_information"]))
        ds._staffId = StaffId.from_dict(data["_staffId"])
        return ds


    def returnCoursesForDepartment(self, courses, department):
        logger.info("Returning courses for department in DepartmentScheduler class")

        departmentCourses = []

        for course in courses:
            if course.getCourseRequirements().get_departmentID().getDepartmentName().equalsIgnoreCase(
                    department.getDepartmentID().getDepartmentName()):
                departmentCourses.append(course)

        return departmentCourses

    def changeCourseSectionDayAndTime(self, courseSection, day, time):
        logger.info("Changing course section day and time in DepartmentScheduler class")

        courseSection._day = day
        courseSection._sectionTime = time


class StudentsAffairs(Staff):
    def __init__(self, user_information):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        super().__init__(user_information)

    @staticmethod
    def from_dict(data):
        sa = StudentsAffairs(UserInformation.UserInformation.from_dict(data["_user_information"]))
        sa._staffId = StaffId.from_dict(data["_staffId"])
        return sa


    def addCourse(self, course, courses):
        logger.info("Adding course in StudentsAffairs class")
        courses.add(course)
        return True

    def removeCourse(self, course, courses):
        logger.info("Removing course in StudentsAffairs class")
        courses.remove(course)
        return True

    def sendNotification(self, student, message):
        logger.info("Sending notification in StudentsAffairs class")
        student.getNotifications().append(message)
        return True

    def sentNotificationToDepartment(self, department, students, message):
        logger.info("Sending notification to department in StudentsAffairs class")
        for student in students:
            if student.getDepartment().getDepartmentID().getDepartmentName().equalsIgnoreCase(department.getDepartmentID().getDepartmentName()):
                student.getNotifications().append(message)
        return True

    def sendNotificationToFaculty(self, faculty, students, message):
        logger.info("Sending notification to faculty in StudentsAffairs class")
        for student in students:
            if student.getDepartment().getDepartmentID().getFacultyName().equalsIgnoreCase(faculty.getFacultyName()):
                student.getNotifications().append(message)
        return True

    def sendNotificationToAllStudents(self, students, message):
        logger.info("Sending notification to all students in StudentsAffairs class")
        for student in students:
            student.getNotifications().append(message)
        return True


class DepartmentHead(Staff):
    def __init__(self, user_information):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        super().__init__(user_information)

    def changeCourseSectionQuota(self, courseSection, quota):
        logger.info("Changing course section quota in DepartmentHead class")
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
