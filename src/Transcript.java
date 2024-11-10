package src;

import java.util.ArrayList;

public class Transcript {
    private Student _student;
    private ArrayList<TakenCourse> _taken_courses;
    private float _GPA;

    public ArrayList<TakenCourse> getTakenCourses() {
        return _taken_courses;
    }
    Transcript(Student student){
        _student = student;
    }

    public boolean addTakenCourse(TakenCourse tc) {
        return true;
    }

    private void calculateGPA(){
    }

    //getters
}

