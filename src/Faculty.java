package src;

import java.util.ArrayList;

public class Faculty {                                          // Faculty class
    private final FacultyID _facultyID;
    private ArrayList<Department> _departments;

    public Faculty(FacultyID facultyID) {                       // constructor
        _facultyID = facultyID;
        _departments = new ArrayList<Department>();
    }
    public boolean addDepartment(Department department) {    // add department method
        _departments.add(department);
        return true;
    }
    public boolean removeDepartment(Department department) {   // remove department method
        _departments.remove(department);
        return true;
    }
    public FacultyID getFacultyID() {                           // faculty ID getter
        return _facultyID;
    }
}
class FacultyID {                                               // FacultyID class
    private final int _FacultyID;
    private final String _FacultyName;
    FacultyID(int facultyID,String facultyName ){                                     // constructor
        _FacultyName = facultyName;
        _FacultyID = facultyID;
    }
    public int getFacultyID() {                                 // getter
        return _FacultyID;
    }
    public String getFacultyName() {                            // getter
        return _FacultyName;
    }
}
