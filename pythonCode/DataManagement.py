import json
import os
import random
from json import JSONEncoder

from Classroom import Classroom
from Course import CourseInformation, CourseRequirements, CourseSection, Course
from Day import Day, SectionTime

from Department import DepartmentID, Department
from Faculty import FacultyID, Faculty
from User import Lecturer, Advisor, DepartmentScheduler, StudentsAffairs, DepartmentHead

from pythonCode.UserInformation import UserInformation
from pythonCode.Student import StudentID, Student
from pythonCode.Transcript import Transcript
import logging

from pythonCode.Logger import setup_logger
logger = setup_logger("DataManagement")

class DataManagement:

    def __init__(self):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        pass

    def saveToJson(self, obj):

        file_name = ""
        logger.info(f"Saving {type(obj).__name__} to JSON")
        users = ("Student", "Lecturer", "Advisor", "Admin", "DepartmentScheduler", "StudentsAffairs", "DepartmentHead")
        if type(obj).__name__ in users:
            file_name = obj.getUserInformation().get_UNIVERSITY_EMAIL()
            logger.info(f"Saving {type(obj).__name__} with university email: {file_name}")
        elif type(obj).__name__ == "Department":
            file_name = obj.getDepartmentID().getDepartmentName()
            logger.info(f"Saving {type(obj).__name__} with department name: {file_name}")
        elif type(obj).__name__ == "Faculty":
            file_name = obj.getFacultyID().getFacultyName()
            logger.info(f"Saving {type(obj).__name__} with faculty name: {file_name}")
        elif type(obj).__name__ == "Course":
            file_name = obj.getCourseName()
            logger.info(f"Saving {type(obj).__name__} with course name: {file_name}")
        elif type(obj).__name__ == "Classroom":
            file_name = obj.get_classroom_name()
            logger.info(f"Saving {type(obj).__name__} with classroom name: {file_name}")
        file_path = f"../{type(obj).__name__}s/{file_name}.json"
        self.__saveToJson(obj, file_path)

    def __saveToJson(self, obj, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Create the directory if it doesn't exist
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")

        # Open the file and write JSON data
        with open(file_path_and_name, "w") as file:
            json.dump(obj, file, indent=4, cls=customEncoder)
            logger.info(f"Saved {type(obj).__name__} to JSON")

    def loadFromJson(self, file_path_and_name):
        # Extract the directory path from the file path
        if not os.path.exists(file_path_and_name):
            logger.error(f"File doesn't exist: {file_path_and_name}")
            return None

        # Open the file and read JSON data
        with open(file_path_and_name, "r") as file:
            obj = json.load(file)
            logger.info(f"Loaded {type(obj).__name__} from JSON")
            return obj
        pass

    def deleteJsonFile(self, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Return None if the directory doesn't exist
        if directory and not os.path.exists(directory):
            logger.error(f"Directory doesn't exist: {directory}")
            return

        os.remove(file_path_and_name)
        logger.info(f"Deleted file: {file_path_and_name}")

    def getAllJsons(self, folder_path):
        allObjects = []
        if not os.path.exists(folder_path):
            logger.info(f"There is no path such {folder_path}")
            return
        logger.info(f"Getting all JSON files from {folder_path}")
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and file_path.endswith(".json"):
                allObjects.append(self.loadFromJson(file_path))

        logger.info(f"Got all JSON files from {folder_path}")
        return allObjects

    def getAllStudents(self):
        absolute_path = os.path.abspath("../Students")
        datas = self.getAllJsons(absolute_path)
        s_list = list()

        for data in datas:
            s_list.append(Student.from_dict(data))

        return s_list

    def createOrChangeStudent(self, student):
        self.saveToJson(student)

    def getStudent(self, university_email):
        data = self.loadFromJson(f"../Students/{university_email}.json")
        return Student.from_dict(data)

    def removeStudent(self, university_email):
        self.deleteJsonFile(f"../Students/{university_email}.json")

    def getAllLecturers(self):
        absolute_path = os.path.abspath("../Lecturers")
        datas = self.getAllJsons(absolute_path)

        lecturers = list()
        for data in datas:
            lecturers.append(Lecturer.from_dict(data))

        return lecturers

    def createOrChangeLecturer(self, lecturer):
        self.saveToJson(lecturer)

    def getLecturer(self, university_email):
        data = self.loadFromJson(f"../Lecturers/{university_email}.json")
        return Lecturer.from_dict(data)

    def removeLecturer(self, university_email):
        self.deleteJsonFile(f"../Lecturers/{university_email}.json")

    def getAllCourses(self):
        absolute_path = os.path.abspath("../Courses")
        datas = self.getAllJsons(absolute_path)
        c_list = list()

        for data in datas:
            c_list.append(Course.from_dict(data))

        return c_list

    def createOrChangeCourse(self, course):
        self.saveToJson(course)

    def getCourse(self, course_name):
        data = self.loadFromJson(f"../Courses/{course_name}.json")
        return Course.from_dict(data)

    def removeCourse(self, course_name):
        self.deleteJsonFile(f"../Courses/{course_name}.json")

    def getAllAdvisors(self):
        absolute_path = os.path.abspath("../Advisors")
        datas = self.getAllJsons(absolute_path)
        advisors = list()
        for data in datas:
            advisors.append(Advisor.from_dict(data))
        return advisors

    def createOrChangeAdvisor(self, advisor):
        self.saveToJson(advisor)

    def getAdvisor(self, university_email):
        data = self.loadFromJson(f"../Advisors/{university_email}.json")
        return Advisor.from_dict(data)

    def removeAdvisor(self, university_email):
        self.deleteJsonFile(f"../Advisors/{university_email}.json")

    def getAllFaculties(self):
        absolute_path = os.path.abspath("../Facultys")
        datas = self.getAllJsons(absolute_path)
        f_list = list()

        for data in datas:
            f_list.append(data)
        return f_list

    def createOrChangeFaculty(self, faculty):
        self.saveToJson(faculty)

    def getFaculty(self, faculty_name):
        data = self.loadFromJson(f"../Faculties/{faculty_name}.json")
        return Faculty.from_dict(data)


    def removeFaculty(self, faculty_name):
        self.deleteJsonFile(f"../Faculties/{faculty_name}.json")

    def getAllDepartments(self):
        absolute_path = os.path.abspath("../Departments")
        datas = self.getAllJsons(absolute_path)
        d_list = list()

        for data in datas:
            d_list.append(Department.from_dict(data))
        return d_list

    def createOrChangeDepartment(self, department):
        self.saveToJson(department)

    def getDepartment(self, department_name):
        data = self.loadFromJson(f"../Departments/{department_name}.json")
        return Department.from_dict(data)

    def removeDepartment(self, department_name):
        self.deleteJsonFile(f"../Departments/{department_name}.json")

    def getAllDepartmentHeads(self):
        absolute_path = os.path.abspath("../DepartmentHeads")
        datas = self.getAllJsons(absolute_path)
        dh_list = list()
        for data in datas:
            dh_list.append(DepartmentHead.from_dict(data))
        return dh_list


    def createOrChangeDepartmentHead(self, departmentHead):
        self.saveToJson(departmentHead)

    def getDepartmentHead(self, university_email):
        return self.loadFromJson(f"../DepartmentHeads/{university_email}.json")

    def removeDepartmentHead(self, university_email):
        self.deleteJsonFile(f"../DepartmentHeads/{university_email}.json")

    def getAllDepartmentSchedulers(self):
        absolute_path = os.path.abspath("../DepartmentSchedulers")
        datas = self.getAllJsons(absolute_path)
        dss = list()
        for data in datas:
            dss.append(DepartmentScheduler.from_dict(data))
        return dss

    def createOrChangeDepartmentScheduler(self, departmentScheduler):
        self.saveToJson(departmentScheduler)

    def getDepartmentScheduler(self, university_email):
        data = self.loadFromJson(f"../DepartmentSchedulers/{university_email}.json")
        return DepartmentScheduler.from_dict(data)

    def removeDepartmentScheduler(self, university_email):
        self.deleteJsonFile(f"../DepartmentSchedulers/{university_email}.json")

    def getAllStudentsAffairs(self):
        absolute_path = os.path.abspath("../StudentsAffairss")
        datas = self.getAllJsons(absolute_path)
        sas = list()
        for data in datas:
            sas.append(StudentsAffairs.from_dict(data))
        return sas

    def createOrChangeStudentsAffairs(self, studentsAffairs):
        self.saveToJson(studentsAffairs)

    def getStudentsAffairs(self, university_email):
        data = self.loadFromJson(f"../StudentsAffairs/{university_email}.json")
        return StudentsAffairs.from_dict(data)

    def removeStudentsAffairs(self, university_email):
        self.deleteJsonFile(f"../StudentsAffairs/{university_email}.json")

    def getAllClassrooms(self):
        absolute_path = os.path.abspath("../Classrooms")
        datas = self.getAllJsons(absolute_path)
        classrooms = list()
        for data in datas:
            classrooms.append(Classroom.from_dict(data))
        return classrooms

    def createOrChangeClassroom(self, classroom):
        self.saveToJson(classroom)


    def getClassroom(self, classroom_name):
        data = self.loadFromJson(f"../Classrooms/{classroom_name}.json")
        return Classroom.from_dict(data)

    def removeClassroom(self, classroom_name):
        self.deleteJsonFile(f"../Classrooms/{classroom_name}.json")


names = ["Ali", "Fatma", "Zeynep", "Ahmet", "Ayse", "Mehmet", "Emine", "Hasan", "Huseyin", "Elif", "Mustafa",
         "Sibel", "Burak", "Busra", "Omer", "Halime", "Murat", "Gizem", "Eren", "Esra", "Yusuf", "Melis", "Can",
         "Hatice", "Oguz", "Rabia", "Kerem", "Derya", "Furkan", "Sevgi", "Kadir", "Selin", "Ibrahim", "Tugce",
         "Cem", "Pelin", "Baris", "Leyla", "Serkan", "Sule", "Deniz", "Cansu", "Hakan", "Damla", "Merve", "Tolga",
         "Ezgi", "Volkan", "Dilara", "Uğur", "Selma", "Ece", "Adem", "Zeynep", "Burcu", "Ozan", "Cemile",
         "Yasemin", "Alper", "Duygu", "Serdar", "Gul", "Okan", "Seda", "Bora", "Nurgul", "Cagri", "Seyma",
         "Dogukan", "Gulsah", "Tuna", "Hande", "Gokhan", "Berna", "Caner", "Bahar", "Arda", "Necla", "Batuhan",
         "Hilal", "Atakan", "Tulay", "Cengiz", "Berke", "Perihan", "Ece", "Tayfun", "Ceyda", "Emirhan", "Gonca",
         "Erdem", "Ayla", "Tamer", "Isil", "Havva", "Sevda", "Gokce", "Alime"]
surnames = ["Yilmaz", "Kaya", "Demir", "Celik", "Sahin", "Arslan", "Aydin", "Eren", "Ozturk", "Yildiz", "Aslan",
            "Keskin", "Polat", "Dogan", "Koc", "Gunes", "Aksoy", "Karaca", "Uzun", "Kilic", "Tas", "Candan",
            "Erdogan", "Gul", "Yalcin", "Balci", "Kaplan", "Can", "Durmaz", "Cetin", "Turkmen", "Simsek", "Duman",
            "Sari", "Saglam", "Ucar", "Kurt", "Ozdemir", "Isik", "Ersoy", "Soylu", "Korkmaz", "Bulut", "Kavak",
            "Turan", "Altun", "Ozkan", "Kara", "Gunduz", "Ates", "Yucel", "Erdem", "Keser", "Celikkan", "Toprak",
            "Yalman", "Ari", "Bayrak", "Deniz", "Durak", "Gultekin", "Orhan", "Aktas", "Sezer", "Pala", "Karatas",
            "Aksu", "Goksel", "Bozkurt", "Yuksel", "Albayrak", "Ozen", "Seker", "Erol", "Akcay", "Ozdem", "Arman",
            "Karahan", "Tunc", "Oztan", "Batur", "Tokgoz", "Acar", "Ergin", "Ulu", "Uz", "Altay", "Soydan",
            "Koroglu", "Torun", "Akbas", "Kalayci", "Koksal", "Tuna", "Akin", "Guler", "Erkan", "Gokce"]
cities = ["Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan",
          "Artvin", "Aydin", "Balikesir", "Bartin", "Batman", "Bayburt", "Bilecik", "Bingol", "Bitlis", "Bolu",
          "Burdur", "Bursa", "Canakkale", "Cankiri", "Corum", "Denizli", "Diyarbakir", "Duzce", "Edirne", "Elazig",
          "Erzincan", "Erzurum", "Eskisehir", "Gaziantep", "Giresun", "Gumushane", "Hakkari", "Hatay", "Igdir",
          "Isparta", "Istanbul", "Izmir", "Kahramanmaras", "Karabuk", "Karaman", "Kars", "Kastamonu", "Kayseri",
          "Kirikkale", "Kirklareli", "Kirsehir", "Kilis", "Kocaeli", "Konya", "Kutahya", "Malatya", "Manisa",
          "Mardin", "Mersin", "Mugla", "Mus", "Nevsehir", "Nigde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun",
          "Sanliurfa", "Siirt", "Sinop", "Sirnak", "Sivas", "Tekirdag", "Tokat", "Trabzon", "Tunceli", "Usak",
          "Van", "Yalova", "Yozgat", "Zonguldak"]


def __getRandomName():
    ___name = random.choice(names)
    logger.info(f"Getting random name: {___name}")
    return ___name


def __getRandomSurname():
    ___surname = random.choice(surnames)
    logger.info(f"Getting random surname: {___surname}")
    return ___surname


def __getRandomCity():
    ___city = random.choice(cities)
    logger.info(f"Getting random city: {___city}")
    return ___city


def __generateEmail(name, surname):
    ___email = f"{str(name).lower()}{str(surname).lower()}{random.randint(0, 100)}@gmail.com"
    logger.info(f"Generated email: {___email}")
    return ___email


def __generateUniversityEmail(name, surname):
    ___unimail = f"{str(name).lower()}{str(surname).lower()}@marun.edu.tr"
    logger.info(f"Generated university email: {___unimail}")
    return ___unimail


def __generatePhoneNumber():
    phoneNumber = f"+90 5{random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}"
    logger.info(f"Generated phone number: {phoneNumber}")
    return phoneNumber


def __generatePassword(name, city, phoneNumber):
    ___password = str(1234)
    logger.info(f"Generated password: {___password}")
    return ___password


def __generateRandomUserInformation():
    logger.info("Generating random user information")
    firstName = __getRandomName()
    lastName = __getRandomSurname()
    city = __getRandomCity()
    phoneNumber = __generatePhoneNumber()
    email = __generateEmail(firstName, lastName)
    universityEmail = __generateUniversityEmail(firstName, lastName)
    password = __generatePassword(firstName, city, phoneNumber)
    ui = UserInformation(firstName, lastName, password, universityEmail, email, city, phoneNumber)
    logger.info(
        f"Generated random user information: {firstName} {lastName} {city} {phoneNumber} {email} {universityEmail}")
    return ui


def generateFaculty(facultyID, facultyName):
    logger.info("Generating faculty")
    ___fac = Faculty(FacultyID(facultyID, facultyName))
    logger.info(f"Generated faculty: {facultyID} {facultyName}")
    return ___fac


def generateDepartment(departmentID, departmentName, faculty):
    logger.info("Generating department")
    ___dep = Department(DepartmentID(departmentID, departmentName), faculty.getFacultyID())
    faculty.addDepartment(___dep)
    logger.info(f"Generated department: {departmentID} {departmentName}")
    return ___dep


def generateRandomLecturer(department):
    logger.info("Generating random lecturer")
    userInformation = __generateRandomUserInformation()
    ___lec = Lecturer(userInformation)
    logger.info(f"Generated random lecturer: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___lec


def generateRandomAdvisor(department):
    logger.info("Generating random advisor")
    userInformation = __generateRandomUserInformation()
    ___adv = Advisor(userInformation)
    logger.info(f"Generated random advisor: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___adv


def generateRandomStudent(department, entranceDate, entranceRank, advisorID):
    logger.info("Generating random student")
    userInformation = __generateRandomUserInformation()
    studentID = StudentID(department.getDepartmentID(), entranceDate, entranceRank, department.get_facultyID())
    transcript = Transcript(studentID)
    return Student(userInformation, studentID, transcript, advisorID, 2025 - entranceDate)


def generateNonRandomStudent(userInformation, department, entrance_date, entrance_rank, advisor_id):
    logger.info("Generating non-random student")
    studentID = StudentID(department.getDepartmentID(), entrance_date, entrance_rank, department.get_facultyID())
    transcript = Transcript(studentID)
    ___stu = Student(userInformation, studentID, transcript, advisor_id, 2025 - entrance_date)
    logger.info(f"Generated non-random student: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___stu


def generateCourseInformation(courseName, courseCode):
    logger.info("Generating course information")
    ___courseInfo = CourseInformation(courseName, courseCode)
    logger.info(f"Generated course information: {courseName} {courseCode}")
    return ___courseInfo


def generateCourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID):
    logger.info("Generating course requirements")
    ___courseReq = CourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID)
    logger.info(f"Generated course requirements: {prerequisiteCourses} {minimumCurrentClass}")
    return ___courseReq


def generateCourse(lecturerForSections, days, sectionTimes, classRooms, courseName, courseCode, prerequisiteCourses,
                   minimumCurrentClass, facultyID, departmentID):
    logger.info("Generating course")
    ___courseInfo = generateCourseInformation(courseName, courseCode)
    ___courseReq = generateCourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID)
    courseSections = list()
    for i in range(len(lecturerForSections)):
        ___courseSec = CourseSection(days[i], sectionTimes[i], lecturerForSections[i], classRooms[i])
        courseSections.append(___courseSec)
    ___course = Course(___courseInfo, ___courseReq, courseSections)
    logger.info(f"Generated course: {courseName} {courseCode}")
    return ___course


def generateRandomDepartmentScheduler(department):
    logger.info("Generating random department scheduler")
    userInformation = __generateRandomUserInformation()
    ___depSched = DepartmentScheduler(userInformation)
    logger.info(
        f"Generated random department scheduler: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___depSched

def generateRandomDepartmentHead(department):
    logger.info("Generating random department head")
    userInformation = __generateRandomUserInformation()
    ___depHead = DepartmentHead(userInformation)
    logger.info(
        f"Generated random department head: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___depHead

def generateRandomStudentsAffairs(department):
    logger.info("Generating random students affairs")
    userInformation = __generateRandomUserInformation()
    ___stuAff = StudentsAffairs(userInformation)
    logger.info(
        f"Generated random students affairs: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___stuAff

def generateClassroom(classroomName, capacity):
    logger.info("Generating classroom")
    ___classroom = Classroom(classroomName, capacity)
    logger.info(f"Generated classroom: {classroomName} {capacity}")
    return ___classroom

class customEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

# dm = DataManagement()
# fac = generateFaculty(15,"eng")
# dm.createOrChangeFaculty(fac)
#
# dep = generateDepartment(150, "comp eng",fac )
# dm.createOrChangeDepartment(dep)
#
# ad = generateRandomAdvisor(dep)
#
# dm.createOrChangeAdvisor(ad)
#
# stu = generateRandomStudent(dep,2022,1,ad.get_staffId())
# dm.createOrChangeStudent(stu)
#
# lec = generateRandomLecturer(dep)
# dm.createOrChangeLecturer(lec)
#
# sa = generateRandomStudentsAffairs(dep)
# dm.createOrChangeStudentsAffairs(sa)
#
# dsch = generateRandomDepartmentScheduler(dep)
# dm.createOrChangeDepartmentScheduler(dsch)
#
# dh = generateRandomDepartmentHead(dep)
# dm.createOrChangeDepartmentHead(dh)
#
# cr = generateClassroom("aa",20)
# dm.createOrChangeClassroom(cr)
#
# course = generateCourse([lec], [Day.Friday], [SectionTime.Fifth], [cr], "test", "TT101", list(), 1, dep.get_facultyID(), dep.getDepartmentID())
# dm.createOrChangeCourse(course)
#
# course1 = generateCourse([lec], [Day.Friday], [SectionTime.Fifth], [cr], "test2", "TT102", list(), 1, dep.get_facultyID(), dep.getDepartmentID())
# dm.createOrChangeCourse(course1)