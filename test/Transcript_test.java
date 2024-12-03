import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Transcript_test {
    @Test
    public void calculateGPA_test() {
        DataManagement dataManagement = new DataManagement();
        Student student = dataManagement.getStudent("baristokgoz@marun.edu.tr");
        Transcript transcript = student.getTranscript();
        float trueGPA = 1.8125f;
        float calculatedGPA = transcript.get_GPA();
        assertEquals(trueGPA, calculatedGPA, "GPA should be the same!");


    }

}
