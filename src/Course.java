package src;

import java.util.ArrayList;

public class Course {

    private String courseName;
    private String courseCode;
    private String courseDescription;
    private CourseRequirements courseRequirements;
    private ArrayList<CourseSection> courseSections;

    public boolean checkStudentQualification(Student student) {
        return true;
    }

    public boolean changeLecturerOfCourseSection(CourseSection courseSection, Lecturer lecturer) {
        return true;
    }

    public boolean addCourseSection(CourseSection courseSection) {
        return true;
    }

    public boolean removeCourseSection(CourseSection courseSection) {
        return true;
    }
}

class TakenCourse {

    private Course _course;
    private int _midterm_score;
    private int _final_score;
    private Score _course_score;

    TakenCourse(Course course, int midtermScore, int finalScore) {
        this._course = course;
        this._midterm_score = midtermScore;
        this._final_score = finalScore;
        calculateCourseScore();
    }

    private void calculateCourseScore() {
        double weightedScore = (_midterm_score + _final_score) / 2;
        _course_score = determineLetterGrade(weightedScore);
    }

    private Score determineLetterGrade(double score) {
        if (score >= 90) {
            return Score.AA;
        } else if (score >= 85) {
            return Score.BA;
        } else if (score >= 80) {
            return Score.BB;
        } else if (score >= 75) {
            return Score.CB;
        } else if (score >= 70) {
            return Score.CC;
        } else if (score >= 65) {
            return Score.DC;
        } else if (score >= 60) {
            return Score.DD;
        } else {
            return Score.FF;
        }
    }

    public Score getCourseScore() {
        return _course_score;
    }

    public Course getCourse() {
        return _course;
    }

    public int getMidtermScore() {
        return _midterm_score;
    }

    public int getFinalScore() {
        return _final_score;
    }

}

enum Score {
    AA(4.0f),
    BA(3.5f),
    BB(3.0f),
    CB(2.5f),
    CC(2.0f),
    DC(1.5f),
    DD(1.0f),
    FF(0.0f);

    private final float numericValue;

    Score(float numericValue) {
        this.numericValue = numericValue;
    }

    public float getNumericValue() {
        return this.numericValue;
    }
}

class CourseRequirements implements FacultyOnlyCourse, DepartmentOnlyCourse {

    private ArrayList<Course> _prerequisite_courses;
    private int _minimum_current_class;

    public boolean isStudentQualified(Student student) {

        return true;
    }

    @Override
    public boolean isDepartmentOnly() {

        return false;
    }

    @Override
    public boolean checkDepartment(Student student) {
        return false;
    }

    @Override
    public boolean isFacultyOnly() {
        return false;
    }

    @Override
    public boolean checkFaculty(Student student) {
        return false;
    }
}

class CourseSection {

    private Day _day;
    private SectionTime _sectionTime;
    private Lecturer _lecturer;

    public CourseSection(Day day, SectionTime sectionTime, Lecturer lecturer) {
    }

    boolean changeLecturer(Lecturer lecturer) {
        return true;
    }
}

interface DepartmentOnlyCourse {

    Department DEPARTMENT = null;

    boolean isDepartmentOnly();

    boolean checkDepartment(Student student);
}

interface FacultyOnlyCourse {

    Faculty FACULTY = null;

    boolean isFacultyOnly();

    boolean checkFaculty(Student student);
}
