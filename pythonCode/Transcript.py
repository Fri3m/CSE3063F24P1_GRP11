import logging

import Student
from Course import TakenCourse


class Transcript:
    def __init__(self, student_id):
        self._student_id = student_id
        self._taken_courses = []
        self._gpa = 0.0

        logging.info(f"Transcript created for student ID: {self._student_id.get_ID()}")

    @staticmethod
    def from_dict(data):
        sid = Student.StudentID.from_dict(data["_student_id"])
        tc_list =list()

        for dtc in data["_taken_courses"]:
            tc_list.append(TakenCourse.from_dict(dtc))

        tc = Transcript(sid)
        tc.addTakenCourses(tc_list)
        tc.calculateGPA()
        return tc


    def addTakenCourses(self, taken_courses):
        logging.info(f"Adding courses to transcript for student ID: {self._student_id.get_ID()}. Courses: {taken_courses}")
        self._taken_courses.extend(taken_courses)
        self.calculateGPA()
        logging.info(f"Courses added. New GPA: {self._gpa:.2f}")
        return True

    def addTakenCourse(self, taken_course):
        logging.info(f"Adding course {taken_course.get_course_name()} to transcript for student ID: {self._student_id.get_ID()}.")
        self._taken_courses.append(taken_course)
        self.calculateGPA()
        logging.info(f"Course {taken_course.get_course_name()} added. New GPA: {self._gpa:.2f}")
        return True

    def calculateGPA(self):
        logging.debug(f"Calculating GPA for student ID: {self._student_id.get_ID()} based on courses: {self._taken_courses}.")
        self._gpa = 0.0
        if not self._taken_courses:
            logging.debug("No courses taken yet, GPA remains 0.0.")
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

            logging.debug(f"Course {course.get_course_name()} has score {course.get_course_score()} which gives GPA score {score}.")
            self._gpa += score

        self._gpa /= len(self._taken_courses)
        logging.debug(f"New GPA calculated: {self._gpa:.2f}")

    def getTakenCourses(self):
        logging.debug(f"Retrieving taken courses for student ID: {self._student_id.get_ID()}.")
        return self._taken_courses

    def get_GPA(self):
        logging.debug(f"Retrieving GPA for student ID: {self._student_id.get_ID()}.")
        self.calculateGPA()
        return self._gpa
