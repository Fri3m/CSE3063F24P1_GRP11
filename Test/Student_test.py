import unittest

from pythonCode.DataManagement import DataManagement


class Student_test(unittest.TestCase):
    def createStudentID_test(self):
        data_management = DataManagement()
        student = data_management.getStudent("baristokgoz@marun.edu.tr")
        departmentID = data_management.getDepartment("Computer Engineering").getDepartmentID()
        facultyID = data_management.getFaculty("Engineering").getFacultyID()
        studentID = student.get_studentID()
        self.assertEqual(studentID.get_departmentID().getDepartmentName(),"ComputerEngineering", "Department name should be the same!")
        self.assertEqual(studentID.get_facultyID().getFacultyName(),"Engineering", "Faculty name should be the same!")
        self.assertEqual(studentID.get_entrance_date(),2021, "Entrance date should be the same!")
        self.assertEqual(studentID.get_entrance_rank(),70, "Entrance rank should be the same!")