import Department
import Faculty
from User import Lecturer



class Course:
    def __init__(self, courseInformation, courseRequirements, courseSections):
        self.courseInformation = courseInformation
        self.courseRequirements = courseRequirements
        self.courseSections = courseSections

    @staticmethod
    def from_dict(data):
        ci = CourseInformation.from_dict(data["courseInformation"])
        cr = CourseRequirements.from_dict(data["courseRequirements"])
        css = list()
        for data_cs in data["courseSections"]:
            css.append(CourseSection.from_dict(data_cs))

        return Course(ci, cr, css)

    def getCourseName(self):
        return self.courseInformation.getCourseName()

    def getCourseCode(self):
        return self.courseInformation.getCourseCode()

    def getCourseInformation(self):
        return self.courseInformation

    def getCourseRequirements(self):
        return self.courseRequirements

    def getCourseSections(self):
        return self.courseSections


class CourseInformation:
    def __init__(self, courseName, courseCode):
        self.courseName = courseName
        self.courseCode = courseCode

    @staticmethod
    def from_dict(data):
        return CourseInformation(data["courseName"], data["courseCode"])

    def getCourseCode(self):
        return self.courseCode

    def getCourseName(self):
        return self.courseName


class TakenCourse:
    def __init__(self, courseInformation, midtermScore, finalScore):
        self._courseInformation = courseInformation
        self._midterm_score = midtermScore
        self._final_score = finalScore

    @staticmethod
    def from_dict(data):
        ci = data["_courseInformation"]
        ms = int(data["_midterm_score"])
        fs = int(data["_final_score"])
        return TakenCourse(ci,ms,fs)

    def getCourseInformation(self):
        return self._courseInformation

    def getMidtermScore(self):
        return self._midterm_score

    def getFinalScore(self):
        return self._final_score

    def calculateCourseScore(self):
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
        ans = [False, False, False, False]
        ans[0] = student.getCurrentClass() >= self._minimum_current_class
        ans[
            1] = self._departmentID is None or self._departmentID == student.get_studentID().get_departmentID().getDepartmentID()
        ans[2] = self._facultyID is None or self._facultyID == student.get_studentID().get_facultyID().getFacultyID()
        ans[3] = self.checkPrerequisiteCourse(student)
        return ans

    def checkPrerequisiteCourse(self, student):
        if self._prerequisite_courses is None or len(self._prerequisite_courses) == 0:
            return True

        for courseInformation in self._prerequisite_courses:
            check = False
            for takenCourse in student.getTranscript().getTakenCourses():
                if takenCourse.get_courseInformation().equals(courseInformation):
                    check = True
                    break

            if not check:
                return False

        return True

    def get_departmentID(self, _departmentID):
        return self._departmentID

    def get_facultyID(self, _facultyID):
        return self._facultyID

    def get_minimum_current_class(self):
        return self._minimum_current_class

    def getDepartmentID(self):
        return self._departmentID.getDepartmentID()

    def getFacultyID(self):
        return self._facultyID.getFacultyID()


class CourseSection:
    def __init__(self, day, sectionTime, lecturer, quota):
        self._day = day
        self._sectionTime = sectionTime
        self._lecturer = lecturer
        self._quota = quota

    @staticmethod
    def from_dict(data):
        d = int(data["_day"])
        lec = Lecturer.from_dict(data["_lecturer"])
        sect = int(data["_sectionTime"])
        q = int(data["_quota"])
        return CourseSection(d, sect, lec, q)

    def createClassroom(self, classroom):
        if self._quota <= classroom.get_capacity():
            return classroom
        else:
            return "Classroom capacity is not enough"



