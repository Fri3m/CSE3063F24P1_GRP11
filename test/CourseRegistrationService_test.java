import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class CourseRegistrationService_test {
    @Test
    public void checkAccesiableRequests_test() {
        DataManagement dataManagement = new DataManagement();
        Advisor advisor = dataManagement.getAdvisor("hilalozkan@marun.edu.tr");
        Student student = dataManagement.getStudent("leylapala@marun.edu.tr");
        //courses
        CourseRegistrationService courseRegistrationService = new CourseRegistrationService();
        courseRegistrationService.createCourseRequest(student, dataManagement.getCourse("Fluid Mechanics"));
        courseRegistrationService.createCourseRequest(student, dataManagement.getCourse("Heat Transfer"));
        courseRegistrationService.createCourseRequest(student, dataManagement.getCourse("Material Sci."));
        ArrayList<CourseRequest> trueList = new ArrayList<>();
        trueList.add(new CourseRequest(student, dataManagement.getCourse("Fluid Mechanics"), student.get_advisorID()));
        trueList.add(new CourseRequest(student, dataManagement.getCourse("Heat Transfer"), student.get_advisorID()));
        trueList.add(new CourseRequest(student, dataManagement.getCourse("Material Sci."), student.get_advisorID()));

        ArrayList<CourseRequest> calculatedList = courseRegistrationService.checkAccesiableRequests(advisor);
        for (int i = 0; i < calculatedList.size(); i++) {
            assertEquals(trueList.get(i).get_course().getCourseName(), calculatedList.get(i).get_course().getCourseName());
        }
    }
}
