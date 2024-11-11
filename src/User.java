package src;

import java.util.ArrayList;


public abstract class User {
    private UserInformation user_information;
    public User(UserInformation user_information) {
        this.user_information = user_information;
    }

    public UserInformation getUserInformation() {
        return user_information;
    }
}

abstract class Staff extends User {
    private StaffID _staffID;

    public Staff(UserInformation user_information) {
        super(user_information);
    }
}

class Lecturer extends Staff {
    private ArrayList<Course> _courses;
    private Department _department;
    public Lecturer(UserInformation user_information) {
        super(user_information);
    }
    public boolean addCourse(Course course) {
        return true;
    }
    public boolean removeCourse(Course course) {
        return true;
    }
}

class Advisor extends Lecturer{
    private ArrayList<Student> _advisor_students;
    public Advisor(UserInformation user_information) {
        super(user_information);
    }

    public boolean addStudentToAdvisor(Student student) {
        if (student.get_advisor() != null) {
            System.out.println("The student already has an advisor.");
            return false;
        }
        return true;
    }

    public boolean removeStudentToAdvisor(Student student) {
        return true;
    }

    public boolean checkRegistration(Student student, Course course) {
        // 1. Check if the student is assigned to the advisor
        if (!_advisor_students.contains(student)) {
            System.out.println("The student does not belong to this advisor.");
            return false;
        }

        if (!course.checkStudentQualification(student)) {
            System.out.println("The student does not meet the course requirements.");
            return false;
        }

        System.out.println("Registration completed successfully.");
        return true;
    }





    private boolean checkCourseRequest(CourseRequest courseRequest){


        return true;
    }
}

class StaffID{ // check this class logic again
    private static int lastID = 0;
    private final int _id;
    public StaffID() {
        this._id = StaffID.generateNewUniqueID();
    }
    private static int generateNewUniqueID(){
        return ++lastID;
    }
}


