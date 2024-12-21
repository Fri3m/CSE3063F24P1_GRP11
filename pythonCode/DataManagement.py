import json
import os
import random
from json import JSONEncoder

from fontTools.merge.util import first

from pythonCode.Department import Department, DepartmentID
from pythonCode.User import User
from pythonCode.UserInformation import UserInformation
from pythonCode.Student import StudentID, Student
from pythonCode.Transcript import Transcript


class DataManagement:

    def saveToJson(self, obj):
        file_name = ""
        users = ("Student", "Lecturer", "Advisor", "Admin", "DepartmentScheduler", "StudentsAffairs", "DepartmentHead")
        if type(obj).__name__ in users:
            file_name = obj.getUserInformation().get_UNIVERSITY_EMAIL()
        elif type(obj).__name__ == "Department":
            file_name = obj.getDepartmentID().getDepartmentName()
        elif type(obj).__name__ == "Faculty":
            file_name = obj.getFacultyID().getFacultyName()
        elif type(obj).__name__ == "Course":
            file_name = obj.getCourseID().getCourseName()

        file_path = f"../{type(obj).__name__}s/{file_name}.json"
        self.__saveToJson(obj, file_path)

    def __saveToJson(self, obj, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Create the directory if it doesn't exist
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Open the file and write JSON data
        with open(file_path_and_name, "w") as file:
            json.dump(obj, file, indent=4, cls=customEncoder)

    def loadFromJson(self, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Return None if the directory doesn't exist
        if directory and not os.path.exists(directory):
            return None

        # Open the file and read JSON data
        with open(file_path_and_name, "r") as file:
            return json.load(file)
        pass

    def deleteJsonFile(self, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Return None if the directory doesn't exist
        if directory and not os.path.exists(directory):
            return

        os.remove(file_path_and_name)

    def getAllJsons(self, folder_path):
        allObjects = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".json"):
                    allObjects.append(self.loadFromJson(os.path.join(root, file)))
        return allObjects

    def getAllStudents(self):
        return self.getAllJsons("../Students")

    def createOrChangeStudent(self, student):
        self.saveToJson(student)

    def getStudent(self, university_email):
        return self.loadFromJson(f"../Students/{university_email}.json")

    def removeStudent(self, university_email):
        self.deleteJsonFile(f"../Students/{university_email}.json")

    def getAllLecturers(self):
        return self.getAllJsons("../Lecturers")

    def createOrChangeLecturer(self, lecturer):
        self.saveToJson(lecturer)

    def getLecturer(self, university_email):
        return self.loadFromJson(f"../Lecturers/{university_email}.json")

    def removeLecturer(self, university_email):
        self.deleteJsonFile(f"../Lecturers/{university_email}.json")

    def getAllCourses(self):
        return self.getAllJsons("../Courses")

    def createOrChangeCourse(self, course):
        self.saveToJson(course)

    def getCourse(self, course_name):
        return self.loadFromJson(f"../Courses/{course_name}.json")

    def removeCourse(self, course_name):
        self.deleteJsonFile(f"../Courses/{course_name}.json")

    def getAllAdvisors(self):
        return self.getAllJsons("../Advisors")

    def createOrChangeAdvisor(self, advisor):
        self.saveToJson(advisor)

    def getAdvisor(self, university_email):
        return self.loadFromJson(f"../Advisors/{university_email}.json")

    def removeAdvisor(self, university_email):
        self.deleteJsonFile(f"../Advisors/{university_email}.json")

    def getAllFaculties(self):
        return self.getAllJsons("../Faculties")

    def createOrChangeFaculty(self, faculty):
        self.saveToJson(faculty)

    def getFaculty(self, faculty_name):
        return self.loadFromJson(f"../Faculties/{faculty_name}.json")

    def removeFaculty(self, faculty_name):
        self.deleteJsonFile(f"../Faculties/{faculty_name}.json")

    def getAllDepartments(self):
        return self.getAllJsons("../Departments")

    def createOrChangeDepartment(self, department):
        self.saveToJson(department)

    def getDepartment(self, department_name):
        return self.loadFromJson(f"../Departments/{department_name}.json")

    def removeDepartment(self, department_name):
        self.deleteJsonFile(f"../Departments/{department_name}.json")

    def getAllDepartmentHeads(self):
        return self.getAllJsons("../DepartmentHeads")

    def createOrChangeDepartmentHead(self, departmentHead):
        self.saveToJson(departmentHead)

    def getDepartmentHead(self, university_email):
        return self.loadFromJson(f"../DepartmentHeads/{university_email}.json")

    def removeDepartmentHead(self, university_email):
        self.deleteJsonFile(f"../DepartmentHeads/{university_email}.json")

    def getAllDepartmentSchedulers(self):
        return self.getAllJsons("../DepartmentSchedulers")

    def createOrChangeDepartmentScheduler(self, departmentScheduler):
        self.saveToJson(departmentScheduler)

    def getDepartmentScheduler(self, university_email):
        return self.loadFromJson(f"../DepartmentSchedulers/{university_email}.json")

    def removeDepartmentScheduler(self, university_email):
        self.deleteJsonFile(f"../DepartmentSchedulers/{university_email}.json")

    def getAllStudentsAffairs(self):
        return self.getAllJsons("../StudentsAffairs")

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
    return random.choice(names)


def __getRandomSurname():
    return random.choice(surnames)


def __getRandomCity():
    return random.choice(cities)


def __generateEmail(name, surname):
    return f"{str(name).lower()}{str(surname).lower()}{random.randint(0, 100)}@gmail.com"


def __generateUniversityEmail(name, surname):
    return f"{str(name).lower()}{str(surname).lower()}@marun.edu.tr"


def __generatePhoneNumber():
    return f"+90 5{random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}"


def __generatePassword():
    return str(1234)


def __generateRandomUserInformation():
    firstName = __getRandomName()
    lastName = __getRandomSurname()
    city = __getRandomCity()
    phoneNumber = __generatePhoneNumber()
    email = __generateEmail(firstName, lastName)
    universityEmail = __generateUniversityEmail(firstName, lastName)
    password = __generatePassword()
    ui = UserInformation(firstName, lastName, password, universityEmail, email, city, phoneNumber)
    return ui


def generateRandomStudent(department, entranceDate, entranceRank, advisorID):
    userInformation = __generateRandomUserInformation()
    studentID = StudentID(department.getDepartmentID(), entranceDate, entranceRank, department.get_facultyID())
    transcript = Transcript(studentID)
    return Student(userInformation, studentID, transcript, advisorID, 2025 - entranceDate)


class customEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


dm = DataManagement()

# st = generateRandomStudent(Department(DepartmentID("1", "Computer Engineering"), "1"), 2019, 1, "1")
# dm.saveToJson(st)

students = dm.getAllStudents()
print(students)
