package src;

public class Student extends User {
    private int _current_class;
    private StudentID _studentID;
    private Transcript _transcript;
    public Student(UserInformation userInformation, StudentID studentID) {
        super(userInformation);
        //
    }

    public boolean takeCourse() {
        return false;
    }
    //getters

}

class StudentID{
    private final int _departmentID;
    private final int _unitID;
    private final int _entrance_date;
    private final int _entrance_rank;
    private final String _ID;

    StudentID(Unit unit, int entrance_date, int entrance_rank) {
        _departmentID = unit.get_department().getDepartmentID();
        _unitID = unit.getUnitID();
        _entrance_date = entrance_date;
        _entrance_rank = entrance_rank;
        _ID = createStudentID();
    }

    private String createStudentID(){
        return "";
    }

    //getters
}