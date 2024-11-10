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
    public boolean changeLecturerOfCourseSection(CourseSection courseSection,Lecturer lecturer){
        return true;
    }
    public boolean addCourseSection(CourseSection courseSection){
        return true;
    }
    public boolean removeCourseSection(CourseSection courseSection){
        return true;
    }
}

class TakenCourse{
    private Course _course;
    private int _midterm_score;
    private int _final_score;
    private Score _course_score;

    TakenCourse(Course course, int midtermScore, int finalScore){

    }

    private void calculateCourseScore(){

    }


    public Score get_course_score() {
        return _course_score;
    }
}

enum Score{
    AA,
    BA,
    BB,
    CB,
    CC,
    DC,
    DD,
    FF;
}

class CourseRequirements implements FacultyOnlyCourse, DepartmentOnlyCourse {
    private ArrayList<Course> _prerequisite_courses;
    private int _minimum_current_class;

    public boolean isStudentQualified(Student student){
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

class CourseSection{
    private Day _day;
    private SectionTime _sectionTime;
    private Lecturer _lecturer;
    public CourseSection(Day day, SectionTime sectionTime, Lecturer lecturer) {}

    boolean changeLecturer(Lecturer lecturer){
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
