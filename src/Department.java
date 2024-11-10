package src;

import java.util.ArrayList;

public class Department {
    private final int _departmentID;
    private ArrayList<Unit> _units;
    private ArrayList<Course> _department_courses;

    public Department(int departmentID) {
        _departmentID = departmentID;
    }
    public int getDepartmentID() {
        return _departmentID;
    }
}
