package src;

import java.util.ArrayList;

public class CourseRegistrationService {
    private ArrayList<CourseRequest> _courseRequests = new ArrayList<CourseRequest>();

    public void createCourseRequest(Student student, Course course) {
        _courseRequests.add(new CourseRequest(student, course, student.get_advisorID()));

    }

    public ArrayList<CourseRequest> checkAccesiableRequests(Advisor advisor) {
        System.out.println(_courseRequests.size());
        ArrayList<CourseRequest> accessibleRequests = new ArrayList<CourseRequest>();

        for (CourseRequest courseRequest : _courseRequests) {
//            System.out.println("FORUN İÇİNDEYİM");
            if (courseRequest.get_advisorID().equals(advisor.get_staffId())) {
//                System.out.println("IF İÇİNDEYİM");
                accessibleRequests.add(courseRequest);
            }
        }

        return accessibleRequests;
    }
}

class CourseRequest {
    private final Student _student;
    private final Course _course;
    private final StaffId _advisorID;

    public CourseRequest(Student student, Course course, StaffId advisorID) {
        _student = student;
        _course = course;
        _advisorID = advisorID;
    }

    public Student get_student() {
        return _student;
    }

    public Course get_course() {
        return _course;
    }

    public StaffId get_advisorID() {
        return _advisorID;
    }
}