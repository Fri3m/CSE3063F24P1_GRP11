package src;

import java.util.ArrayList;

public class Student extends User {
    private int _current_class;
    private StudentID _studentID;
    private Transcript _transcript;
    private Department _department;
    private ArrayList<Course> _current_courses;

    public Student(UserInformation userInformation, StudentID studentID) {
        super(userInformation);
        //
    }

    public Transcript getTranscript() {    //getter
        return _transcript;
    }

    public Department getDepartment() {    //getter
        return _department;
    }
    public int getCurrentClass() {    //getter
        return _current_class;
    }

    public boolean takeCourse() {
        return false;
    }

    //getters
}

class StudentID{
    private final FacultyID _facultyID;
    private final DepartmentID _departmentID;
    private final int _entrance_date;
    private final int _entrance_rank;
    private final String _ID;

    StudentID(Department department, int entrance_date, int entrance_rank) {
        _facultyID = department.getFaculty().getFacultyID();
        _departmentID = department.getDepartmentID();
        _entrance_date = entrance_date;
        _entrance_rank = entrance_rank;
        _ID = createStudentID();
    }

    private String createStudentID(){
        return "";
    }

    //getters
}