package src;

import java.util.ArrayList;

public class Faculty { // change as faculty
    private final FacultyID _facultyID;
    private ArrayList<Department> _departments;
    private ArrayList<Course> _faculty_courses;

    public Faculty(FacultyID facultyID) {
        _facultyID = facultyID;
    }
    public FacultyID getFacultyID() {
        return _facultyID;
    }
    //getters
}
class FacultyID {
    private final int _FacultyID;

    FacultyID(int FacultyID) {
        _FacultyID = FacultyID;
    }
}
