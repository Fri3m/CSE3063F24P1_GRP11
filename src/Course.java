package src;

import java.util.ArrayList;

public class Course {
    private String courseName;
    private String courseCode;
    private String courseDescription;
    private CourseRequirements courseRequirements;
    private ArrayList<CourseSection> courseSections;

    public boolean checkStudentQualification(Student student) {             // check student qualification method
        return courseRequirements.isStudentQualified(student);
    }

    public boolean changeLecturerOfCourseSection(CourseSection courseSection, Lecturer lecturer) {
        return courseSection.changeLecturer(lecturer);
    }

    public boolean addCourseSection(CourseSection courseSection) {
        courseSections.add(courseSection);
        return true;
    }

    public boolean removeCourseSection(CourseSection courseSection) {
        courseSections.remove(courseSection);
        return true;
    }

    public boolean equals(Course course) {
        if (this.courseName == course.courseName && this.courseCode == course.courseCode) {
            return true;
        } else {
            return false;
        }
    }
}

class TakenCourse {
    private Course _course;
    private int _midterm_score;
    private int _final_score;
    private Score _course_score;

    TakenCourse(Course course, int midtermScore, int finalScore) {

    }

    public Course getCourse() {
        return _course;
    }


    private void calculateCourseScore() {
        double total = _midterm_score * 0.6 + _final_score * 0.4;
        if (total >= 90) {
            _course_score = Score.AA;
        } else if (total >= 85) {
            _course_score = Score.BA;
        } else if (total >= 80) {
            _course_score = Score.BB;
        } else if (total >= 75) {
            _course_score = Score.CB;
        } else if (total >= 65) {
            _course_score = Score.CC;
        } else if (total >= 58) {
            _course_score = Score.DC;
        } else if (total >= 50) {
            _course_score = Score.DD;
        } else {
            _course_score = Score.FF;
        }
    }


    public Score get_course_score() {
        return _course_score;
    }
}

enum Score {
    AA,
    BA,
    BB,
    CB,
    CC,
    DC,
    DD,
    FF;
}

class CourseRequirements {
    private ArrayList<Course> _prerequisite_courses;
    private int _minimum_current_class;
    private Department _department;
    private Faculty _faculty;


    public boolean isStudentQualified(Student student) {
        if (student.getCurrentClass() < _minimum_current_class) {                     // check current class
            return false;
        }
        return checkPrerequisiteCourse(student);                                  // check prerequisite courses

    }

    public boolean checkPrerequisiteCourse(Student student) {// check prerequisite courses method

        for (Course course : _prerequisite_courses) {
            boolean check = false;
            for (TakenCourse takenCourse : student.getTranscript().getTakenCourses()) {
                if (takenCourse.getCourse().equals(course)) { //branchleri birlşetirirken takenCourse getterının ismini aynı yap
                    check = true;
                    break;
                }
            }
            if (!check) {
                return false;
            }
        }
        return true;
    }

}

class CourseSection {                                                        // CourseSection class
    private Day _day;
    private SectionTime _sectionTime;
    private Lecturer _lecturer;

    public CourseSection(Day day, SectionTime sectionTime, Lecturer lecturer) { // constructor
        _day = day;
        _sectionTime = sectionTime;
        _lecturer = lecturer;
    }

    boolean changeLecturer(Lecturer lecturer) {                              // change lecturer method
        _lecturer = lecturer;
        return true;
    }
}