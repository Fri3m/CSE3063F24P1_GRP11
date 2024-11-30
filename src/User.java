package src;

import java.util.ArrayList;
import java.util.Objects;


public class User {
    private UserInformation user_information;

    User(UserInformation user_information) {
        this.user_information = user_information;
    }

    public UserInformation getUserInformation() {
        return user_information;
    }

}

class Staff extends User {
    private StaffId _staffId;

    Staff(UserInformation user_information) {
        super(user_information);
        _staffId = new StaffId();
    }

    public StaffId get_staffId() {
        return _staffId;
    }
}

class StaffId {
    private final int _staffId;
    private static int _staffIdCounter = 1;

    public StaffId() {
        _staffId = generateStaffId();
    }

    private static int generateStaffId() {
        return _staffIdCounter++;
    }

    public int get_staffId() {
        return _staffId;
    }
    public static void changeStaticCounter(int newCounter) {
        if (newCounter > _staffIdCounter)
            _staffIdCounter = newCounter;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        StaffId staffId = (StaffId) o;
        return _staffId == staffId._staffId;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(_staffId);
    }
}

class Lecturer extends Staff {
    private DepartmentID _departmentID;
    private FacultyID _facultyID;

    public Lecturer(UserInformation user_information) {
        super(user_information);
    }

    public DepartmentID get_departmentID() {
        return _departmentID;
    }
}


class Advisor extends Lecturer {

    public Advisor(UserInformation user_information) {
        super(user_information);
    }

    public boolean checkCourseRequest(CourseRequest courseRequest) {
        CourseRequirements pre = courseRequest.get_course().getCourseRequirements();
        return pre.isStudentQualified(courseRequest.get_student());
    }

    public void approveCourseRequest(CourseRequest courseRequest) {
        courseRequest.get_student().get_current_courses().add(courseRequest.get_course());
    }
}


class Admin extends Staff { // Admin is a staff that can add or remove students from system
    public Admin(UserInformation user_information) {
        super(user_information);
    }
}

class DepartmentScheduler extends Staff {

    DepartmentScheduler(UserInformation user_information) {
        super(user_information);
    }

    public ArrayList<Course> returnCoursesForDepartment(ArrayList<Course> courses, Department department) {
        ArrayList<Course> departmentCourses = new ArrayList<Course>();
        for (Course course : courses) {
            if (course.getCourseRequirements().get_departmentID().getDepartmentName().equalsIgnoreCase(department.getDepartmentID().getDepartmentName())) {
                departmentCourses.add(course);
            }
        }
        return departmentCourses;
    }

    public void changeCourseSectionDayAndTime(CourseSection courseSection, Day day, SectionTime time) {
        courseSection._day = day;
        courseSection._sectionTime = time;
    }

}

class StudentsAffairs extends Staff {
    StudentsAffairs(UserInformation user_information) {
        super(user_information);
    }

    public boolean addCourse(Course course, ArrayList<Course> courses) {
        courses.add(course);
        return true;
    }

    public boolean removeCourse(Course course, ArrayList<Course> courses) {
        courses.remove(course);
        return true;
    }
}


























