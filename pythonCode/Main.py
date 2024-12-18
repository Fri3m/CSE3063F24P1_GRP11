from operator import truediv
from warnings import catch_warnings
import random
from pythonCode.Student import Student
from pythonCode.User import StaffId, Admin, User, Advisor
from pythonCode.UserInformation import UserInformation

import Course


class Main:


    user_type = str()

    @staticmethod
    def main(self):
        main: Main
        main.startMenu()


    def __init__(self, _login_auth_service, _data_management, _course_registration_service,_faculties,_departments,_students,_advisors,_lecturers,_departmentSchedulers,_studentsAffairs,_courses,_admin,user,user_type):
        self.user = None
        self._login_auth_service = _login_auth_service
        self._data_management = _data_management
        self._course_registration_service = _course_registration_service

        self._faculties = _data_management.getAllFaculties()
        self._departments = _data_management.getAllDepartments()
        self._students = _data_management.getAllStudents()
        self._advisors = _data_management.getAllAdvisors()
        self._lecturers = _data_management.getAllLecturers()
        self._departmentSchedulers = _data_management.getAllDepartmentSchedulers()
        self._studentsAffairs = _data_management.getAllStudentsAffairs()
        self._courses = _data_management.getAllCourses()

        self.changeStaticStaffID()

        # BUNA SONRA BAK !!!!! (loginauthservice)
        _admin = Admin(UserInformation(("admin"), ("admin"), ("admin"), ("admin"), ("admin"), ("admin"),
                                       _login_auth_service.hash_password("admin")))


        self._users = []
        self._users.extend(self._students)
        self._users.extend(self._advisors)
        self._users.extend(self._lecturers)
        self._users.extend(self._departmentSchedulers)
        self._users.extend(self._studentsAffairs)
        self._users.append(_admin)

        _login_auth_service._user = self._user

        for _departments in self._departments:
            for _lecturers in self._lecturers:
                if _lecturers.get_department_id() is not None and _lecturers.get_department_id().getDepartmentID == _departments.getDepartmentID().getDepartmentID():
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

    def startMenu(self):
        print("Welcome to the Course Registration System")
        print("Please choose an option:")
        print("1. Login")
        print("2. Exit")
        choice = input()
        if choice == "1":
            self.login()
        elif choice == "2":
            SystemExit(0)
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")
            self.startMenu()


    def showUserInformation(self):
        print("Name: " + self.user.getUserInformation().get_FIRST_NAME())
        print("Surname: " + self.user.getUserInformation().get_LAST_NAME())
        print("Email: " + self.user.getUserInformation().get_email())
        print("Phone Number: " + self.user.getUserInformation().get_phone_number())
        print("Address: " + self.user.getUserInformation().get_address())


    def updateUserInfo(self):
        print ("Please enter the information you would like to update:")
        print ("1. Change password")
        print ("2. Change email")
        print ("3. Change address")
        print ("4. Change phone number")
        print ("5. Exit")
        choice = input()
        if choice == "1":
            self.changePassword()
        elif choice == "2":
            self.changeEmail()
        elif choice == "3":
            self.changeAddress()
        elif choice == "4":
            self.changePhoneNumber()
        elif choice == "5":
            print ("Returning to main menu")
            self.startMenu()
        else:
            print ("Invalid choice. Please try again.")

        self.updateUserInfo()

    def studentMainMenu(self):

        print("Please choose an option:")
        print("1. Register for a course")
        print("2. Show current courses")
        print("3. Show transcript")
        print("4. Update user information")
        print("5. Show user information")
        print("6. Logout")

        choice = input()
        if choice == "1":
            print("Please choose a course to register:")
            courseList = []
            for course in self._courses:
                isInIt = False
                for currentCourse in self.user.get_current_courses():
                    if currentCourse.getCourseInformation().getCourseCode().equals(course.getCourseInformation().getCourseCode()):
                        isInIt = True
                        break

                if(not isInIt):
                    courseList.append(course)

            for course in courseList:
                print(course.getCourseName())

            courseName = input()

            for course in courseList:
                if course.getCourseName() == courseName:
                    self.user.take_course(course, self._course_registration_service)
                    break


        elif choice == "2":

            print("Current courses:")
            for course in self.user.get_current_courses():
                print(course.getCourseInformation().getCourseCode() + " " + course.getCourseName())
                for courseSection in course.getCourseSections():
                    print("Day :" + courseSection._day.name() + " Time " + courseSection._sectionTime.name())

        elif choice == "3":
            # GetUserInformation çalışmıyor!!!  (studentten dolayı olabilir)
            print ("Transcript for student " + self.user.getUserInformation().get_FIRST_NAME() + " " + self.user.getUserInformation().get_LAST_NAME())
            print("GPA: " + self.user.get_transcript().get_gpa())
            for takenCourse in self.user.get_transcript().get_taken_courses():
                print(takenCourse.getCourseInformation().getCourseCode() + ": " + takenCourse.getCourseInformation().getCourseName()+ ": " + takenCourse.getCourseScore().name())

        elif choice == "4":
            self.updateUserInfo()

        elif choice == "5":
            self.showStudentInfo()
            self.showUserInformation()

        elif choice == "6":
            self.startMenu()
            return
        else:
            print("Invalid choice. Please try again.")

        self.studentMainMenu()

    def showStudentInfo(self):

        print("In year: " + self.user.get_current_class())
        print("Student ID: " + self.user.get_student_id().get_id())
        print("Department Name: " + self.user.get_student_id().get_department_id().getDepartmentId())
        print("Faculty Name: " + self.user.get_student_id().get_faculty_id().getFacultyName())

    def lecturerMainMenu(self):
        print("Please choose an option:")
        print("1. Show user information: ")
        print("2. Update user information: ")
        print("3. Logout")
        choice = input()
        if choice == "1":
            self.showUserInformation()
        elif choice == "2":
            self.updateUserInfo()
        elif choice == "3":
            self.startMenu()
            return
        else:
            print("Invalid choice. Please try again.")

        self.lecturerMainMenu()

    def advisorMainMenu(self):

        print("Please choose an option:")
        print("1. Check request of course request")
        print("2. Show user information")
        print("3. Update user information")
        print("4. Logout")
        choice = input()

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
            print("Invalid choice. Please try again.")

        self.advisorMainMenu()

    def checkRegistration (self, advisor, course_registration_service):
        courseRequests = course_registration_service.checkAccesiableRequests(advisor)

        if courseRequests is None:
            print("There is no requests")
            return
        for courseRequest in courseRequests:
            print(courseRequest.get_student().getUserInformation().get_FIRST_NAME() + " " + courseRequest.get_course().getCourseName())
            x = advisor.checkCourseRequest(courseRequest)
            if x[0] and x[1] and x[2] and x[3]:
                print("Student is qualified for this course.")
            else:
                print("Student is not qualified for this course. Because of conditions: ")
                if not x[0]: print("Year condition");
                if not x[1]: print("Department condition");
                if not x[2]: print("Faculty condition");
                if not x[3]: print("Prerequisites condition");

            print("Do you want to approve the course request? (Y/N)")
            choice = input()
            if choice == "Y" or choice == "y":
                advisor.approveCourseRequest(courseRequest)
                self._data_management.createOrChangeStudent(courseRequest.get_student())
                print("Course request approved")
            elif choice == "N" or choice == "n":
                print("Course request denied")
            else:
                print("Invalid choice. Please try again.")

            course_registration_service.removeCourseRequest(courseRequest)

        print("All requests checked")

    def adminMainMenu(self):
        print("Please choose an option:")
        print("1. Add a new student")
        print("2. Add a new randomly generated student")
        print("3. Remove a student")
        print("4. Logout")

        choice = input()
        if choice == "1":
            userInformation = self.adminCreateUserInformation()
            print("Please choose a department:")
            for department in self._departments:
                print(department.getDepartmentID().getDepartmentName())

            department = None

            while(True):
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
                print(advisor.getUserInformation().get_FIRST_NAME() + " " + advisor.getUserInformation().get_LAST_NAME())

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

            student = self._data_management.generateNonRandomStudent(userInformation, department, entrance_date, advisorID)
            self._data_management.createOrChangeStudent(student)
            self._students.append(student)
            self._login_auth_service._users.append(student)
            print("Student" + student.getUserInformation().get_FIRST_NAME() + " " + student.getUserInformation().get_LAST_NAME() + " added successfully.")

        elif choice == "2":
            d = self._departments.get((int) (random.random() * len(self._departments)))
            entranceRank = (int) (random.random() * 1000)

            while True:
                found = False
                for s in self._students:
                    if s.get_student_id().get_entrance_rank() == entranceRank and s.get_student_id().get_entrance_rank() == 2024 :
                        found = True
                        break
                if not found:
                    break
                entranceRank = (int) (random.random() * 1000)

            advisorID2 = self._advisors.get((int) (random.random() * len(self._advisors))).get_staffId()
            student2 = self._data_management.generateRandomStudent(d, 2024, entranceRank, advisorID2)
            self._data_management.createOrChangeStudent(student2)
            self._students.append(student2)
            self._login_auth_service._users.append(student2)
            print("Student" + student2.getUserInformation().get_FIRST_NAME() + " " + student2.getUserInformation().get_LAST_NAME() + " added successfully.")

        elif choice == "3":
            print("Please choose a student to remove:")
            for student1 in self._students:
                #get_UNIVERSITY_EMAIL çalışmıyor(get'i silince çalışıyor)
                print(student1.getUserInformation().get_UNIVERSITY_EMAIL())

            student_email = input()
            studentExists = False

            for student1 in self._students:
                if student1.getUserInformation().get_UNIVERSITY_EMAIL() == student_email:
                    self._students.remove(student1)
                    self._login_auth_service._users.remove(student1)
                    self._data_management.removeStudent(student1)
                    print("Student " + student1.getUserInformation().get_FIRST_NAME() + " " + student1.getUserInformation().get_LAST_NAME() + " removed successfully.")
                    studentExists = True
                    break

            if not studentExists:
                print("Student not found.")


        elif choice == "4":
            self.startMenu()
            return
        else:
            print("Invalid choice. Please try again.")

        self.adminMainMenu()

    def adminCreateUserInformation(self):
        print("Enter first name: ")
        first_name = input()
        print("Enter last name: ")
        last_name = input()
        university_email = self._data_management.generateUniversityEmail(first_name, last_name)
        print("Created university email: " + university_email)
        print("Enter email: ")
        email = input()
        print("Enter address (City only): ")
        address = input()
        print("Enter phone number: ")
        phone_number = input()
        print("Enter password: ")
        password = input()
        return UserInformation(first_name, last_name, university_email,email, address,phone_number, self._login_auth_service.hashPassword(password))

    def departmentSchedulerMainMenu(self):
        print("Please choose an option:")
        print("1. Change course section")
        print("2. Show user information")
        print("3. Update user information")
        print("4. Logout")
        choice = input()
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
                if c.getCourseRequirements().get_departmentID().getDepartmentID() == department.getDepartmentID().getDepartmentID():
                    coursesForThisDepartment.append(c)
                    print(c.getCourseName())

            course = None
            while True:
                courseSelection = input()
                found = False
                for c in coursesForThisDepartment:
                    if c.getCourseName == courseSelection:
                        found = True
                        course = c
                        break
                if found:
                    break

            #getCourseSections çalışmıyor
            if len(course.getCourseSections())==0:
                print("There are no sections for this course")
                return

            for courseSection in course.getCourseSections():
                print("This course section is in day " + courseSection._day + " time " +courseSection._sectionTime)
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

                    if x : break

                while True :
                    x = True
                    print("Enter the section time(First, Second, Third,Fourth, Fifth, Sixth, Seventh, Eighth, Ninth)")
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
            print("Invalid choice. Please try again.")

        self.departmentSchedulerMainMenu()

    def studentsAffairsMainMenu(self):
        print("Please choose an option:")
        print("1. Add new course")
        print("2. Remove course")
        print("3. Show user information")
        print("4. Update user information")
        print("5. Logout")
        choice = input()
        if choice == "1":
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

            print("If your course has a department requirement, enter the department name. If not, enter anything: ")
            for department in self._departments:
                print(department.getDepartmentID().getDepartmentName())
            inp= input()
            department = None
            for d in self._departments:
                if d.getDepartmentID().getDepartmentName() == inp:
                    department = d
                    break

            if department is None:
                department = Department (DepartmentID(0,"No Department"), FacultyID(0,"No Faculty"))

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
                if inp is "finished":
                    break
            #niye unreachable
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
                print(lecturer.getUserInformation().get_FIRST_NAME() + " " + lecturer.getUserInformation().get_LAST_NAME())
            for i in range(section_number):
                print("Enter lecturer name for section" + str(i+1) + ":")
                lecturer_name = input()
                lecturerExists = False
                for lecturer in self._lecturers:
                    if (lecturer.getUserInformation().get_FIRST_NAME() + " " + lecturer.getUserInformation().get_LAST_NAME()) == lecturer_name:
                        lecturerExists = True
                        lecturerArrayList.append(lecturer)
                        break
                if not lecturerExists:
                    print("Lecturer not found. Please try again.")
                    i -= 1

            dayArrayList = []
            sectionTimeArrayList = []
            print("Days: ")
            for d in Day.values():
                print(d.name()+", ")
            print()

            print("Section Times: ")

            for i in range(section_number):
                print("Enter day for section "+ str(i+1) + ":")
                day =input()

                if day.lower() == "monday":
                    dayArrayList.append(Day.Monday)
                elif day.lower() == "tuesday":
                    dayArrayList.append(Day.Tuesday)
                elif day.lower() == "wednesday":
                    dayArrayList.append(Day.Wednesday)
                elif day.lower() == "thursday":
                    dayArrayList.append(Day.Thursday)
                elif day.lower() == "friday":
                    dayArrayList.append(Day.Friday)
                else:
                    print("Invalid day. Please try again.")
                    i -= 1
                    continue

                print("Enter section time for section " + str(i + 1) + ": ")
                sectionTime = input()

                if sectionTime.lower() == "first":
                    sectionTimeArrayList.append(SectionTime.First)
                elif sectionTime.lower() == "second":
                    sectionTimeArrayList.append(SectionTime.Second)
                elif sectionTime.lower() == "third":
                    sectionTimeArrayList.append(SectionTime.Third)
                elif sectionTime.lower() == "fourth":
                    sectionTimeArrayList.append(SectionTime.Fourth)
                elif sectionTime.lower() == "fifth":
                    sectionTimeArrayList.append(SectionTime.Fifth)
                elif sectionTime.lower() == "sixth":
                    sectionTimeArrayList.append(SectionTime.Sixth)
                elif sectionTime.lower() == "seventh":
                    sectionTimeArrayList.append(SectionTime.Seventh)
                elif sectionTime.lower() == "eighth":
                    sectionTimeArrayList.append(SectionTime.Eighth)
                elif sectionTime.lower() == "ninth":
                    sectionTimeArrayList.append(SectionTime.Ninth)
                else:
                    print("Invalid section time. Please try again.")
                    i -= 1

            course = self._data_management.generateCourse(lecturerArrayList, dayArrayList, sectionTimeArrayList, course_name, course_code, prerequisites, min_current_class, department.get_facultyID(), department.getDepartmentID())
            self._data_management.createOrChangeCourse(course)
            self._courses.append(course)

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
            print("Invalid choice. Please try again.")

        self.studentsAffairsMainMenu()

    def login(self):
        print("Which type of user are you? (Student, Advisor, Lecturer, Admin, DepartmentScheduler, StudentAffair)")
        user_type = input()
        print("Enter your university email: ")
        email = input()
        print("Enter your password: ")
        password = input()

        self.user = self._login_auth_service.login(email,password)
        if self.user is None:
            user_type = None

        if user_type.lower() == "student":
            self.studentMainMenu()
        elif user_type.lower() == "advisor":
            self.advisorMainMenu()
        elif user_type.lower() =="lecturer":
            self.lecturerMainMenu()
        elif user_type.lower() == "admin":
            self.adminMainMenu()
        elif user_type.lower() == "departmentScheduler":
            self.departmentSchedulerMainMenu()
        elif user_type.lower() == "studentsAffairs":
            self.studentsAffairsMainMenu()
        else:
            print("Invalid login. To retry enter 1, to return to the main menu enter any other key")
            inp = input()
            if inp == "1":
                self.login()
            else:
                self.startMenu()

    def changePassword(self):
        print("Enter your current password: ")
        current_password = input()
        print("Enter your new password: ")
        new_password = input()


        if self.user.getUserInformation().changePassword(self._login_auth_service.hashPassword(current_password), self._login_auth_service.hashPassword(new_password)):
            print("Password changed successfully.")
        else:
            print("Password update failed. Please try again.")

    def changeEmail(self):
        print("Enter your current password: ")
        current_password = input()
        print("Enter your new email: ")
        new_email = input()

        if self.user.getUserInformation().changeEmail(self._login_auth_service.hashPassword(current_password), new_email):
            print("Email changed successfully.")
        else:
            print("Email update failed. Please try again.")

    def changeAddress(self):
        print("Enter your current password: ")
        current_password = input()
        print("Enter your new address: ")
        new_address = input()

        if self.user.getUserInformation().changeAddress(self._login_auth_service.hashPassword(current_password), new_address):
            print("Address changed successfully.")
        else:
            print("Address update failed. Please try again.")

    def changePhoneNumber(self):
        print("Enter your current password: ")
        current_password = input()
        print("Enter your new phone number: ")
        new_phone_number = input()

        if self.user.getUserInformation().changePhoneNumber(self._login_auth_service.hashPassword(current_password), new_phone_number):
            print("Phone number changed successfully.")
        else:
            print("Phone number update failed. Please try again.")
