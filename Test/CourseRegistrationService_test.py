import unittest

from pythonCode.CourseRegistrationService import CourseRegistrationService, CourseRequest
from pythonCode.DataManagement import DataManagement


class CourseRegistrationService_test(unittest.TestCase):
    def test_checkAccesiableRequests_test(self):
        data_management = DataManagement()
        advisor = data_management.getAdvisor("sevdaucar@marun.edu.tr")
        student = data_management.getStudent("selinpolat@marun.edu.tr")

        courseRegistrationService = CourseRegistrationService()
        courseRegistrationService.createCourseRequest(student,data_management.getCourse("Fluid Mechanics"))
        courseRegistrationService.createCourseRequest(student,data_management.getCourse("Heat Transfer"))
        courseRegistrationService.createCourseRequest(student,data_management.getCourse("Material Sci."))
        trueList = []
        trueList.append(CourseRequest(student,data_management.getCourse("Fluid Mechanics"),student.get_advisorID()))
        trueList.append(CourseRequest(student,data_management.getCourse("Heat Transfer"),student.get_advisorID()))
        trueList.append(CourseRequest(student,data_management.getCourse("Material Sci."),student.get_advisorID()))

        calculatedList = courseRegistrationService.checkAccesiableRequests(advisor)
        for i in range(len(trueList)):
            self.assertEqual(trueList[i].get_course().getCourseName(), calculatedList[i].get_course().getCourseName(), "Requests are not calculated correctly!")
