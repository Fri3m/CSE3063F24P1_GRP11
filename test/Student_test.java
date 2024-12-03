import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class Student_test {
    @Test
    public void createStudentID_test() {
        DataManagement dataManagement = new DataManagement();
        Student student = dataManagement.getStudent("baristokgoz@marun.edu.tr");
        DepartmentID departmentID = dataManagement.getDepartment("ComputerEngineering").getDepartmentID();
        FacultyID facultyID = dataManagement.getFaculty("Engineering").getFacultyID();
        StudentID studentID = student.get_studentID();
        assertEquals(studentID.get_departmentID().getDepartmentName(), "ComputerEngineering", "Department name should be the same!");
        assertEquals(studentID.get_facultyID().getFacultyName(), "Engineering", "Faculty name should be the same!");
        assertEquals(studentID.get_entrance_date(), 2021, "Entrance date should be the same!");
        assertEquals(studentID.get_entrance_rank(), 70, "Entrance rank should be the same!");

    }
}


