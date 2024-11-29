package src;

import java.util.ArrayList;

public class Student extends User {
    private int _current_class;
    private StudentID _studentID;
    private Transcript _transcript;
    private StaffId _advisorID;
    private ArrayList<Course> _current_courses;


    public Student(UserInformation userInformation, StudentID studentID, Transcript transcript, StaffId advisorID, int current_class) {
        super(userInformation);
        _studentID = studentID;
        _transcript = transcript;
        _advisorID = advisorID;
        _current_class = current_class;
        _current_courses = new ArrayList<Course>();
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


    public StudentID get_studentID() {
        return _studentID;
    }

    public StaffId get_advisorID() {
        return _advisorID;
    }


    public ArrayList<Course> get_current_courses() {
        return _current_courses;
    }
}


class StudentID {
    private final DepartmentID _departmentID;
    private final FacultyID _facultyID;
    private final int _entrance_date; // in format of YYYY
    private final int _entrance_rank; // the rank of the student in the entrance exam
    private final String _ID;

    StudentID(DepartmentID departmentID, int entrance_date, int entrance_rank, FacultyID facultyID) {
        _departmentID = departmentID;
        _entrance_date = entrance_date;
        _entrance_rank = entrance_rank;
        _facultyID = facultyID;
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

    public FacultyID get_facultyID() {
        return _facultyID;
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
