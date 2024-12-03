package src;

import java.util.ArrayList;
import java.util.Objects;

public class Course {
    private CourseInformation courseInformation;
    private CourseRequirements courseRequirements;
    private ArrayList<CourseSection> courseSections;

    public Course(CourseInformation courseInformation, CourseRequirements courseRequirements, ArrayList<CourseSection> courseSections) {
        this.courseInformation = courseInformation;
        this.courseRequirements = courseRequirements;
        this.courseSections = courseSections;
    }

    public String getCourseName() { // do not use this. Instead of use getter for courseInformation
        return getCourseInformation().getCourseName();
    }

    public CourseInformation getCourseInformation() {
        return courseInformation;
    }

    public CourseRequirements getCourseRequirements() {
        return courseRequirements;
    }

    public ArrayList<CourseSection> getCourseSections() {
        return courseSections;
    }
}

class CourseInformation {
    private final String courseName;
    private final String courseCode;

    CourseInformation(String courseName, String courseCode) {
        this.courseName = courseName;
        this.courseCode = courseCode;
    }

    public String getCourseCode() {
        return courseCode;
    }

    public String getCourseName() {
        return courseName;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        CourseInformation that = (CourseInformation) o;
        return Objects.equals(courseName, that.courseName) && Objects.equals(courseCode, that.courseCode);
    }

    @Override
    public int hashCode() {
        return Objects.hash(courseName, courseCode);
    }
}

class TakenCourse {
    private CourseInformation _courseInformation;
    private final int _midterm_score;
    private final int _final_score;
    private final Score _course_score;

    TakenCourse(CourseInformation courseInformation, int midtermScore, int finalScore) {
        _courseInformation = courseInformation;
        _midterm_score = midtermScore;
        _final_score = finalScore;
        _course_score = calculateCourseScore();
    }

    public CourseInformation get_courseInformation() {
        return _courseInformation;
    }


    private Score calculateCourseScore() {
        double total = _midterm_score * 0.6 + _final_score * 0.4;
        if (total >= 90) {
            return Score.AA;
        } else if (total >= 85) {
            return Score.BA;
        } else if (total >= 80) {
            return Score.BB;
        } else if (total >= 75) {
            return Score.CB;
        } else if (total >= 65) {
            return Score.CC;
        } else if (total >= 58) {
            return Score.DC;
        } else if (total >= 50) {
            return Score.DD;
        } else {
            return Score.FF;
        }
    }


    public Score get_course_score() {
        return _course_score;
    }

    public int get_midterm_score() {
        return _midterm_score;
    }

    public int get_final_score() {
        return _final_score;
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
    private ArrayList<CourseInformation> _prerequisite_courses;
    private final int _minimum_current_class;
    private final DepartmentID _departmentID;
    private final FacultyID _facultyID;

    public CourseRequirements(ArrayList<CourseInformation> prerequisiteCourses, int minimumCurrentClass, FacultyID faculty, DepartmentID department) { // constructor
        _prerequisite_courses = prerequisiteCourses;
        _minimum_current_class = minimumCurrentClass;
        _departmentID = department;
        _facultyID = faculty;
    }

    public boolean[] isStudentQualified(Student student) {
        boolean[] ans = new boolean[4]; //Year, department, faculty, prerequisites
        ans[0] = student.getCurrentClass() >= _minimum_current_class; // check current class
        ans[1] = _departmentID == null || _departmentID.getDepartmentID() == student.get_studentID().get_departmentID().getDepartmentID(); // check department
        ans[2] = _facultyID == null || _facultyID.getFacultyID() == student.get_studentID().get_facultyID().getFacultyID(); //check faculty
        ans[3] = checkPrerequisiteCourse(student);                                  // check prerequisite courses
        return ans;
    }

    private boolean checkPrerequisiteCourse(Student student) {// check prerequisite courses method
        if (_prerequisite_courses == null || _prerequisite_courses.isEmpty()) {
            return true;
        }
        for (CourseInformation courseInformation : _prerequisite_courses) {
            boolean check = false;
            for (TakenCourse takenCourse : student.getTranscript().getTakenCourses()) {
                if (takenCourse.get_courseInformation().equals(courseInformation)) { //branchleri birlşetirirken takenCourse getterının ismini aynı yap
                    check = true;
                    break;
                }
            }
            if (!check) {
                return false;
            }
        }
        return true;
    }//

    public DepartmentID get_departmentID() {
        return _departmentID;
    }

    public FacultyID get_facultyID() {
        return _facultyID;
    }

    public int get_minimum_current_class() {
        return _minimum_current_class;
    }
}

class CourseSection {                                                        // CourseSection class
    public Day _day;
    public SectionTime _sectionTime;
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
