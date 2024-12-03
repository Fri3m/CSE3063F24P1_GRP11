

import java.util.ArrayList;

public class Department {    // Department class
    private final DepartmentID _departmentID;
    private ArrayList<Lecturer> _lecturers;
    private FacultyID _facultyID;

    public Department(DepartmentID departmentID, FacultyID facultyID) {                      // constructor
        _departmentID = departmentID;
        _facultyID = facultyID;
    }

    public boolean addLecturer(Lecturer lecturer) {           // add lecturer method
        _lecturers.add(lecturer);
        return true;
    }
    public DepartmentID getDepartmentID() {                             // get department ID method
        return _departmentID;
    }
    public boolean removeLecturer(Lecturer lecturer,User user) {        // remove lecturer method
        _lecturers.remove(lecturer);
        return true;
    }

    public FacultyID get_facultyID() {
        return _facultyID;
    }

}
class DepartmentID {                                    // DepartmentID class
    private final int _departmentID;
    private final String _departmentName;
    public DepartmentID(int departmentID, String departmentName) {    // constructor
        _departmentID = departmentID;
        _departmentName = departmentName;
    }
    public String getDepartmentName() {                     //department name getter
        return _departmentName;
    }
    public int getDepartmentID() {                     //department ID getter
        return _departmentID;
    }
}
