class Course:
    def __init__(self, courseInformation, courseRequirements, courseSections):
        self.courseInformation = courseInformation
        self.courseRequirements = courseRequirements
        self.courseSections = courseSections

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

    def getCourseCode(self):
        return self.courseCode

    def getCourseName(self):
        return self.courseName


class TakenCourse:
    def __init__(self, courseInformation, midtermScore, finalScore):
        self._courseInformation = courseInformation
        self._midterm_score = midtermScore
        self._final_score = finalScore

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

    def isStudentQualified(self, student):
        ans = [False, False, False, False]
        ans[0] = student.getCurrentClass() >= self._minimum_current_class
        ans[
            1] = self._departmentID is None or self._departmentID == student.get_studentID().get_departmentID().getDepartmentID()
        ans[2] = self._facultyID is None or self._facultyID == student.get_studentID.get_facultyID().getFacultyID()
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
    def __init__(self, day, sectionTime, lecturer):
        self._day = day
        self._sectionTime = sectionTime
        self._lecturer = lecturer
