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

class StaffId{
    private final int _staffId;
    private static int _staffIdCounter = 0;

    public StaffId() {
        _staffId = generateStaffId();
    }

    private static int generateStaffId() {
        return _staffIdCounter++;
    }

    public int get_staffId() {
        return _staffId;
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
}

class Advisor extends Lecturer{
    private ArrayList<StudentID> _advisor_students;
    public Advisor(UserInformation user_information) {
        super(user_information);
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


    private boolean checkCourseRequest(CourseRequest courseRequest){
        CourseRequirements pre = courseRequest.get_course().getCourseRequirements();
        return pre.isStudentQualified(courseRequest.get_student());

    }
}



