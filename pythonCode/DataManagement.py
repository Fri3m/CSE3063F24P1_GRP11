import json
import os
import random
from json import JSONEncoder
import logging

from Course import CourseInformation, CourseRequirements, CourseSection, Course
from Department import DepartmentID, Department
from Faculty import FacultyID, Faculty
from User import Lecturer, Advisor, DepartmentScheduler, StudentsAffairs

logging.basicConfig(filename='../Logs/DataLogs.log', level=logging.INFO)

from pythonCode.UserInformation import UserInformation
from pythonCode.Student import StudentID, Student
from pythonCode.Transcript import Transcript


class DataManagement:

    def __init__(self):
        pass

    def saveToJson(self, obj):
        file_name = ""
        logging.info(f"Saving {type(obj).__name__} to JSON")
        users = ("Student", "Lecturer", "Advisor", "Admin", "DepartmentScheduler", "StudentsAffairs", "DepartmentHead")
        if type(obj).__name__ in users:
            file_name = obj.getUserInformation().get_UNIVERSITY_EMAIL()
            logging.info(f"Saving {type(obj).__name__} with university email: {file_name}")
        elif type(obj).__name__ == "Department":
            file_name = obj.getDepartmentID().getDepartmentName()
            logging.info(f"Saving {type(obj).__name__} with department name: {file_name}")
        elif type(obj).__name__ == "Faculty":
            file_name = obj.getFacultyID().get_faculty_name()
            logging.info(f"Saving {type(obj).__name__} with faculty name: {file_name}")
        elif type(obj).__name__ == "Course":
            file_name = obj.getCourseID().getCourseName()
            logging.info(f"Saving {type(obj).__name__} with course name: {file_name}")
        file_path = f"../{type(obj).__name__}s/{file_name}.json"
        self.__saveToJson(obj, file_path)

    def __saveToJson(self, obj, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Create the directory if it doesn't exist
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created directory: {directory}")

        # Open the file and write JSON data
        with open(file_path_and_name, "w") as file:
            json.dump(obj, file, indent=4, cls=customEncoder)
            logging.info(f"Saved {type(obj).__name__} to JSON")

    def loadFromJson(self, file_path_and_name):
        # Extract the directory path from the file path
        if not os.path.exists(file_path_and_name):
            logging.error(f"File doesn't exist: {file_path_and_name}")
            return None

        # Open the file and read JSON data
        with open(file_path_and_name, "r") as file:
            obj = json.load(file)
            logging.info(f"Loaded {type(obj).__name__} from JSON")
            return obj
        pass

    def deleteJsonFile(self, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Return None if the directory doesn't exist
        if directory and not os.path.exists(directory):
            logging.error(f"Directory doesn't exist: {directory}")
            return

        os.remove(file_path_and_name)
        logging.info(f"Deleted file: {file_path_and_name}")

    def getAllJsons(self, folder_path):
        allObjects = []
        logging.info(f"Getting all JSON files from {folder_path}")
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and file_path.endswith(".json"):
                allObjects.append(self.loadFromJson(file_path))

        # for root, dirs, files in os.walk(folder_path):
        #     print(f"{root} {dirs} {files}")
        #     for file in files:
        #         if file.endswith(".json"):
        #             allObjects.append(self.loadFromJson(os.path.join(root, file)))

        logging.info(f"Got all JSON files from {folder_path}")
        return allObjects

    def getAllStudents(self):
        absolute_path = os.path.abspath("../Students")
        return self.getAllJsons(absolute_path)

    def createOrChangeStudent(self, student):
        self.saveToJson(student)

    def getStudent(self, university_email):
        return self.loadFromJson(f"../Students/{university_email}.json")

    def removeStudent(self, university_email):
        self.deleteJsonFile(f"../Students/{university_email}.json")

    def getAllLecturers(self):
        absolute_path = os.path.abspath("../Lecturers")
        return self.getAllJsons(absolute_path)

    def createOrChangeLecturer(self, lecturer):
        self.saveToJson(lecturer)

    def getLecturer(self, university_email):
        return self.loadFromJson(f"../Lecturers/{university_email}.json")

    def removeLecturer(self, university_email):
        self.deleteJsonFile(f"../Lecturers/{university_email}.json")

    def getAllCourses(self):
        absolute_path = os.path.abspath("../Courses")
        return self.getAllJsons(absolute_path)

    def createOrChangeCourse(self, course):
        self.saveToJson(course)

    def getCourse(self, course_name):
        return self.loadFromJson(f"../Courses/{course_name}.json")

    def removeCourse(self, course_name):
        self.deleteJsonFile(f"../Courses/{course_name}.json")

    def getAllAdvisors(self):
        absolute_path = os.path.abspath("../Advisors")
        return self.getAllJsons(absolute_path)

    def createOrChangeAdvisor(self, advisor):
        self.saveToJson(advisor)

    def getAdvisor(self, university_email):
        return self.loadFromJson(f"../Advisors/{university_email}.json")

    def removeAdvisor(self, university_email):
        self.deleteJsonFile(f"../Advisors/{university_email}.json")

    def getAllFaculties(self):
        absolute_path = os.path.abspath("../Faculties")
        return self.getAllJsons(absolute_path)

    def createOrChangeFaculty(self, faculty):
        self.saveToJson(faculty)

    def getFaculty(self, faculty_name):
        return self.loadFromJson(f"../Faculties/{faculty_name}.json")

    def removeFaculty(self, faculty_name):
        self.deleteJsonFile(f"../Faculties/{faculty_name}.json")

    def getAllDepartments(self):
        absolute_path = os.path.abspath("../Departments")
        return self.getAllJsons(absolute_path)

    def createOrChangeDepartment(self, department):
        self.saveToJson(department)

    def getDepartment(self, department_name):
        return self.loadFromJson(f"../Departments/{department_name}.json")

    def removeDepartment(self, department_name):
        self.deleteJsonFile(f"../Departments/{department_name}.json")

    def getAllDepartmentHeads(self):
        absolute_path = os.path.abspath("../DepartmentHeads")
        return self.getAllJsons(absolute_path)

    def createOrChangeDepartmentHead(self, departmentHead):
        self.saveToJson(departmentHead)

    def getDepartmentHead(self, university_email):
        return self.loadFromJson(f"../DepartmentHeads/{university_email}.json")

    def removeDepartmentHead(self, university_email):
        self.deleteJsonFile(f"../DepartmentHeads/{university_email}.json")

    def getAllDepartmentSchedulers(self):
        absolute_path = os.path.abspath("../DepartmentSchedulers")
        return self.getAllJsons(absolute_path)

    def createOrChangeDepartmentScheduler(self, departmentScheduler):
        self.saveToJson(departmentScheduler)

    def getDepartmentScheduler(self, university_email):
        return self.loadFromJson(f"../DepartmentSchedulers/{university_email}.json")

    def removeDepartmentScheduler(self, university_email):
        self.deleteJsonFile(f"../DepartmentSchedulers/{university_email}.json")

    def getAllStudentsAffairs(self):
        absolute_path = os.path.abspath("../StudentsAffairs")
        return self.getAllJsons(absolute_path)

    def createOrChangeStudentsAffairs(self, studentsAffairs):
        self.saveToJson(studentsAffairs)

    def getStudentsAffairs(self, university_email):
        return self.loadFromJson(f"../StudentsAffairs/{university_email}.json")

    def removeStudentsAffairs(self, university_email):
        self.deleteJsonFile(f"../StudentsAffairs/{university_email}.json")


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
    logging.info(f"Getting random name: {___name}")
    return ___name


def __getRandomSurname():
    ___surname = random.choice(surnames)
    logging.info(f"Getting random surname: {___surname}")
    return ___surname


def __getRandomCity():
    ___city = random.choice(cities)
    logging.info(f"Getting random city: {___city}")
    return ___city


def __generateEmail(name, surname):
    ___email = f"{str(name).lower()}{str(surname).lower()}{random.randint(0, 100)}@gmail.com"
    logging.info(f"Generated email: {___email}")
    return ___email


def __generateUniversityEmail(name, surname):
    ___unimail = f"{str(name).lower()}{str(surname).lower()}@marun.edu.tr"
    logging.info(f"Generated university email: {___unimail}")
    return ___unimail


def __generatePhoneNumber():
    phoneNumber = f"+90 5{random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}"
    logging.info(f"Generated phone number: {phoneNumber}")
    return phoneNumber


def __generatePassword(name, city, phoneNumber):
    ___password = str(1234)
    logging.info(f"Generated password: {___password}")
    return ___password


def __generateRandomUserInformation():
    logging.info("Generating random user information")
    firstName = __getRandomName()
    lastName = __getRandomSurname()
    city = __getRandomCity()
    phoneNumber = __generatePhoneNumber()
    email = __generateEmail(firstName, lastName)
    universityEmail = __generateUniversityEmail(firstName, lastName)
    password = __generatePassword(firstName, city, phoneNumber)
    ui = UserInformation(firstName, lastName, password, universityEmail, email, city, phoneNumber)
    logging.info(
        f"Generated random user information: {firstName} {lastName} {city} {phoneNumber} {email} {universityEmail}")
    return ui


def generateFaculty(facultyID, facultyName):
    logging.info("Generating faculty")
    ___fac = Faculty(FacultyID(facultyID, facultyName))
    logging.info(f"Generated faculty: {facultyID} {facultyName}")
    return ___fac


def generateDepartment(departmentID, departmentName, faculty):
    logging.info("Generating department")
    ___dep = Department(DepartmentID(departmentID, departmentName), faculty.getFacultyID())
    faculty.addDepartment(___dep)
    logging.info(f"Generated department: {departmentID} {departmentName}")
    return ___dep


def generateRandomLecturer(department):
    logging.info("Generating random lecturer")
    userInformation = __generateRandomUserInformation()
    ___lec = Lecturer(userInformation)
    logging.info(f"Generated random lecturer: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___lec


def generateRandomAdvisor(department):
    logging.info("Generating random advisor")
    userInformation = __generateRandomUserInformation()
    ___adv = Advisor(userInformation)
    logging.info(f"Generated random advisor: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___adv


def generateRandomStudent(department, entranceDate, entranceRank, advisorID):
    logging.info("Generating random student")
    userInformation = __generateRandomUserInformation()
    studentID = StudentID(department.getDepartmentID(), entranceDate, entranceRank, department.get_facultyID())
    transcript = Transcript(studentID)
    return Student(userInformation, studentID, transcript, advisorID, 2025 - entranceDate)


def generateNonRandomStudent(userInformation, department, entrance_date, entrance_rank, advisor_id):
    logging.info("Generating non-random student")
    studentID = StudentID(department.getDepartmentID(), entrance_date, entrance_rank, department.get_facultyID())
    transcript = Transcript(studentID)
    ___stu = Student(userInformation, studentID, transcript, advisor_id, 2025 - entrance_date)
    logging.info(f"Generated non-random student: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___stu


def generateCourseInformation(courseName, courseCode):
    logging.info("Generating course information")
    ___courseInfo = CourseInformation(courseName, courseCode)
    logging.info(f"Generated course information: {courseName} {courseCode}")
    return ___courseInfo


def generateCourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID):
    logging.info("Generating course requirements")
    ___courseReq = CourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID)
    logging.info(f"Generated course requirements: {prerequisiteCourses} {minimumCurrentClass}")
    return ___courseReq


def generateCourse(lecturerForSections, days, sectionTimes, courseName, courseCode, prerequisiteCourses,
                   minimumCurrentClass, facultyID, departmentID):
    logging.info("Generating course")
    ___courseInfo = generateCourseInformation(courseName, courseCode)
    ___courseReq = generateCourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID)
    courseSections = list()
    for i in range(len(lecturerForSections)):
        ___courseSec = CourseSection(lecturerForSections[i], days[i], sectionTimes[i])
        courseSections.append(___courseSec)
    ___course = Course(___courseInfo, ___courseReq, courseSections)
    logging.info(f"Generated course: {courseName} {courseCode}")
    return ___course


def generateRandomDepartmentScheduler(department):
    logging.info("Generating random department scheduler")
    userInformation = __generateRandomUserInformation()
    ___depSched = DepartmentScheduler(userInformation)
    logging.info(
        f"Generated random department scheduler: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___depSched


def generateRandomStudentsAffairs(department):
    logging.info("Generating random students affairs")
    userInformation = __generateRandomUserInformation()
    ___stuAff = StudentsAffairs(userInformation)
    logging.info(
        f"Generated random students affairs: {userInformation.get_FIRST_NAME()} {userInformation.get_LAST_NAME()}")
    return ___stuAff


class customEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


# dm = DataManagement()
# fac = generateFaculty(15,"eng")
# dep = generateDepartment(150, "comp eng",fac )
# ad = generateRandomAdvisor(dep)
# stu = generateRandomStudent(dep,2022,1,ad.get_staffId())
# dm.createOrChangeStudent(stu)
# dm.createOrChangeFaculty(fac)
# dm.createOrChangeDepartment(dep)
# dm.createOrChangeAdvisor(ad)

# students = dm.getAllStudents()
# print(students)
