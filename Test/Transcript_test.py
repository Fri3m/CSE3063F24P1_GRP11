import unittest

from pythonCode.DataManagement import DataManagement


class Transcript_test(unittest.TestCase):
    def test_calculateGPA_test(self):
        data_management = DataManagement()
        student = data_management.getStudent("caneraksu@marun.edu.tr")
        transcript = student.getTranscript()
        trueGPA = 2.0
        calculatedGPA = transcript.get_GPA()
        self.assertEqual(trueGPA, calculatedGPA, "GPA should be the same!")