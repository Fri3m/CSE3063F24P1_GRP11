import Department
import Faculty
from Classroom import Classroom
from User import Lecturer
import logging

from pythonCode.Logger import setup_logger
logger = setup_logger("Course")

class Course:
    def __init__(self, courseInformation, courseRequirements, courseSections):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self.courseInformation = courseInformation
        self.courseRequirements = courseRequirements
        self.courseSections = courseSections
        self._currentStudentCount = 0
        self._courseCapacity = int(1e9)
        for courseSection in courseSections:
            if courseSection._classRoom.get_capacity() < self._courseCapacity:
                self._courseCapacity = courseSection._classRoom.get_capacity()

    @staticmethod
    def from_dict(data):
        ci = CourseInformation.from_dict(data["courseInformation"])
        cr = CourseRequirements.from_dict(data["courseRequirements"])
        css = list()
        for data_cs in data["courseSections"]:
            css.append(CourseSection.from_dict(data_cs))

        return Course(ci, cr, css)

    def getCourseName(self):
        logger.info(f"The getCourseName method in the {self.__class__.__name__} class is called.")
        return self.courseInformation.getCourseName()

    def getCourseCode(self):
        logger.info(f"The getCourseCode method in the {self.__class__.__name__} class is called.")
        return self.courseInformation.getCourseCode()

    def getCourseInformation(self):
        logger.info(f"The getCourseInformation method in the {self.__class__.__name__} class is called.")
        return self.courseInformation

    def getCourseRequirements(self):
        logger.info(f"The getCourseRequirements method in the {self.__class__.__name__} class is called")
        return self.courseRequirements

    def getCourseSections(self):
        logger.info(f"The getCourseSections method in the {self.__class__.__name__} class is called.")
        return self.courseSections

    def getCourseCapacity(self):
        logger.info(f"The getCourseCapacity method in the {self.__class__.__name__} class is called.")
        return self._courseCapacity

    def getCurrentStudentCount(self):
        logger.info(f"The getCurrentStudentCount method in the {self.__class__.__name__} class is called.")
        return self._currentStudentCount

    def incrementCurrentStudentCount(self):
        logger.info(f"The incrementCurrentStudentCount method in the {self.__class__.__name__} class is called.")
        self._currentStudentCount += 1


class CourseInformation:
    def __init__(self, courseName, courseCode):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self.courseName = courseName
        self.courseCode = courseCode

    @staticmethod
    def from_dict(data):
        return CourseInformation(data["courseName"], data["courseCode"])

    def getCourseCode(self):
        logger.info(f"The getCourseCode method in the {self.__class__.__name__} class is called.")
        return self.courseCode

    def getCourseName(self):
        logger.info(f"The getCourseName method in the {self.__class__.__name__} class is called.")
        return self.courseName


class TakenCourse:
    def __init__(self, courseInformation, midtermScore, finalScore):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._courseInformation = courseInformation
        self._midterm_score = midtermScore
        self._final_score = finalScore

    @staticmethod
    def from_dict(data):
        ci = CourseInformation.from_dict(data["_courseInformation"])
        ms = int(data["_midterm_score"])
        fs = int(data["_final_score"])
        return TakenCourse(ci, ms, fs)

    def getCourseInformation(self):
        logger.info(f"The getCourseInformation method in the {self.__class__.__name__} class is called.")
        return self._courseInformation

    def getMidtermScore(self):
        logger.info(f"The getMidtermScore method in the {self.__class__.__name__} class is called.")
        return self._midterm_score

    def getFinalScore(self):
        logger.info(f"The getFinalScore method in the {self.__class__.__name__} class is called.")
        return self._final_score

    def calculateCourseScore(self):
        logger.info("Calculating the course score.")
        total = self._midterm_score * 0.6 + self._final_score * 0.4
        if total >= 90:
            return Score.AA
        elif total >= 85:
            return Score.BA
        elif total >= 80:
            return Score.BB
        elif total >= 75:
            return Score.CB
        elif total >= 65:
            return Score.CC
        elif total >= 58:
            return Score.DC
        elif total >= 50:
            return Score.DD
        else:
            return Score.FF

    def getCourseScore(self):

        return self.calculateCourseScore()


class Score:
    AA = 4.0
    BA = 3.5
    BB = 3.0
    CB = 2.5
    CC = 2.0
    DC = 1.5
    DD = 1.0
    FF = 0.0


class CourseRequirements:
    def __init__(self, prerequisiteCourses, minimumCurrentClass, facultyID, departmentID):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._prerequisite_courses = prerequisiteCourses
        self._minimum_current_class = minimumCurrentClass
        self._facultyID = facultyID
        self._departmentID = departmentID

    @staticmethod
    def from_dict(data):
        prerequisite_courses_dict = data["_prerequisite_courses"]
        prerequisite_courses_list = list()

        for x in prerequisite_courses_dict:
            prerequisite_courses_list.append(CourseInformation.from_dict(x))

        mcc = int(data["_minimum_current_class"])
        fid = Faculty.FacultyID.from_dict(data["_facultyID"])
        did = Department.DepartmentID.from_dict(data["_departmentID"])

        return CourseRequirements(prerequisite_courses_list, mcc, fid, did)

    def isStudentQualified(self, student):
        logger.info("Checking if student is qualified for the course.")
        ans = [False, False, False, False]
        ans[0] = student.getCurrentClass() >= self._minimum_current_class
        ans[
            1] = self._departmentID is None or self._departmentID.getDepartmentID() == student.get_studentID().get_departmentID().getDepartmentID()
        ans[2] = self._facultyID is None or self._facultyID.getFacultyID() == student.get_studentID().get_facultyID().getFacultyID()
        ans[3] = self.checkPrerequisiteCourse(student)
        return ans

    def checkPrerequisiteCourse(self, student):
        logger.info("Checking if student has taken the prerequisite courses.")
        if self._prerequisite_courses is None or len(self._prerequisite_courses) == 0:
            return True

        for courseInformation in self._prerequisite_courses:
            check = False
            for takenCourse in student.getTranscript().getTakenCourses():
                if takenCourse.getCourseInformation().getCourseName()==courseInformation.getCourseName():
                    check = True
                    break

            if not check:
                return False

        return True

    def get_departmentID(self, _departmentID):
        logger.info(f"The get_departmentID method in the {self.__class__.__name__} class is called.")
        return self._departmentID

    def get_facultyID(self, _facultyID):
        logger.info(f"The get_facultyID method in the {self.__class__.__name__} class is called.")
        return self._facultyID

    def get_minimum_current_class(self):
        logger.info(f"The get_minimum_current_class method in the {self.__class__.__name__} class is called.")
        return self._minimum_current_class

    def getDepartmentID(self):
        logger.info(f"The getDepartmentID method in the {self.__class__.__name__} class is called.")
        return self._departmentID.getDepartmentID()

    def getFacultyID(self):
        logger.info(f"The getFacultyID method in the {self.__class__.__name__} class is called.")
        return self._facultyID.getFacultyID()


class CourseSection:
    def __init__(self, day, sectionTime, lecturer, classRoom):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._day = day
        self._sectionTime = sectionTime
        self._lecturer = lecturer
        self._classRoom = classRoom
        self._quota = classRoom.get_capacity()

    @staticmethod
    def from_dict(data):
        d = int(data["_day"])
        lec = Lecturer.from_dict(data["_lecturer"])
        sect = int(data["_sectionTime"])
        cr = Classroom.from_dict(data["_classRoom"])
        return CourseSection(d, sect, lec, cr)
