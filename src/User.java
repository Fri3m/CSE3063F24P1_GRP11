package src;

import java.lang.reflect.Array;
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

    public boolean checkRegistration(CourseRegistrationService courseRegistrationService) {
        ArrayList<CourseRequest> courseRequests= courseRegistrationService.checkAccesiableRequests(this);
        for(CourseRequest courseRequest: courseRequests){
           System.out.println(courseRequest.get_student().getUserInformation().get_FIRST_NAME() + " wants to take " + courseRequest.get_course().getCourseName());
           boolean x = checkCourseRequest(courseRequest);
              if(x){
                System.out.println("The request is accepted");
                return true;
              }
              else{
                System.out.println("The request is rejected");
                return false;
              }
        }


        System.out.println("There is no request");
       return false;
    }
    public boolean equals(Advisor advisor){
        return this.getUserInformation().get_email().equals(advisor.getUserInformation().get_email());
    }


    private boolean checkCourseRequest(CourseRequest courseRequest){
        CourseRequirements pre = courseRequest.get_course().getCourseRequirements();
        return pre.isStudentQualified(courseRequest.get_student());

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


