package src;

import com.google.gson.Gson;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class DataManagement {

    private final String STUDENTS_FILE_PATH = "data/students/";
    private final String COURSES_FILE_PATH = "data/courses/";
    private final String LECTURERS_FILE_PATH = "data/lecturers/";
    private final String ADVISORS_FILE_PATH = "data/advisors/";
    private final String FACULTIES_FILE_PATH = "data/faculties/";
    private final String DEPARTMENTS_FILE_PATH = "data/departments/";

    private final Gson gson = new Gson();

    public static void main(String[] args) {
        DataManagement dataManagement = new DataManagement();

        Faculty engineering = dataManagement.generateFaculty(1, "Engineering");
        dataManagement.createOrChangeFaculty(engineering);

        Department computerEngineering = dataManagement.generateDepartment(150, "ComputerEngineering", engineering);
        dataManagement.createOrChangeDepartment(computerEngineering);


        Department electricalEngineering = dataManagement.generateDepartment(151, "ElectricalEngineering", engineering);
        dataManagement.createOrChangeDepartment(electricalEngineering);

        Advisor advisor = dataManagement.generateRandomAdvisor(computerEngineering);
        Lecturer lecturer = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer3 = dataManagement.generateRandomLecturer(computerEngineering);
        dataManagement.createOrChangeAdvisor(advisor);
        dataManagement.createOrChangeLecturer(lecturer);
        dataManagement.createOrChangeLecturer(lecturer3);

        ArrayList<Lecturer> lecturersForSections = new ArrayList<>();
        lecturersForSections.add(lecturer);
        lecturersForSections.add(lecturer);
        lecturersForSections.add(lecturer);
        ArrayList<Day> days = new ArrayList<>();
        days.add(Day.Monday);
        days.add(Day.Monday);
        days.add(Day.Thursday);
        ArrayList<SectionTime> sectionTimes = new ArrayList<>();
        sectionTimes.add(SectionTime.Fifth);
        sectionTimes.add(SectionTime.Sixth);
        sectionTimes.add(SectionTime.Fifth);
        Course course = dataManagement.generateCourse(lecturersForSections,days,sectionTimes,"Introduction to Computer Science", "CS101", new ArrayList<>(),1, computerEngineering.get_facultyID(),computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer);
        lecturersForSections.add(lecturer3);
        lecturersForSections.add(lecturer3);
        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Wednesday);
        days.add(Day.Thursday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Fifth);
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Fifth);

        Course course1 = dataManagement.generateCourse(lecturersForSections,days,sectionTimes,"Random", "XX001", new ArrayList<>(),1, computerEngineering.get_facultyID(),computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course1);



        Advisor advisor2 = dataManagement.generateRandomAdvisor(electricalEngineering);
        Lecturer lecturer2 = dataManagement.generateRandomLecturer(electricalEngineering);
        dataManagement.createOrChangeAdvisor(advisor2);
        dataManagement.createOrChangeLecturer(lecturer2);

        Student student1 = dataManagement.generateRandomStudent(computerEngineering, 2018, 5, advisor.get_staffId());
        Student student2 = dataManagement.generateRandomStudent(computerEngineering, 2018, 5, advisor.get_staffId());
        Student student3 = dataManagement.generateRandomStudent(computerEngineering, 2018, 5, advisor.get_staffId());

        TakenCourse takenCourse = new TakenCourse(course1.getCourseInformation(),90,54);
        student1.getTranscript().addTakenCourse(takenCourse);
        dataManagement.createOrChangeStudent(student1);
        dataManagement.createOrChangeStudent(student2);
        dataManagement.createOrChangeStudent(student3);


    }


    public ArrayList<Student> getAllStudents() {
        // Read all students from the files
        ArrayList<Student> students = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(STUDENTS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(STUDENTS_FILE_PATH + filePath)) {
                    students.add(gson.fromJson(reader, Student.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return students;
    }

    public void createOrChangeStudent(Student student) {
        // Save student to the file
        String filePath = STUDENTS_FILE_PATH + student.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try (FileWriter writer = new FileWriter(filePath);) {

            gson.toJson(student, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Student getStudent(String university_email) {
        // Read student from the file
        String filePath = STUDENTS_FILE_PATH + university_email + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Student.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeStudent(Student student) {
        if (student == null) {
            return false;
        }
        String filePath = STUDENTS_FILE_PATH + student.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try {
            java.io.File file = new java.io.File(filePath);
            if (file.exists()) {
                file.delete();
                return true;
            }
        }catch (Exception e){
            e.printStackTrace();
        }


        return false;
    }

    public ArrayList<Lecturer> getAllLecturers() {
        // Read all lecturers from the files
        ArrayList<Lecturer> lecturers = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(LECTURERS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(LECTURERS_FILE_PATH + filePath)) {
                    lecturers.add(gson.fromJson(reader, Lecturer.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lecturers;
    }

    public void createOrChangeLecturer(Lecturer lecturer) {
        String filePath = LECTURERS_FILE_PATH + lecturer.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(lecturer, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Lecturer getLecturer(String university_email) {
        String filePath = LECTURERS_FILE_PATH + university_email + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Lecturer.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeLecturer(Lecturer lecturer) {
        String filePath = LECTURERS_FILE_PATH + lecturer.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    public ArrayList<Course> getAllCourses() {
        // Read all courses from the files
        ArrayList<Course> courses = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(COURSES_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(COURSES_FILE_PATH + filePath)) {
                    courses.add(gson.fromJson(reader, Course.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return courses;
    }

    public void createOrChangeCourse(Course course) {
        // Save course to the file
        String filePath = COURSES_FILE_PATH + course.getCourseInformation().getCourseName() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(course, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Course getCourse(String courseName) {
        // Read course from the file
        String filePath = COURSES_FILE_PATH + courseName + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Course.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeCourse(Course course) {
        String filePath = COURSES_FILE_PATH + course.getCourseInformation().getCourseName() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }
        return false;
    }

    public ArrayList<Advisor> getAllAdvisors() {
        // Read all advisors from the files
        ArrayList<Advisor> advisors = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(ADVISORS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(ADVISORS_FILE_PATH + filePath)) {
                    advisors.add(gson.fromJson(reader, Advisor.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return advisors;
    }

    public void createOrChangeAdvisor(Advisor advisor) {
        // Save advisor to the file
        String filePath = ADVISORS_FILE_PATH + advisor.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(advisor, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Advisor getAdvisor(String university_email) {
        // Read advisor from the file
        String filePath = ADVISORS_FILE_PATH + university_email + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Advisor.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeAdvisor(Advisor advisor) {
        String filePath = ADVISORS_FILE_PATH + advisor.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    public ArrayList<Faculty> getAllFaculties() {
        // Read all faculties from the files
        ArrayList<Faculty> faculties = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(FACULTIES_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(FACULTIES_FILE_PATH + filePath)) {
                    faculties.add(gson.fromJson(reader, Faculty.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return faculties;
    }

    public void createOrChangeFaculty(Faculty faculty) {
        // Save faculty to the file
        String filePath = FACULTIES_FILE_PATH + faculty.getFacultyID().getFacultyName() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(faculty, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Faculty getFaculty(String facultyName) {
        // Read faculty from the file
        String filePath = FACULTIES_FILE_PATH + facultyName + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Faculty.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeFaculty(Faculty faculty) {
        String filePath = FACULTIES_FILE_PATH + faculty.getFacultyID().getFacultyName() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    public ArrayList<Department> getAllDepartments() {
        // Read all departments from the files
        ArrayList<Department> departments = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(DEPARTMENTS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(DEPARTMENTS_FILE_PATH + filePath)) {
                    departments.add(gson.fromJson(reader, Department.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return departments;
    }

    public void createOrChangeDepartment(Department department) {
        // Save department to the file
        String filePath = DEPARTMENTS_FILE_PATH + department.getDepartmentID().getDepartmentName() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(department, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Department getDepartment(String departmentName) {
        // Read department from the file
        String filePath = DEPARTMENTS_FILE_PATH + departmentName + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Department.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeDepartment(Department department) {
        String filePath = DEPARTMENTS_FILE_PATH + department.getDepartmentID().getDepartmentName() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    //helper methods and variables for generating random objects
    private final String[] names = {"Ali", "Fatma", "Zeynep", "Ahmet", "Ayse", "Mehmet", "Emine", "Hasan", "Huseyin", "Elif", "Mustafa", "Sibel", "Burak", "Busra", "Omer", "Halime", "Murat", "Gizem", "Eren", "Esra", "Yusuf", "Melis", "Can", "Hatice", "Oguz", "Rabia", "Kerem", "Derya", "Furkan", "Sevgi", "Kadir", "Selin", "Ibrahim", "Tugce", "Cem", "Pelin", "Baris", "Leyla", "Serkan", "Sule", "Deniz", "Cansu", "Hakan", "Damla", "Merve", "Tolga", "Ezgi", "Volkan", "Dilara", "Uğur", "Selma", "Ece", "Adem", "Zeynep", "Burcu", "Ozan", "Cemile", "Yasemin", "Alper", "Duygu", "Serdar", "Gul", "Okan", "Seda", "Bora", "Nurgul", "Cagri", "Seyma", "Dogukan", "Gulsah", "Tuna", "Hande", "Gokhan", "Berna", "Caner", "Bahar", "Arda", "Necla", "Batuhan", "Hilal", "Atakan", "Tulay", "Cengiz", "Berke", "Perihan", "Ece", "Tayfun", "Ceyda", "Emirhan", "Gonca", "Erdem", "Ayla", "Tamer", "Isil", "Havva", "Sevda", "Gokce", "Alime"};
    private final String[] surnames = {"Yilmaz", "Kaya", "Demir", "Celik", "Sahin", "Arslan", "Aydin", "Eren", "Ozturk", "Yildiz", "Aslan", "Keskin", "Polat", "Dogan", "Koc", "Gunes", "Aksoy", "Karaca", "Uzun", "Kilic", "Tas", "Candan", "Erdogan", "Gul", "Yalcin", "Balci", "Kaplan", "Can", "Durmaz", "Cetin", "Turkmen", "Simsek", "Duman", "Sari", "Saglam", "Ucar", "Kurt", "Ozdemir", "Isik", "Ersoy", "Soylu", "Korkmaz", "Bulut", "Kavak", "Turan", "Altun", "Ozkan", "Kara", "Gunduz", "Ates", "Yucel", "Erdem", "Keser", "Celikkan", "Toprak", "Yalman", "Ari", "Bayrak", "Deniz", "Durak", "Gultekin", "Orhan", "Aktas", "Sezer", "Pala", "Karatas", "Aksu", "Goksel", "Bozkurt", "Yuksel", "Albayrak", "Ozen", "Seker", "Erol", "Akcay", "Ozdem", "Arman", "Karahan", "Tunc", "Oztan", "Batur", "Tokgoz", "Acar", "Ergin", "Ulu", "Uz", "Altay", "Soydan", "Koroglu", "Torun", "Akbas", "Kalayci", "Koksal", "Tuna", "Akin", "Guler", "Erkan", "Gokce"};
    private final String[] cities = {"Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydin", "Balikesir", "Bartin", "Batman", "Bayburt", "Bilecik", "Bingol", "Bitlis", "Bolu", "Burdur", "Bursa", "Canakkale", "Cankiri", "Corum", "Denizli", "Diyarbakir", "Duzce", "Edirne", "Elazig", "Erzincan", "Erzurum", "Eskisehir", "Gaziantep", "Giresun", "Gumushane", "Hakkari", "Hatay", "Igdir", "Isparta", "Istanbul", "Izmir", "Kahramanmaras", "Karabuk", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kirikkale", "Kirklareli", "Kirsehir", "Kilis", "Kocaeli", "Konya", "Kutahya", "Malatya", "Manisa", "Mardin", "Mersin", "Mugla", "Mus", "Nevsehir", "Nigde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Sanliurfa", "Siirt", "Sinop", "Sirnak", "Sivas", "Tekirdag", "Tokat", "Trabzon", "Tunceli", "Usak", "Van", "Yalova", "Yozgat", "Zonguldak"};

    private String generateRandomName() {
        return names[(int) (Math.random() * names.length)];
    }

    private String generateRandomSurname() {
        return surnames[(int) (Math.random() * surnames.length)];
    }

    private String generateRandomCity() {
        return cities[(int) (Math.random() * cities.length)];
    }

    private String generateEmail(String name, String surname) {
        return name.toLowerCase() + surname.toLowerCase() + (int) (Math.random() * 1000) + "@gmail.com";
    }

    public String generateUniversityEmail(String name, String surname) {
        return name.toLowerCase() + surname.toLowerCase() + "@marun.edu.tr";
    }

    private String generatePhoneNumber() {
        String phoneNumber = "+90 5";
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10) + " ";
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10) + " ";
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10) + " ";
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10);
        return phoneNumber;
    }

    private String generatePassword(String name, String city, String phoneNumber) {
        return name.toLowerCase() + city.toUpperCase() + phoneNumber.substring(15);
    }

    private UserInformation generateRandomUserInformation() {
        String firstName = generateRandomName();
        String lastName = generateRandomSurname();
        String city = generateRandomCity();
        String phoneNumber = generatePhoneNumber();
        String password = generatePassword(firstName, city, phoneNumber);
        return new UserInformation(firstName, lastName, generateUniversityEmail(firstName, lastName), generateEmail(firstName, lastName), city, phoneNumber, LoginAuthService.hashPassword(password));
    }

    private Faculty generateFaculty(int FacultyID, String FacultyName) {
        return new Faculty(new FacultyID(FacultyID, FacultyName));
    }

    private Department generateDepartment(int DepartmentID, String DepartmentName, Faculty faculty) {
        Department d = new Department(new DepartmentID(DepartmentID, DepartmentName), faculty.getFacultyID());
        faculty.addDepartment(d);
        return d;
    }

    private Lecturer generateRandomLecturer(Department department) {
        UserInformation userInformation = generateRandomUserInformation();
        return new Lecturer(userInformation);
    }

    private Advisor generateRandomAdvisor(Department department) {
        UserInformation userInformation = generateRandomUserInformation();
        return new Advisor(userInformation);
    }

    public Student generateRandomStudent(Department department, int entrance_date, int entrance_rank, StaffId advisorID) {
        UserInformation userInformation = generateRandomUserInformation();
        StudentID studentID = new StudentID(department.getDepartmentID(), entrance_date, entrance_rank, department.get_facultyID());
        Transcript transcript = new Transcript(studentID);
        return new Student(userInformation, studentID, transcript, advisorID, 2024 - entrance_date + 1);
    }

    public Student generateNonRandomStudent(UserInformation userInformation, Department department, int entrance_date, int entrance_rank, StaffId advisorID) {
        StudentID studentID = new StudentID(department.getDepartmentID(), entrance_date, entrance_rank, department.get_facultyID());
        Transcript transcript = new Transcript(studentID);
        return new Student(userInformation, studentID, transcript, advisorID, 2024 - entrance_date + 1);
    }

    private CourseInformation generateCourseInformation(String courseName, String courseCode) {
        return new CourseInformation(courseName, courseCode);
    }

    private CourseRequirements generateCourseRequirements(ArrayList<CourseInformation> prerequisiteCourses, int minimumCurrentClass, FacultyID facultyID, DepartmentID departmentID) {
        return new CourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID);
    }

    public Course generateCourse(ArrayList<Lecturer> lecturersForSections, ArrayList<Day> days, ArrayList<SectionTime> sectionTimes, String courseName, String courseCode, ArrayList<CourseInformation> prerequisiteCourses, int minimumCurrentClass, FacultyID facultyID, DepartmentID departmentID) {
        CourseInformation courseInformation = generateCourseInformation(courseName, courseCode);
        CourseRequirements courseRequirements = generateCourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID);
        ArrayList<CourseSection> courseSections = new ArrayList<>();
        for (int i = 0; i < lecturersForSections.size(); i++) {
            CourseSection courseSection = new CourseSection(days.get(i), sectionTimes.get(i), lecturersForSections.get(i));
            courseSections.add(courseSection);
        }
        return new Course(courseInformation, courseRequirements, courseSections);
    }

}
