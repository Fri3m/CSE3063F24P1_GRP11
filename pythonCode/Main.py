import random
import sys

from Classroom import Classroom
from CourseRegistrationService import CourseRegistrationService
from LoginAuthService import LoginAuthService

from pythonCode.DataManagement import DataManagement
from pythonCode.Day import Day, SectionTime
from pythonCode.Department import Department, DepartmentID
from pythonCode.Faculty import FacultyID
from pythonCode.Logger import setup_logger
from pythonCode.User import StaffId, Admin, Advisor
from pythonCode.UserInformation import UserInformation
import DataManagement
from pythonCode.ExceptionHandler import handle_exception
import logging


logging.getLogger().handlers.clear()

logger = setup_logger("Main")
day_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}
sectionTime_dict = {0: "First", 1: "Second", 2: "Third", 3: "Fourth", 4: "Fifth", 5: "Sixth", 6: "Seventh", 7: "Eighth",
                    8: "Ninth"}


class Main:

    user_type = str()

    def main(self):

        logger.info("Program started")


        print("Welcome to the Course Registration System")
        self.startMenu()

    def __init__(self):


        self._data_management = DataManagement.DataManagement()
        self._login_auth_service = LoginAuthService()
        self._course_registration_service = CourseRegistrationService()


        self._faculties = self._data_management.getAllFaculties()
        self._departments = self._data_management.getAllDepartments()
        self._students = self._data_management.getAllStudents()
        self._advisors = self._data_management.getAllAdvisors()
        self._lecturers = self._data_management.getAllLecturers()
        self._departmentSchedulers = self._data_management.getAllDepartmentSchedulers()
        self._departmentHeads = self._data_management.getAllDepartmentHeads()
        self._studentsAffairs = self._data_management.getAllStudentsAffairs()
        self._courses = self._data_management.getAllCourses()
        self._classrooms = self._data_management.getAllClassrooms()

        self.coursesNameDict = dict()
        for course in self._courses:
            self.coursesNameDict[course.getCourseName()] = course

        self.changeStaticStaffID()

        _admin = Admin(UserInformation(("admin"), ("admin"), ("admin"), ("admin"), ("admin"), ("admin"), ("admin")))

        self._users = []
        self._users.extend(self._students)
        self._users.extend(self._advisors)
        self._users.extend(self._lecturers)
        self._users.extend(self._departmentSchedulers)
        self._users.extend(self._studentsAffairs)
        self._users.extend(self._departmentHeads)
        self._users.append(_admin)

        logger.info("All users added to the system")

        self._login_auth_service._users = self._users

        for _departments in self._departments:
            for _lecturers in self._lecturers:
                if _lecturers.get_departmentId() is not None and _lecturers.get_departmentId() == _departments.getDepartmentID().getDepartmentID():
                    _departments.add_lecturer(_lecturers)

    def changeStaticStaffID(self):

        maxID = int(0)

        for _advisors in self._advisors:
            if int(_advisors.get_staffId().get_staff_id()) > maxID:
                maxID = int(_advisors.get_staffId().get_staff_id())
        for _lecturers in self._lecturers:
            if int(_lecturers.get_staffId().get_staff_id()) > maxID:
                maxID = int(_lecturers.get_staffId().get_staff_id())
        for _departmentSchedulers in self._departmentSchedulers:
            if int(_departmentSchedulers.get_staffId().get_staff_id()) > maxID:
                maxID = int(_departmentSchedulers.get_staffId().get_staff_id())
        for _studentsAffairs in self._studentsAffairs:
            if int(_studentsAffairs.get_staffId().get_staff_id()) > maxID:
                maxID = int(_studentsAffairs.get_staffId().get_staff_id())

        StaffId.changeStaticCounter(maxID)

        logger.info("Staff ID counter changed")

    def startMenu(self):
        logger.info("Start menu opened")
        print("Please choose an option:")
        print("1. Login")
        print("2. Exit")
        choice = input()
        try:
            if choice == "1":
                self.login()
            elif choice == "2":
                logger.info("Program closed")
                print("Goodbye!")
                SystemExit()
            else:
                raise ValueError("User can only choose 1 or 2")
        except Exception as e:
            handle_exception(type(e), e, sys.exc_info()[2])
            print("You can only choose 1 or 2")
            logger.error("Invalid choice")
            self.startMenu()  # Tekrar başlangıç menüsünü çağır
    def showUserInformation(self):
        logger.info("User information shown")
        print("Name: " + self.user.getUserInformation().get_FIRST_NAME())
        print("Surname: " + self.user.getUserInformation().get_LAST_NAME())
        print("Email: " + self.user.getUserInformation().get_email())
        print("Phone Number: " + self.user.getUserInformation().get_phone_number())
        print("Address: " + self.user.getUserInformation().get_address())

    def updateUserInfo(self):
        logger.info("User information can be updated")
        print("Please enter the information you would like to update:")
        print("1. Change password")
        print("2. Change email")
        print("3. Change address")
        print("4. Change phone number")
        print("5. Exit")
        choice = input()
        try:
            if choice == "1":
                self.changePassword()
            elif choice == "2":
                self.changeEmail()
            elif choice == "3":
                self.changeAddress()
            elif choice == "4":
                self.changePhoneNumber()
            elif choice == "5":
                print("Returning to main menu")
                self.startMenu()
            else:
                raise ValueError("User can only choose 1, 2, 3, 4 or 5")
        except Exception as e:
            handle_exception(type(e), e, sys.exc_info()[2])
            print("You can only choose 1, 2, 3, 4 or 5")
            logger.error("Invalid choice")
            self.updateUserInfo()

    def studentMainMenu(self):
        logger.info("Student main menu opened")
        print("Please choose an option:")
        print("1. Register for a course")
        print("2. Show current courses")
        print("3. Show transcript")
        print("4. Update user information")
        print("5. Show user information")
        print("6. Logout")
        choice = input()
        try:
            if choice == "1":
                print("Please choose a course to register:")
                courseList = []
                for course in self._courses:
                    if course.courseInformation not in self.user.get_current_courses():
                        courseList.append(course)
                print("Courses available to register: ")
                for course in courseList:
                    print(course.getCourseName())
                courseTaken = False
                while not courseTaken:
                    courseName = input()
                    if courseName == "exit":
                        print("Exiting course registration")
                        break
                    for course in courseList:
                        if course.getCourseName() == courseName:
                            self.user.takeCourse(course, self._course_registration_service)
                            courseTaken = True
                            break
                    if courseTaken:
                        break

                    print("Invalid course name. Please try again. Type exit if you want to exit.")
                logger.info("Course registered")
            elif choice == "2":
                print("Current courses:")
                for courseInfo in self.user.get_current_courses():
                    print(courseInfo.getCourseCode() + " " + courseInfo.getCourseName())
                    for courseSection in self.coursesNameDict[courseInfo.getCourseName()].getCourseSections():
                        print("Day :" + day_dict[courseSection._day] + " Time " + sectionTime_dict[
                            courseSection._sectionTime])
                logger.info("Current courses shown")
            elif choice == "3":
                print(
                    "Transcript for student " + self.user.getUserInformation().get_FIRST_NAME() + " " + self.user.getUserInformation().get_LAST_NAME())
                print("GPA:", self.user.getTranscript().get_GPA())
                for takenCourse in self.user.getTranscript().getTakenCourses():
                    print(
                        takenCourse.getCourseInformation().getCourseCode() + ": " + takenCourse.getCourseInformation().getCourseName() + ": " + takenCourse.getCourseScore().name())
                logger.info("Transcript shown")
            elif choice == "4":
                self.updateUserInfo()
            elif choice == "5":
                self.showStudentInfo()
                self.showUserInformation()
            elif choice == "6":
                self.startMenu()
                return
            else:
                raise ValueError("User can only choose 1, 2, 3, 4, 5 or 6")
        except Exception as e:
            handle_exception(type(e), e, sys.exc_info()[2])
            print("You can only choose 1, 2, 3, 4, 5 or 6")
            logger.error("Invalid choice")
            self.studentMainMenu()
        self.studentMainMenu()

    def showStudentInfo(self):

        print("In year: " + str(self.user.getCurrentClass()))
        print("Student ID: " + str(self.user.get_studentID().get_ID()))
        print("Department Name: " + str(self.user.get_studentID().get_departmentID().getDepartmentID()))
        print("Faculty Name: " + str(self.user.get_studentID().get_facultyID().getFacultyName()))
        logger.info("Student information shown")

    def lecturerMainMenu(self):
        logger.info("Lecturer main menu opened")
        print("Please choose an option:")
        print("1. Show user information: ")
        print("2. Update user information: ")
        print("3. Logout")
        choice = input()
        try:
            if choice == "1":
                self.showUserInformation()
            elif choice == "2":
                self.updateUserInfo()
            elif choice == "3":
                self.startMenu()
                return
            else:
                raise ValueError("User can only choose 1, 2 or 3")
        except Exception as e:
            handle_exception(type(e), e, sys.exc_info()[2])
            print("You can only choose 1, 2 or 3")
            logger.error("Invalid choice")
            self.lecturerMainMenu()
        self.lecturerMainMenu()

    def advisorMainMenu(self):
        logger.info("Advisor main menu opened")
        print("Please choose an option:")
        print("1. Check request of course request")
        print("2. Show user information")
        print("3. Update user information")
        print("4. Logout")
        choice = input()
        try:
            if choice == "1":
                self.checkRegistration(self.user, self._course_registration_service)
            elif choice == "2":
                self.showUserInformation()
            elif choice == "3":
                self.updateUserInfo()
            elif choice == "4":
                self.startMenu()
                return
            else:
                raise ValueError("User can only choose 1, 2, 3 or 4")
        except Exception as e:
            handle_exception(type(e), e, sys.exc_info()[2])
            print("You can only choose 1, 2, 3 or 4")
            logger.error("Invalid choice")
            self.advisorMainMenu()
        self.advisorMainMenu()

    def checkSectionConflict(self, courseSections, coursesInformations):
        logger.info("Checking section conflict")
        for courseSection in courseSections:
            for courseInformation in coursesInformations:
                for courseSection1 in self.coursesNameDict[courseInformation.getCourseName()].getCourseSections():
                    try:
                        if courseSection._day == courseSection1._day and courseSection._sectionTime == courseSection1._sectionTime:
                            raise ValueError("Student is already taking a course at this time. ")
                    except Exception as e:
                        handle_exception(type(e), e, sys.exc_info()[2])
                        print("Student is already taking a course at this time.")
                        logger.error("Student is already taking a course at this time.")
                        return False
        return True

    def checkRegistration(self, advisor, course_registration_service):
        logger.info("Checking course registration")
        courseRequests = course_registration_service.checkAccesiableRequests(advisor)

        if courseRequests is None:
            print("There is no requests")
            return
        for courseRequest in courseRequests:
            print(
                courseRequest.get_student().getUserInformation().get_FIRST_NAME() + " " + courseRequest.get_course().getCourseName())
            x = advisor.checkCourseRequest(courseRequest)

            if courseRequest.get_course().getCurrentStudentCount() >= courseRequest.get_course().getCourseCapacity():
                print("Course is full. Course request denied.")
                course_registration_service.removeCourseRequest(courseRequest)
                continue
            if self.checkSectionConflict(courseRequest.get_course().getCourseSections(),
                                         courseRequest.get_student().get_current_courses()):
                print("Student doesn't have any courses at this time.")

            if x[0] and x[1] and x[2] and x[3]:
                print("Student is qualified for this course.")
            else:
                print("Student is not qualified for this course. Because of conditions: ")
                if not x[0]: print("Year condition");
                if not x[1]: print("Department condition");
                if not x[2]: print("Faculty condition");
                if not x[3]: print("Prerequisites condition");

            while True:
                print("Do you want to approve the course request? (Y/N)")
                choice = input()
                if choice == "Y" or choice == "y":
                    advisor.approveCourseRequest(courseRequest)
                    self._data_management.createOrChangeStudent(courseRequest.get_student())
                    print("Course request approved")
                    break
                elif choice == "N" or choice == "n":
                    print("Course request denied")
                    break
                else:
                    print("Invalid choice. Please try again.")

            course_registration_service.removeCourseRequest(courseRequest)
        logger.info("All requests checked")
        print("All requests checked")

    def adminMainMenu(self):
        logger.info("Admin main menu opened")
        print("Please choose an option:")
        print("1. Add a new student")
        print("2. Add a new randomly generated student")
        print("3. Remove a student")
        print("4. Logout")

        choice = input()
        try:
            if choice == "1":
                userInformation = self.adminCreateUserInformation()
                print("Please choose a department:")
                for department in self._departments:
                    print(department.getDepartmentID().getDepartmentName())

                department = None

                while (True):
                    department_name = input()
                    for d in self._departments:
                        if d.getDepartmentID().getDepartmentName() == department_name:
                            department = d
                            break
                    if department is not None:
                        break

                    print("Invalid department name. Please try again.")

                print("Enter entrance date:")
                while True:
                    try:
                        entrance_date = int(input())
                        break
                    except ValueError:
                        print("Invalid entrance date. Please try again.")

                print("Enter entrance rank:")
                while True:
                    try:
                        entrance_rank = int(input())
                        break
                    except ValueError:
                        print("Invalid entrance rank. Please try again.")

                print("Select a advisor: ")
                for advisor in self._advisors:
                    print(
                        advisor.getUserInformation().get_FIRST_NAME() + " " + advisor.getUserInformation().get_LAST_NAME())

                advisorID = None

                while True:
                    advisor_name = input()
                    for ad in self._advisors:
                        if ad.getUserInformation().get_FIRST_NAME() + " " + ad.getUserInformation().get_LAST_NAME() == advisor_name:
                            advisorID = ad.get_staffId()
                            break
                    if advisorID is not None:
                        break
                print("Invalid advisor name. Please try again.")

                student = DataManagement.generateNonRandomStudent(userInformation, department, entrance_date,
                                                                  entrance_rank,
                                                                  advisorID)
                self._data_management.createOrChangeStudent(student)
                self._students.append(student)
                self._login_auth_service._users.append(student)
                print(
                    "Student" + student.getUserInformation().get_FIRST_NAME() + " " + student.getUserInformation().get_LAST_NAME() + " added successfully.")

            elif choice == "2":
                d = random.choice(self._departments)
                entranceRank = int(random.random() * 1000)

                while True:
                    found = False
                    for s in self._students:
                        if s.get_studentID().get_entrance_rank() == entranceRank and s.get_studentID().get_entrance_rank() == 2024:
                            found = True
                            break
                    if not found:
                        break
                    entranceRank = int(random.random() * 1000)

                advisorID2 = random.choice(self._advisors).get_staffId()
                entranceDate = random.choice([2024, 2023, 2022, 2021])

                student2 = DataManagement.generateRandomStudent(d, entranceDate, entranceRank, advisorID2)
                self._data_management.createOrChangeStudent(student2)
                self._students.append(student2)
                self._login_auth_service._users.append(student2)
                print(
                    "Student" + student2.getUserInformation().get_FIRST_NAME() + " " + student2.getUserInformation().get_LAST_NAME() + " added successfully.")

            elif choice == "3":
                print("Please choose a student to remove:")
                for student1 in self._students:
                    # get_UNIVERSITY_EMAIL çalışmıyor(get'i silince çalışıyor)
                    print(student1.getUserInformation().get_UNIVERSITY_EMAIL())

                student_email = input()
                studentExists = False

                for student1 in self._students:
                    if student1.getUserInformation().get_UNIVERSITY_EMAIL() == student_email:
                        self._students.remove(student1)
                        self._login_auth_service._users.remove(student1)
                        self._data_management.removeStudent(student1)
                        print(
                            "Student " + student1.getUserInformation().get_FIRST_NAME() + " " + student1.getUserInformation().get_LAST_NAME() + " removed successfully.")
                        studentExists = True
                        break

                if not studentExists:
                    print("Student not found.")


            elif choice == "4":
                self.startMenu()
                return
            else:
                raise ValueError("User can only choose 1, 2, 3 or 4")
        except Exception as e:
            handle_exception(type(e), e, sys.exc_info()[2])
            print("You can only choose 1, 2, 3 or 4")
            logger.error("Invalid choice")
            self.adminMainMenu()
        self.adminMainMenu()

    def departmentHeadMainMenu(self):
        logger.info("Department head main menu opened")
        print("Please choose an option:")
        print("1. Change course section quota")
        print("2. Show user information")
        print("3. Update user information")
        print("4. Logout")
        choice = input()
        try:
            if choice == "1":
                print("Select department to continue")
                for department in self._departments:
                    print(department.getDepartmentID().getDepartmentName())

                department = None
                while True:
                    departmentSelection = input()
                    found = False
                    for d in self._departments:
                        if departmentSelection == d.getDepartmentID().getDepartmentName():
                            department = d
                            found = True
                            break
                    if found:
                        break
                print("Select course to continue")
                coursesForThisDepartment = []
                for c in self._courses:
                    if c.getCourseRequirements().getDepartmentID() == department.getDepartmentID().getDepartmentID():
                        coursesForThisDepartment.append(c)
                        print(c.getCourseName())

                course = None
                while True:
                    courseSelection = input()
                    found = False
                    for c in coursesForThisDepartment:
                        if c.getCourseName() == courseSelection:

                            found = True
                            course = c
                            break
                    if found:
                        break

                if len(course.getCourseSections()) == 0:

                    print("There are no sections for this course")
                    return

                # course kotasını değiş
                maxCapacity = int(1e9)
                for courseSection in course.getCourseSections():
                    maxCapacity = min(maxCapacity, courseSection._quota)
                print(f"Select new quota for course {course.getCourseName()}. Current course quota is {course.getCourseCapacity()}. Maximum quota for a section is {maxCapacity}")
                newCapacity = 0
                while True:
                    try:
                        inp = int(input())
                        if inp > maxCapacity:
                            print("Invalid quota. Please try again.")
                            continue
                        newCapacity = inp
                        break
                    except ValueError:
                        newCapacity = course.getCourseCapacity()
                        break

                course._courseCapacity = newCapacity

                self._data_management.createOrChangeCourse(course)
                print("Course section quota changed successfully")

            elif choice == "2":
                self.showUserInformation()
            elif choice == "3":
                self.updateUserInfo()
            elif choice == "4":
                self.startMenu()
                return
            else:
                raise ValueError("User can only choose 1, 2, 3 or 4")
        except Exception as e:
            handle_exception(type(e), e, sys.exc_info()[2])
            print("You can only choose 1, 2, 3 or 4")
            logger.error("Invalid choice")
            self.departmentHeadMainMenu()
        self.departmentHeadMainMenu()

    def adminCreateUserInformation(self):
        logger.info("Admin creating user information")
        print("Enter first name: ")
        first_name = input()
        print("Enter last name: ")
        last_name = input()
        university_email = DataManagement.__generateUniversityEmail(first_name, last_name)
        print("Created university email: " + university_email)
        print("Enter email: ")
        email = input()
        print("Enter address (City only): ")
        address = input()
        print("Enter phone number: ")
        phone_number = input()
        print("Enter password: ")
        password = input()
        return UserInformation(first_name, last_name, university_email, email, address, phone_number, password)

    def departmentSchedulerMainMenu(self):
        logger.info("Department scheduler main menu opened")
        print("Please choose an option:")
        print("1. Change course section")
        print("2. Show user information")
        print("3. Update user information")
        print("4. Logout")
        choice = input()
        try:
            if choice == "1":
                print("Select department to continue")
                for department in self._departments:
                    print(department.getDepartmentID().getDepartmentName())

                department = None
                while True:
                    departmentSelection = input()
                    found = False
                    for d in self._departments:
                        if departmentSelection == d.getDepartmentID().getDepartmentName():
                            department = d
                            found = True
                            break
                    if found:
                        break
                print("Select course to continue")
                coursesForThisDepartment = []
                for c in self._courses:
                    if c.getCourseRequirements().getDepartmentID() == department.getDepartmentID().getDepartmentID():
                        coursesForThisDepartment.append(c)
                        print(c.getCourseName())

                course = None
                while True:
                    courseSelection = input()
                    found = False
                    for c in coursesForThisDepartment:
                        if c.getCourseName() == courseSelection:
                            found = True
                            course = c
                            break
                    if found:
                        break

                # getCourseSections çalışmıyor
                if len(course.getCourseSections()) == 0:
                    print("There are no sections for this course")
                    return

                for courseSection in course.getCourseSections():
                    print("This course section is in day " + day_dict[courseSection._day] + " time " + sectionTime_dict[
                        courseSection._sectionTime])
                    print("Do you want to change this section? Yes if continue: ")
                    choice = input()
                    if not choice == "Yes" or choice == "yes":
                        continue
                    while True:
                        x = True
                        print("Enter the day(Monday, Tuesday, Wednesday, Thursday, Friday): ")
                        inp = input()
                        if inp.lower() == "monday":
                            print("This section day changed to Monday")
                            courseSection._day = Day.Monday
                        elif inp.lower() == "tuesday":
                            print("This section day changed to Tuesday")
                            courseSection._day = Day.Tuesday
                        elif inp.lower() == "wednesday":
                            print("This section day changed to Wednesday")
                            courseSection._day = Day.Wednesday
                        elif inp.lower() == "thursday":
                            print("This section day changed to Thursday")
                            courseSection._day = Day.Thursday
                        elif inp.lower() == "friday":
                            print("This section day changed to Friday")
                            courseSection._day = Day.Friday
                        else:
                            x = False
                            print("Invalid day. Please try again.")

                        if x: break

                    while True:
                        x = True
                        print(
                            "Enter the section time(First, Second, Third,Fourth, Fifth, Sixth, Seventh, Eighth, Ninth)")
                        inp = input()
                        if inp.lower() == "first":
                            print("This section time changed to First")
                            courseSection._sectionTime = SectionTime.First
                        elif inp.lower() == "second":
                            print("This section time changed to Second")
                            courseSection._sectionTime = SectionTime.Second
                        elif inp.lower() == "third":
                            print("This section time changed to Third")
                            courseSection._sectionTime = SectionTime.Third
                        elif inp.lower() == "fourth":
                            print("This section time changed to Fourth")
                            courseSection._sectionTime = SectionTime.Fourth
                        elif inp.lower() == "fifth":
                            print("This section time changed to Fifth")
                            courseSection._sectionTime = SectionTime.Fifth
                        elif inp.lower() == "sixth":
                            print("This section time changed to Sixth")
                            courseSection._sectionTime = SectionTime.Sixth
                        elif inp.lower() == "seventh":
                            print("This section time changed to Seventh")
                            courseSection._sectionTime = SectionTime.Seventh
                        elif inp.lower() == "eighth":
                            print("This section time changed to Eighth")
                            courseSection._sectionTime = SectionTime.Eighth
                        elif inp.lower() == "ninth":
                            print("This section time changed to Ninth")
                            courseSection._sectionTime = SectionTime.Ninth
                        else:
                            x = False
                            print("Invalid time. Please try again.")

                        if x: break

                self._data_management.createOrChangeCourse(course)
                print("Course section changed successfully")

            elif choice == "2":
                self.showUserInformation()
            elif choice == "3":
                self.updateUserInfo()
            elif choice == "4":
                self.startMenu()
                return
            else:
                raise ValueError("User can only choose 1, 2, 3 or 4")
        except Exception as e:
            handle_exception(type(e), e, sys.exc_info()[2])
            print("You can only choose 1, 2, 3 or 4")
            logger.error("Invalid choice")
            self.departmentSchedulerMainMenu()
        self.departmentSchedulerMainMenu()

    def studentsAffairsMainMenu(self):
        logger.info("Students affairs main menu opened")
        print("Please choose an option:")
        print("1. Add new course")
        print("2. Remove course")
        print("3. Show user information")
        print("4. Update user information")
        print("5. Logout")
        choice = input()
        try:
            if choice == "1":
                self.studentsAffairsAddCourseMenu()

            elif choice == "2":
                print("Enter a course name to remove: ")
                cName = input()
                x = False
                for c in self._courses:
                    if c.getCourseName() == cName:
                        self._data_management.removeCourse(c)
                        self._courses.remove(c)
                        print("Course " + cName + " removed successfully.")
                        x = True
                if not x:
                    print("Course not found.")

            elif choice == "3":
                self.showUserInformation()
            elif choice == "4":
                self.updateUserInfo()
            elif choice == "5":
                self.startMenu()
                return
            else:
                raise ValueError("User can only choose 1, 2, 3, 4 or 5")
        except Exception as e:
            handle_exception(type(e), e, sys.exc_info()[2])
            print("You can only choose 1, 2, 3, 4 or 5")
            logger.error("Invalid choice")
            self.studentsAffairsMainMenu()
        self.studentsAffairsMainMenu()

    def studentsAffairsAddCourseMenu(self):
        print("Enter course name: ")
        course_name = input()
        print("Enter course code: ")
        course_code = input()
        min_current_class = 0
        while True:
            print("Enter minimum current class requirement: ")
            try:
                min_current_class = int(input())
                break
            except ValueError:
                print("Invalid minimum current class. Please try again.")

        print(
            "If your course has a department requirement, enter the department name. If not, enter anything: ")
        for department in self._departments:
            print(department.getDepartmentID().getDepartmentName())
        inp = input()
        department = None
        for d in self._departments:
            if d.getDepartmentID().getDepartmentName() == inp:
                department = d
                break

        if department is None:
            department = Department(DepartmentID(0, "No Department"), FacultyID(0, "No Faculty"))

        print("Enter all the prerequisites for this course. When you are finished, type 'finished'")
        for course in self._courses:
            print(course.getCourseName())
        prerequisites = []
        while True:
            inp = input()
            for course in self._courses:
                if course.getCourseName() is inp:
                    prerequisites.append(course.getCourseInformation())
                    break
            if inp == "finished":
                break
        # niye unreachable
        print("Enter the number of sections for this course: ")

        section_number = 0
        while True:
            try:
                section_number = int(input())
                break
            except ValueError:
                print("Invalid section number. Please try again.")

        lecturerArrayList = []
        print("Select a lecturer for this course: ")
        for lecturer in self._lecturers:
            print(
                lecturer.getUserInformation().get_FIRST_NAME() + " " + lecturer.getUserInformation().get_LAST_NAME())

        current_section = 0
        while current_section < section_number:
            print("Enter lecturer name for section" + str(current_section + 1) + ":")
            lecturer_name = input()
            lecturerExists = False
            for lecturer in self._lecturers:
                if (
                        lecturer.getUserInformation().get_FIRST_NAME() + " " + lecturer.getUserInformation().get_LAST_NAME()) == lecturer_name:
                    lecturerExists = True
                    lecturerArrayList.append(lecturer)
                    break
            if not lecturerExists:
                print("Lecturer not found. Please try again.")
                current_section -= 1
            current_section += 1

        dayArrayList = []
        sectionTimeArrayList = []
        classroomArrayList = []

        print("Days: ")
        print("Monday, Tuesday, Wednesday, Thursday, Friday")

        print("Section Times: ")
        print("First, Second, Third, Fourth, Fifth, Sixth, Seventh, Eighth, Ninth")

        current_section = 0
        while current_section < section_number:
            print("Enter day for section " + str(current_section + 1) + ":")
            day = input()
            day = day.lower()
            dayValue = Day.Monday
            match day:
                case "monday":
                    dayArrayList.insert(current_section, Day.Monday)
                    dayValue = Day.Monday
                case "tuesday":
                    dayArrayList.insert(current_section, Day.Tuesday)
                    dayValue = Day.Tuesday
                case "wednesday":
                    dayArrayList.insert(current_section, Day.Wednesday)
                    dayValue = Day.Wednesday
                case "thursday":
                    dayArrayList.insert(current_section, Day.Thursday)
                    dayValue = Day.Thursday
                case "friday":
                    dayArrayList.insert(current_section, Day.Friday)
                    dayValue = Day.Friday
                case _:
                    print("Invalid day. Please try again.")
                    continue

            print("Enter section time for section " + str(current_section + 1) + ": ")
            sectionTime = input()
            sectionTime = sectionTime.lower()
            sectionTimeValue = SectionTime.First
            match sectionTime:
                case "first":
                    sectionTimeArrayList.insert(current_section, SectionTime.First)
                    sectionTimeValue = SectionTime.First
                case "second":
                    sectionTimeArrayList.insert(current_section, SectionTime.Second)
                    sectionTimeValue = SectionTime.Second
                case "third":
                    sectionTimeArrayList.insert(current_section, SectionTime.Third)
                    sectionTimeValue = SectionTime.Third
                case "fourth":
                    sectionTimeArrayList.insert(current_section, SectionTime.Fourth)
                    sectionTimeValue = SectionTime.Fourth
                case "fifth":
                    sectionTimeArrayList.insert(current_section, SectionTime.Fifth)
                    sectionTimeValue = SectionTime.Fifth
                case "sixth":
                    sectionTimeArrayList.insert(current_section, SectionTime.Sixth)
                    sectionTimeValue = SectionTime.Sixth
                case "seventh":
                    sectionTimeArrayList.insert(current_section, SectionTime.Seventh)
                    sectionTimeValue = SectionTime.Seventh
                case "eighth":
                    sectionTimeArrayList.insert(current_section, SectionTime.Eighth)
                    sectionTimeValue = SectionTime.Eighth
                case "ninth":
                    sectionTimeArrayList.insert(current_section, SectionTime.Ninth)
                    sectionTimeValue = SectionTime.Ninth
                case _:
                    print("Invalid section time. Please try again.")
                    continue

            allAvailableClassrooms = []
            for classroom in self._classrooms:
                if self._course_registration_service.checkClassroomAvailabilityForDayAndTime(dayValue, sectionTimeValue,
                                                                                             classroom, self._courses):
                    allAvailableClassrooms.append(classroom)

            print("Available classrooms for this section: ")
            for classroom in allAvailableClassrooms:
                print(classroom.getClassroomName())

            print("Enter classroom for this section " + str(current_section + 1) + ": ")
            inpClassroom = input()
            inpClassroom = sectionTime.lower()

            classroomExists = False

            for classroom in allAvailableClassrooms:
                if classroom.getClassroomName().lower() == inpClassroom:
                    classroomArrayList.insert(current_section, classroom)
                    classroomExists = True
                    break

            if not classroomExists:
                print("Classroom not found. Please try again.")
                current_section -= 1

            current_section += 1

        course = DataManagement.generateCourse(lecturerArrayList, dayArrayList, sectionTimeArrayList,
                                               course_name,
                                               course_code, prerequisites, min_current_class,
                                               department.get_facultyID(), department.getDepartmentID())
        self._data_management.createOrChangeCourse(course)
        self._courses.append(course)

    def login(self):
        logger.info("Login started")
        print(
            "Which type of user are you? (Student, Advisor, Lecturer, Admin, DepartmentScheduler, StudentsAffairs, DepartmentHead)")
        self.user_type = input()
        print("Enter your university email: ")
        email = input()
        print("Enter your password: ")
        password = input()
        self.user = self._login_auth_service.login(email, password)
        if self.user is None:
            print("None")
            self.user_type = str()

        if self.user_type.lower() == "student":
            self.studentMainMenu()
        elif self.user_type.lower() == "advisor":
            self.advisorMainMenu()
        elif self.user_type.lower() == "lecturer":
            self.lecturerMainMenu()
        elif self.user_type.lower() == "admin":
            self.adminMainMenu()
        elif self.user_type.lower() == "departmentscheduler":
            self.departmentSchedulerMainMenu()
        elif self.user_type.lower() == "studentsaffairs":
            self.studentsAffairsMainMenu()
        elif self.user_type.lower() == "departmenthead":
            self.departmentHeadMainMenu()
        else:
            print("Invalid login. To retry enter 1, to return to the main menu enter any other key")
            inp = input()
            if inp == "1":
                self.login()
            else:
                self.startMenu()

    def changePassword(self):
        logger.info("Password change started")
        print("Enter your current password: ")
        current_password = input()
        print("Enter your new password: ")
        new_password = input()
        if self.user.getUserInformation().changePassword(current_password, new_password):
            print("Password changed successfully.")
        else:
            print("Password update failed. Please try again.")
        logger.info("Password changed")

    def changeEmail(self):
        logger.info("Email change started")
        print("Enter your current password: ")
        current_password = input()
        print("Enter your new email: ")
        new_email = input()

        if self.user.getUserInformation().changeEmail(current_password, new_email):
            print("Email changed successfully.")
        else:
            print("Email update failed. Please try again.")
        logger.info("Email changed")

    def changeAddress(self):
        logger.info("Address change started")
        print("Enter your current password: ")
        current_password = input()
        print("Enter your new address: ")
        new_address = input()

        if self.user.getUserInformation().changeAddress(current_password, new_address):
            print("Address changed successfully.")
        else:
            print("Address update failed. Please try again.")
        logger.info("Address changed")

    def changePhoneNumber(self):
        logger.info("Phone number change started")
        print("Enter your current password: ")
        current_password = input()
        print("Enter your new phone number: ")
        new_phone_number = input()

        if self.user.getUserInformation().changePhoneNumber(current_password, new_phone_number):
            print("Phone number changed successfully.")
        else:
            print("Phone number update failed. Please try again.")
        logger.info("Phone number changed")


# us = DataManagement.__generateRandomUserInformation()
# us1 = DataManagement.__generateRandomUserInformation()
# dep = Department(DepartmentID(0, "Computer Engineering"), FacultyID(0, "Engineering"))
# advisor = DataManagement.generateRandomAdvisor(dep)
# student = DataManagement.generateRandomStudent(dep, 2024, 100, advisor.get_staffId())
# DataManagement.DataManagement().createOrChangeDepartment(dep)
# DataManagement.DataManagement().createOrChangeStudent(student)
# DataManagement.DataManagement().createOrChangeAdvisor(advisor)


if __name__ == '__main__':
    main = Main()
    main.main()
