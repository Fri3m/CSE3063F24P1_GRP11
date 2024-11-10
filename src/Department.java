package src;

import java.util.ArrayList;

public class Department { // change as department
    private final DepartmentID _departmentID;
    private ArrayList<Lecturer> _lecturers;
    private ArrayList<Student> _students;
    private ArrayList<Course> _courses;
    private Faculty _faculty;

    public Department(DepartmentID departmentID) {
        _departmentID = departmentID;
    }

    public boolean addLecturer(Lecturer lecturer,User user) {
        return true;
    }
    public boolean addStudent(Student student,User user) {
        return true;
    }
    public boolean addCourse(Course course,User user) {
        return true;
    }
    public DepartmentID getDepartmentID() {
        return null;
    }
    public boolean removeLecturer(Lecturer lecturer,User user) {
        return true;
    }
    public boolean removeStudent(Student student,User user) {
        return true;
    }
    public boolean removeCourse(Course course,User user) {
        return true;
    }

    public Faculty getFaculty() {
        return _faculty;
    }
}
class DepartmentID {
    private final int _departmentID;
    public DepartmentID(int departmentID) {
        _departmentID = departmentID;
    }

    public int get_departmentID() {
        return _departmentID;
    }
}
