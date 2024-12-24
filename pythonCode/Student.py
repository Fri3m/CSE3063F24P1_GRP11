import Course
import Department
import Faculty
import Transcript
import UserInformation
from pythonCode.User import User, StaffId
import logging

from pythonCode.Logger import setup_logger

logger = setup_logger("Student")


class Student(User):
    def __init__(self, user_information, student_id, transcript, advisor_id, current_class):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        super().__init__(user_information)
        self._student_id = student_id
        self._transcript = transcript
        self._advisor_id = advisor_id
        self._current_class = current_class
        self._current_courses = []  # course information
        self._notifications = []

    @staticmethod
    def from_dict(data):
        ui = UserInformation.UserInformation.from_dict(data["_user_information"])
        sid = StudentID.from_dict(data["_student_id"])
        trc = Transcript.Transcript.from_dict(data["_transcript"])
        ad_id = StaffId.from_dict(data["_advisor_id"])
        c_class = int(data["_current_class"])
        c_courses = list()
        for x in data["_current_courses"]:
            c_courses.append(Course.CourseInformation.from_dict(x))

        s = Student(ui, sid, trc, ad_id, c_class)
        s._current_courses = c_courses
        return s

    def takeCourse(self, course, course_registration_service):
        logger.info(f"{self._user_information.get_UNIVERSITY_EMAIL} takeCourse method called.")
        course_registration_service.createCourseRequest(self, course)

        return True

    def getTranscript(self):
        logger.info(f"{self._user_information.get_UNIVERSITY_EMAIL} getTranscript method called.")
        return self._transcript

    def getCurrentClass(self):
        logger.info(f"{self._user_information.get_UNIVERSITY_EMAIL} getCurrentClass method called.")
        return self._current_class

    def get_studentID(self):
        logger.info(f"{self._user_information.get_UNIVERSITY_EMAIL} get_studentID method called.")
        return self._student_id

    def get_advisorID(self):
        logger.info(f"{self._user_information.get_UNIVERSITY_EMAIL} get_advisorID method called.")
        return self._advisor_id

    def get_current_courses(self):  # course information
        logger.info(f"{self._user_information.get_UNIVERSITY_EMAIL} get_current_courses method called.")
        return self._current_courses

    def getNotifications(self):
        logger.info(f"{self._user_information.get_UNIVERSITY_EMAIL} getNotifications method called.")
        return self._notifications


class StudentID:
    def __init__(self, department_id, entrance_date, entrance_rank, faculty_id):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._department_id = department_id
        self._entrance_date = entrance_date
        self._entrance_rank = entrance_rank
        self._faculty_id = faculty_id
        self._id = self.createStudentID()

    @staticmethod
    def from_dict(data):
        did = Department.DepartmentID.from_dict(data["_department_id"])
        ed = int(data["_entrance_date"])
        er = int(data["_entrance_rank"])
        fid = Faculty.FacultyID.from_dict(data["_faculty_id"])
        return StudentID(did, ed, er, fid)

    def createStudentID(self):
        logger.info("Creating student ID in StudentID class.")
        first_part = str(self._department_id.getDepartmentID())
        second_part = str(self._entrance_date)[1:]  # Get the last 3 digits of the year (2024 -> 024)
        third_part = str(self._entrance_rank).zfill(3)  # Ensure its at least 3 digits long
        student_id = first_part + second_part + third_part

        return student_id

    def get_departmentID(self):
        logger.info(f"{self.__class__.__name__} get_departmentID method called.")
        return self._department_id

    def get_facultyID(self):
        logger.info(f"{self.__class__.__name__} get_facultyID method called.")
        return self._faculty_id

    def get_entrance_date(self):
        logger.info(f"{self.__class__.__name__} get_entrance_date method called.")
        return self._entrance_date

    def get_entrance_rank(self):
        logger.info(f"{self.__class__.__name__} get_entrance_rank method called.")
        return self._entrance_rank

    def get_ID(self):
        logger.info(f"{self.__class__.__name__} get_ID method called.")
        return self._id
