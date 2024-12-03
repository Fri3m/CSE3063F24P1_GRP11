

import java.util.ArrayList;

public class Transcript {
    private StudentID _studentId;
    private ArrayList<TakenCourse> _taken_courses;
    private float _GPA;

    Transcript(StudentID studentId){
        _studentId = studentId;
        _taken_courses = new ArrayList<TakenCourse>();
        _GPA = 0;
    }

    public boolean addTakenCourses(ArrayList<TakenCourse> takenCourses) {
        _taken_courses.addAll(takenCourses);
        calculateGPA();
        return true;
    }

    public boolean addTakenCourse(TakenCourse tc) {
        _taken_courses.add(tc);
        calculateGPA();
        return true;
    }

    private void calculateGPA(){
        _GPA = 0;
        if (_taken_courses.isEmpty()) {
            return;
        }
        for (TakenCourse tc : _taken_courses) {
            float x = switch (tc.get_course_score()) {
                case AA -> 4;
                case BA -> 3.5f;
                case BB -> 3;
                case CB -> 2.5f;
                case CC -> 2;
                case DC -> 1.5f;
                case DD -> 1;
                default -> 0;
            };
            _GPA += x;
        }
        _GPA /= _taken_courses.size();
    }

    //getters

    public ArrayList<TakenCourse> getTakenCourses() {
        return _taken_courses;
    }

    public float get_GPA() {
        calculateGPA();
        return _GPA;
    }
}

