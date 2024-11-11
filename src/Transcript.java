package src;

import java.util.ArrayList;

public class Transcript {

    private Student _student;
    private ArrayList<TakenCourse> _taken_courses;
    private float _GPA;

    Transcript(Student student) {
        this._student = student;
        this._taken_courses = new ArrayList<>();
        this._GPA = 0.0f;
    }

    public boolean addTakenCourse(TakenCourse tc) {
        if (tc != null) {
            _taken_courses.add(tc);
            calculateGPA();
            return true;
        }
        return false;
    }

    private void calculateGPA() {
        if (_taken_courses.isEmpty()) {
            _GPA = 0.0f;
            return;
        }
        float totalPoints = 0.0f;

        for (TakenCourse course : _taken_courses) {
            totalPoints += course.getCourseScore().getNumericValue();
        }

        _GPA = totalPoints / _taken_courses.size();
    }

    // getters
    public Student getStudent() {
        return _student;
    }

    public ArrayList<TakenCourse> getTakenCourses() {
        return _taken_courses;
    }

    public float getGPA() {
        return _GPA;
    }
}
