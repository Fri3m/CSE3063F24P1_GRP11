import json
import os
import random

from fontTools.merge.util import first

from pythonCode.Department import Department, DepartmentID
from pythonCode.LoginAuthService import UserInformation
from pythonCode.Student import StudentID, Student
from pythonCode.Transcript import Transcript


class DataManagement:

    def saveToJson(self, obj, obj_type):
        match obj_type:
            case "Course":
                self.__saveToJson(obj, f"{obj_type}/{obj.getCourseCode()}.json")
            case "student":
                self.__saveToJson(obj,
                                  f"{obj_type}/1.json")

    def __saveToJson(self, obj, file_path_and_name):
        # Extract the directory path from the file path
        directory = os.path.dirname(file_path_and_name)

        # Create the directory if it doesn't exist
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Open the file and write JSON data
        with open(file_path_and_name, "w") as file:
            json.dump(obj, file, indent=4)

    def loadFromJson(self, name, obj_type):
        pass

    # helper methods and variables for generating random objects


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
    ui = UserInformation(encoded_password=password,
                         university_email=universityEmail)
    return ui


def generateRandomStudent(department, entranceDate, entranceRank, advisorID):
    userInformation = __generateRandomUserInformation()
    studentID = StudentID(department.getDepartmentID(), entranceDate, entranceRank, department.get_facultyID())
    transcript = Transcript(studentID)
    return Student(userInformation, studentID, transcript, advisorID, 2025 - entranceDate)


dep = Department(DepartmentID(150,"comp sci"), 2)

xx = generateRandomStudent(dep, 2019, 100, 1)
x = DataManagement()
x.saveToJson(xx, "student")
