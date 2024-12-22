class CourseRegistrationService:
    def __init__(self):
        self._courseRequests = list()

    def createCourseRequest(self, student, course):
        self._courseRequests.append(CourseRequest(student, course, student.get_advisorID()))

    def checkAccesiableRequests(self, advisor):
        accessibleRequests = list()
        for courseRequest in self._courseRequests:
            if advisor.get_staffId() == courseRequest.get_advisorID:
                accessibleRequests.append(courseRequest)
        return accessibleRequests

    def removeCourseRequest(self, courseRequest):
        self._courseRequests.remove(courseRequest)


class CourseRequest:
    def __init__(self, student, course, advisorID):
        self._student = student
        self._course = course
        self._advisorID = advisorID

    def get_student(self):
        return self._student

    def get_course(self):
        return self._course

    def get_advisorID(self):
        return self._advisorID
