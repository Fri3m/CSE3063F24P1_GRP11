

import Student
from Course import TakenCourse
import logging

from pythonCode.Logger import setup_logger
logger = setup_logger("Transcript")

class Transcript:
    def __init__(self, student_id):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._student_id = student_id
        self._taken_courses = []
        self._gpa = 0.0



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
        logger.info("Adding taken courses to the transcript.")
        self._taken_courses.extend(taken_courses)
        self.calculateGPA()

        return True

    def addTakenCourse(self, taken_course):
        logger.info("Adding taken course to the transcript.")
        self._taken_courses.append(taken_course)
        self.calculateGPA()

        return True

    def calculateGPA(self):
        logger.info("Calculating GPA.")
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
            }.get(course.getCourseScore(), 0.0)


            self._gpa += score

        self._gpa /= len(self._taken_courses)


    def getTakenCourses(self):
        logger.info(f"The getTakenCourses method in the {self.__class__.__name__} class is called.")
        return self._taken_courses

    def get_GPA(self):
        logger.info(f"The get_GPA method in the {self.__class__.__name__} class is called.")
        self.calculateGPA()
        return self._gpa
