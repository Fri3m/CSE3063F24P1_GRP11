from pythonCode.User import User


class Student(User):
    def __init__(self, user_information, student_id, transcript, advisor_id, current_class):
        super().__init__(user_information)
        self._student_id = student_id
        self._transcript = transcript
        self._advisor_id = advisor_id
        self._current_class = current_class
        self._current_courses = []

    def take_course(self, course, course_registration_service):
        course_registration_service.create_course_request(self, course)
        return True

    def get_transcript(self):
        return self._transcript

    def get_current_class(self):
        return self._current_class

    def get_student_id(self):
        return self._student_id

    def get_advisor_id(self):
        return self._advisor_id

    def get_current_courses(self):
        return self._current_courses


class StudentID:
    def __init__(self, department_id, entrance_date, entrance_rank, faculty_id):
        self._department_id = department_id
        self._entrance_date = entrance_date
        self._entrance_rank = entrance_rank
        self._faculty_id = faculty_id
        self._id = self._create_student_id()

    def _create_student_id(self):
        first_part = str(self._department_id.getDepartmentID())
        second_part = str(self._entrance_date)[1:]  # Get the last 3 digits of the year (e.g., 2024 -> 024)
        third_part = str(self._entrance_rank).zfill(3)  # Ensure it's at least 3 digits long
        return first_part + second_part + third_part

    def get_department_id(self):
        return self._department_id

    def get_faculty_id(self):
        return self._faculty_id

    def get_entrance_date(self):
        return self._entrance_date

    def get_entrance_rank(self):
        return self._entrance_rank

    def get_id(self):
        return self._id
