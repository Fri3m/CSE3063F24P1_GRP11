import unittest

from pythonCode.Course import CourseInformation, TakenCourse, Score
from pythonCode.DataManagement import DataManagement


class Course_test(unittest.TestCase):
    def isStudentQualified_test(self):
        data_management = DataManagement()
        student = data_management.getStudent("duyguates@marun.edu.tr")
        course = data_management.getCourse("General Biology")
        courseRequirements = course.getCourseRequirements()
        trueAns = [True,True,True,True]
        calculatedAns = courseRequirements.isStudentQualified(student)
        for i in range(len(trueAns)):
            self.assertEqual(trueAns[i], calculatedAns[i], "Student is not qualified!")

    def  calculateCourseScore_test(self):
        courseInformation = CourseInformation("test","test")
        midterm_score = 85
        final_score = 85
        course = TakenCourse(courseInformation, midterm_score, final_score)
        course_score = course.getCourseScore()

        self.assertEqual(course_score, Score.BA, "Course score is not calculated correctly!")

