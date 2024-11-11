package src;

import java.util.ArrayList;

public class Faculty {                                          // Faculty class
    private final FacultyID _facultyID;
    private ArrayList<Department> _departments;
    private ArrayList<Course> _faculty_courses;

    public Faculty(FacultyID facultyID) {                       // constructor
        _facultyID = facultyID;
    }
    public boolean addDepartment(Department department,User user) {    // add department method
        _departments.add(department);
        return true;
    }
    public boolean addCourse(Course course,User user) {               // add course method
        _faculty_courses.add(course);
        return true;
    }
    public boolean removeDepartment(Department department,User user) {   // remove department method
        _departments.remove(department);
        return true;
    }
    public boolean removeCourse(Course course,User user) {              // remove course method
        _faculty_courses.remove(course);
        return true;
    }
    public FacultyID getFacultyID() {                           // faculty ID getter
        return _facultyID;
    }
    //getters
}
class FacultyID {                                               // FacultyID class
    private final int _FacultyID;

    FacultyID(int FacultyID){                                     // constructor
        _FacultyID = FacultyID;
    }
}
