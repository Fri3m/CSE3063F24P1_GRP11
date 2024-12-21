from pythonCode.User import User

import logging

class Student(User):
    def __init__(self, user_information, student_id, transcript, advisor_id, current_class):
        super().__init__(user_information)
        self._student_id = student_id
        self._transcript = transcript
        self._advisor_id = advisor_id
        self._current_class = current_class
        self._current_courses = []

        logging.info(f"Student created with ID: {self._student_id.get_id()}")

    def take_course(self, course, course_registration_service):
        logging.info(f"Student {self._student_id.get_id()} attempting to take course {course}.")
        course_registration_service.create_course_request(self, course)
        logging.info(f"Student {self._student_id.get_id()} successfully enrolled in course {course}.")
        return True

    def get_transcript(self):
        logging.debug(f"Retrieving transcript for student {self._student_id.get_id()}.")
        return self._transcript

    def get_current_class(self):
        logging.debug(f"Retrieving current class for student {self._student_id.get_id()}.")
        return self._current_class

    def get_student_id(self):
        logging.debug(f"Retrieving student ID: {self._student_id.get_id()}.")
        return self._student_id

    def get_advisor_id(self):
        logging.debug(f"Retrieving advisor ID for student {self._student_id.get_id()}.")
        return self._advisor_id

    def get_current_courses(self):
        logging.debug(f"Retrieving current courses for student {self._student_id.get_id()}.")
        return self._current_courses

class StudentID:
    def __init__(self, department_id, entrance_date, entrance_rank, faculty_id):
        self._department_id = department_id
        self._entrance_date = entrance_date
        self._entrance_rank = entrance_rank
        self._faculty_id = faculty_id
        self._id = self._create_student_id()

        # Loglama
        logging.info(f"Student ID created: {self._id} (Department: {self._department_id.getDepartmentID()}, "
                     f"Entrance Date: {self._entrance_date}, Rank: {self._entrance_rank})")

    def _create_student_id(self):
        logging.debug(f"Creating student ID using department {self._department_id.getDepartmentID()}, "
                      f"entrance year {self._entrance_date}, rank {self._entrance_rank}.")
        first_part = str(self._department_id.getDepartmentID())
        second_part = str(self._entrance_date)[1:]  # Get the last 3 digits of the year (2024 -> 024)
        third_part = str(self._entrance_rank).zfill(3)  # Ensure its at least 3 digits long
        student_id = first_part + second_part + third_part
        logging.debug(f"Generated student ID: {student_id}")
        return student_id

    def get_department_id(self):
        logging.debug(f"Retrieving department ID: {self._department_id.getDepartmentID()}.")
        return self._department_id

    def get_faculty_id(self):
        logging.debug(f"Retrieving faculty ID: {self._faculty_id}.")
        return self._faculty_id

    def get_entrance_date(self):
        logging.debug(f"Retrieving entrance date: {self._entrance_date}.")
        return self._entrance_date

    def get_entrance_rank(self):
        logging.debug(f"Retrieving entrance rank: {self._entrance_rank}.")
        return self._entrance_rank

    def get_id(self):
        logging.debug(f"Retrieving student ID: {self._id}.")
        return self._id
