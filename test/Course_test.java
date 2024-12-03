import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Course_test {
    @Test
    public void calculateCourseScore_test() {
        CourseInformation courseInformation = new CourseInformation("test", "test");
        int midterm_score = 85;
        int final_score = 85;
        TakenCourse course = new TakenCourse(courseInformation, midterm_score, final_score);
        Score course_score = course.get_course_score();

        assertEquals(course_score, Score.BA, "The scores should be the same!");
    }

    @Test
    public void isStudentQualified_test() {
        DataManagement dataManagement = new DataManagement();
        Student student = dataManagement.getStudent("duyguates@marun.edu.tr");;
        Course course = dataManagement.getCourse("General Biology");
        CourseRequirements courseRequirements = course.getCourseRequirements();
        boolean[] trueAns = {true, true, true, true};
        boolean[] calculatedAns = courseRequirements.isStudentQualified(student);
        for(int i =0; i < trueAns.length; i++) {
            assertEquals(trueAns[i], calculatedAns[i], "Student is not qualified!");
        }
    }

    // we couldn't test checkPrerequisiteCourse method because it is a private method. But isStudentQualified method includes that method

}
