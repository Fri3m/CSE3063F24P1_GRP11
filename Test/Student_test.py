import unittest

from pythonCode.DataManagement import DataManagement


class Student_test(unittest.TestCase):
    def test_createStudentID_test(self):
        data_management = DataManagement()
        student = data_management.getStudent("sulekorkmaz@marun.edu.tr")
        departmentID = data_management.getDepartment("Computer Engineering").getDepartmentID()
        facultyID = data_management.getFaculty("Engineering").getFacultyID()
        studentID = student.get_studentID()
        self.assertEqual(studentID.get_departmentID().getDepartmentName(),"ComputerEngineering", "Department name should be the same!")
        self.assertEqual(studentID.get_facultyID().getFacultyName(),"Engineering", "Faculty name should be the same!")
        self.assertEqual(studentID.get_entrance_date(),2022, "Entrance date should be the same!")
        self.assertEqual(studentID.get_entrance_rank(),32, "Entrance rank should be the same!")