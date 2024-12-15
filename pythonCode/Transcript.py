
class Transcript:
    def __init__(self, student_id):
        self._student_id = student_id
        self._taken_courses = []
        self._gpa = 0.0

    def add_taken_courses(self, taken_courses):
        self._taken_courses.extend(taken_courses)
        self._calculate_gpa()
        return True

    def add_taken_course(self, taken_course):
        self._taken_courses.append(taken_course)
        self._calculate_gpa()
        return True

    def _calculate_gpa(self):
        self._gpa = 0.0
        if not self._taken_courses:
            return

        for course in self._taken_courses:
            score = {
                "AA": 4.0,
                "BA": 3.5,
                "BB": 3.0,
                "CB": 2.5,
                "CC": 2.0,
                "DC": 1.5,
                "DD": 1.0
            }.get(course.get_course_score(), 0.0)

            self._gpa += score

        self._gpa /= len(self._taken_courses)

    def get_taken_courses(self):
        return self._taken_courses

    def get_gpa(self):
        self._calculate_gpa()
        return self._gpa
