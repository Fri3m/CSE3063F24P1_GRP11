package src;

import java.util.ArrayList;

public class Course {                                                   // Course class
    private String courseName;
    private String courseCode;
    private String courseDescription;
    private CourseRequirements courseRequirements;
    private ArrayList<CourseSection> courseSections;

    public boolean checkStudentQualification(Student student) {             // check student qualification method
        return courseRequirements.isStudentQualified(student);
    }
    public boolean changeLecturerOfCourseSection(CourseSection courseSection,Lecturer lecturer){
        return courseSection.changeLecturer(lecturer);
    }
    public boolean addCourseSection(CourseSection courseSection){
        courseSections.add(courseSection);
        return true;
    }
    public boolean removeCourseSection(CourseSection courseSection){
        courseSections.remove(courseSection);
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
        double total = _midterm_score * 0.6 + _final_score * 0.4;
        if(total >= 90){
            _course_score = Score.AA;
        }else if(total >= 85){
            _course_score = Score.BA;
        }else if(total >= 80){
            _course_score = Score.BB;
        }else if(total >= 75){
            _course_score = Score.CB;
        }else if(total >= 65){
            _course_score = Score.CC;
        }else if(total >= 58){
            _course_score = Score.DC;
        }else if(total >= 50){
            _course_score = Score.DD;
        }else{
            _course_score = Score.FF;
        }
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
    private Department _department;
    private Faculty _faculty;
    private boolean isDepartmentOnly;
    private boolean isFacultyOnly;


    public boolean isStudentQualified(Student student){
        if(student.getCurrentClass() < _minimum_current_class){                     // check current class
            return false;
        } else if(isDepartmentOnly && checkDepartment(student) != _department) {    // check department
            return false;
        } else if(isFacultyOnly && checkFaculty(student) != _faculty) {             // check faculty
            return false;
        } return checkPrerequisiteCourse(student);                                  // check prerequisite courses

    }
    public boolean checkPrerequisiteCourse(Student student){                        // check prerequisite courses method
        for(Course course : _prerequisite_courses){
            boolean isTaken = false;
            for(TakenCourse takenCourse : student.getTranscript().getTakenCourses()){
                if(takenCourse.equals(course)){
                    isTaken = true;
                    break;
                }
            }
            if(!isTaken){
                return false;
            }
        }
        return true;
    }
    @Override
    public Department checkDepartment(Student student) {                      // check department method
        return student.getDepartment();
    }
    public boolean isDepartmentOnly() {                                     // is department only method
        return isDepartmentOnly;
    }
    public void makeDepartmentOnly() {                                      // make department only method
        isDepartmentOnly = true;
    }

    @Override
    public Faculty checkFaculty(Student student) {                          // check faculty method
        return student.getDepartment().getFaculty();
    }
    public boolean isFacultyOnly() {                                        // is faculty only method
        return isFacultyOnly;
    }
    public void makeFacultyOnly() {                                         // make faculty only method
        isFacultyOnly = true;
    }
}

class CourseSection{                                                        // CourseSection class
    private Day _day;
    private SectionTime _sectionTime;
    private Lecturer _lecturer;
    public CourseSection(Day day, SectionTime sectionTime, Lecturer lecturer) { // constructor
        _day = day;
        _sectionTime = sectionTime;
        _lecturer = lecturer;
    }

    boolean changeLecturer(Lecturer lecturer){                              // change lecturer method
        _lecturer = lecturer;
        return true;
    }
}

interface DepartmentOnlyCourse {                                            // DepartmentOnlyCourse interface
    Department DEPARTMENT = null;
    boolean isDepartmentOnly = false;
    Department checkDepartment(Student student);
}
interface FacultyOnlyCourse {                                               // FacultyOnlyCourse interface
    Faculty FACULTY = null;
    boolean isFacultyOnly = false;
    Faculty checkFaculty(Student student);
}
