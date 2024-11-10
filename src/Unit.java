package src;

import java.util.ArrayList;

public class Unit {
    private final int _unitID;
    private ArrayList<Lecturer> _lecturers;
    private ArrayList<Student> _students;
    private ArrayList<Course> _courses;
    private Department _department;

    public Unit(int unitID) {
        _unitID = unitID;
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
    public int getUnitID() {
        return 1;
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

    public Department get_department() {
        return _department;
    }
}
