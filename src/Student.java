package src;

import java.util.ArrayList;

public class Student extends User {
    private int _current_class;
    private StudentID _studentID;
    private Transcript _transcript;
    private Advisor _advisor;
    private ArrayList<Course> _current_courses;

    // Mevcut danışmanı ayarlar
    public void set_advisor(Advisor advisor) {
        this._advisor = advisor;
    }
    private ArrayList<TakenCourse> _taken_courses_for_transcript; // this variable is for the transcript creation for the student who has already taken courses never add anything to this variable

    public Student(UserInformation userInformation, StudentID studentID) {
        this(userInformation, studentID, 1, new ArrayList<Course>());
    }

    public Student(UserInformation userInformation, StudentID studentID, int current_class, ArrayList<Course> current_courses) {
        super(userInformation);
        _studentID = studentID;
        _current_class = current_class;
        _advisor = new Advisor(new UserInformation("test", "test", "test")); // get the advisor of the department
        _current_courses = current_courses;
        _taken_courses_for_transcript = new ArrayList<TakenCourse>();
    }

    public Student(UserInformation userInformation, StudentID studentID, int current_class, ArrayList<Course> current_courses, ArrayList<TakenCourse> taken_courses) {
        this(userInformation, studentID, current_class, current_courses);
        _taken_courses_for_transcript = taken_courses;
    }

    public boolean takeCourse(Course course, CourseRegistrationService courseRegistrationService) {
        courseRegistrationService.createCourseRequest(this, course);
        return true;
    }

    public Transcript getTranscript() {    //getter
        return _transcript;
    }

    public int getCurrentClass() {    //getter
        return _current_class;
    }

    public boolean takeCourse() {
        return false;
    }

//getters

    public int get_current_class() {
        return _current_class;
    }

    public StudentID get_studentID() {
        return _studentID;
    }

    public Advisor get_advisor() {
        return _advisor;
    }

    public Transcript get_transcript() {
        return _transcript;
    }

    public ArrayList<Course> get_current_courses() {
        return _current_courses;
    }
}


class StudentID {
    private final DepartmentID _departmentID;
    private final int _entrance_date; // in format of YYYY
    private final int _entrance_rank; // the rank of the student in the entrance exam
    private final String _ID;

    StudentID(DepartmentID departmentID, int entrance_date, int entrance_rank) {
        _departmentID = departmentID;
        _entrance_date = entrance_date;
        _entrance_rank = entrance_rank;
        _ID = createStudentID();
    }

    private String createStudentID() {
        String first_part = _departmentID.getDepartmentID() + ""; // assumes that departmentID is unique and 3 characters
        String second_part = _entrance_date + "";
        second_part = second_part.substring(1); // assumes the _entrance_date is format of YYYY and get the last 3 digits of the year. ex: 2024->024
        StringBuilder third_part = new StringBuilder(_entrance_rank + "");
        while (third_part.length() < 3) {
            third_part.insert(0, "0");
        }
        return first_part + second_part + third_part;
    }

//    public static void main(String[] args) {
//        Student student = new Student(new UserInformation("name", "surname", "email"), new StudentID(new Department(new DepartmentID(100)), 2024, 1));
//        student.initialize();
//        System.out.println(student.get_studentID().get_ID());
//        System.out.println(student.get_studentID().get_department().get_students().get(0).get_studentID().get_ID());
//    }

    //getters


    public DepartmentID get_departmentID() {
        return _departmentID;
    }

    public int get_entrance_date() {
        return _entrance_date;
    }

    public int get_entrance_rank() {
        return _entrance_rank;
    }

    public String get_ID() {
        return _ID;
    }
}
