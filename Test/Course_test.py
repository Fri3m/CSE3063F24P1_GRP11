import unittest

from pythonCode.Course import CourseInformation, TakenCourse, Score
from pythonCode.DataManagement import DataManagement


class Course_test(unittest.TestCase):
    def test_isStudentQualified_test(self):
        data_management = DataManagement()
        student = data_management.getStudent("sulekorkmaz@marun.edu.tr")
        course = data_management.getCourse("Database Systems")
        courseRequirements = course.getCourseRequirements()
        trueAns = [True,True,True,True]
        calculatedAns = courseRequirements.isStudentQualified(student)
        for i in range(len(trueAns)):
            self.assertEqual(trueAns[i], calculatedAns[i], "Student is not qualified!")

    def  test_calculateCourseScore_test(self):
        courseInformation = CourseInformation("Introduction to Computer Engineering","CS1200")
        midterm_score = 70
        final_score = 95
        course = TakenCourse(courseInformation, midterm_score, final_score)
        course_score = course.getCourseScore()

        self.assertEqual(course_score, Score.BB, "Course score is not calculated correctly!")

