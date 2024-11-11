package src;

import java.util.ArrayList;

public class CourseRegistrationService {
    private ArrayList<CourseRequest> _courseRequests;

    public void createCourseRequest(Student student, Course course) {
        _courseRequests.add(new CourseRequest(student, course, student.get_advisor()));
    }
    public ArrayList<CourseRequest> checkAccesiableRequests(Advisor advisor) {
        ArrayList<CourseRequest> accesiableRequests = new ArrayList<CourseRequest>();

        for (CourseRequest courseRequest : _courseRequests) {
            if (courseRequest.get_advisor().equals(advisor)) {
                accesiableRequests.add(courseRequest);
            }
        }

        return accesiableRequests;
    }
}

class CourseRequest{
    private Student _student;
    private Course _course;
    private Advisor _advisor;

    public CourseRequest(Student student, Course course, Advisor advisor){
        _student = student;
        _course = course;
        _advisor = advisor;
    }

    public Student get_student() {
        return _student;
    }

    public Course get_course() {
        return _course;
    }

    public Advisor get_advisor() {
        return _advisor;
    }
}