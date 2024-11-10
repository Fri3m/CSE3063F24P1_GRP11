package src;

import java.util.ArrayList;

public class Department {    // Department class
    private final DepartmentID _departmentID;
    private ArrayList<Lecturer> _lecturers;
    private ArrayList<Student> _students;
    private ArrayList<Course> _courses;
    private Faculty _faculty;

    public Department(DepartmentID departmentID) {                      // constructor
        _departmentID = departmentID;
    }

    public boolean addLecturer(Lecturer lecturer,User user) {           // add lecturer method
        _lecturers.add(lecturer);
        return true;
    }
    public boolean addStudent(Student student,User user) {              // add student method
        _students.add(student);
        return true;
    }
    public boolean addCourse(Course course,User user) {                 // add course method
        _courses.add(course);
        return true;
    }
    public DepartmentID getDepartmentID() {                             // get department ID method
        return _departmentID;
    }
    public boolean removeLecturer(Lecturer lecturer,User user) {        // remove lecturer method
        _lecturers.remove(lecturer);
        return true;
    }
    public boolean removeStudent(Student student,User user) {           // remove student method
        _students.remove(student);
        return true;
    }
    public boolean removeCourse(Course course,User user) {          // remove course method
        _courses.remove(course);
        return true;
    }

    public Faculty getFaculty() {                       // get faculty method
        return _faculty;
    }
}
class DepartmentID {                                    // DepartmentID class
    private final int _departmentID;
    public DepartmentID(int departmentID) {
        _departmentID = departmentID;
    }

    public int getDepartmentID() {                     //department ID getter
        return _departmentID;
    }
}
