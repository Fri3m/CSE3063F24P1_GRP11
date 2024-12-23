import logging

from pythonCode.Logger import setup_logger
logger = setup_logger("CourseRegistrationService")
class CourseRegistrationService:
    def __init__(self):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._courseRequests = list()

    def createCourseRequest(self, student, course):
        logger.info("Creating a course request.")
        self._courseRequests.append(CourseRequest(student, course, student.get_advisorID()))

    def checkAccesiableRequests(self, advisor):
        logger.info("Checking accessible requests.")
        accessibleRequests = list()
        for courseRequest in self._courseRequests:
            if advisor.get_staffId().get_staff_id() == courseRequest.get_advisorID().get_staff_id():
                accessibleRequests.append(courseRequest)
        return accessibleRequests

    def removeCourseRequest(self, courseRequest):
        logger.info("Removing a course request.")
        self._courseRequests.remove(courseRequest)

    def checkClassroomAvailabilityForDayAndTime(self, day, time, classroom, allCourses):
        logger.info(f"Checking classroom availability {day} {time} {classroom.get_classroom_name()}")
        for course in allCourses:
            for courseSection in course.getCourseSections():
                if courseSection._day == day and courseSection._sectionTime == time and courseSection._classroom == classroom:
                    return False
        return True


class CourseRequest:
    def __init__(self, student, course, advisorID):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._student = student
        self._course = course
        self._advisorID = advisorID

    def get_student(self):
        logger.info(f"The get_student method in the {self.__class__.__name__} class is called.")
        return self._student

    def get_course(self):
        logger.info(f"The get_course method in the {self.__class__.__name__} class is called.")
        return self._course

    def get_advisorID(self):
        logger.info(f"The get_advisorID method in the {self.__class__.__name__} class is called.")
        return self._advisorID
