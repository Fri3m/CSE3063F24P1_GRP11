package src;

import com.google.gson.Gson;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class DataManagement {

    private final String STUDENTS_FILE_PATH = "data/students/";
    private final String COURSES_FILE_PATH = "data/courses/";
    private final String LECTURERS_FILE_PATH = "data/lecturers/";
    private final String ADVISORS_FILE_PATH = "data/advisors/";
    private final String FACULTIES_FILE_PATH = "data/faculties/";
    private final String DEPARTMENTS_FILE_PATH = "data/departments/";
    private final String DEPARTMENT_SCHEDULERS_FILE_PATH = "data/departmentSchedulers/";
    private final String STUDENTS_AFFAIRS_FILE_PATH = "data/studentsAffairs/";

    private final Gson gson = new Gson();

    public static void main(String[] args) {
//        DataManagement dataManagement = new DataManagement();

//        Faculty engineering = dataManagement.generateFaculty(1, "Engineering");
//        dataManagement.createOrChangeFaculty(engineering);
//
//        Department computerEngineering = dataManagement.generateDepartment(150, "ComputerEngineering", engineering);
//        dataManagement.createOrChangeDepartment(computerEngineering);
//
//
//        Advisor advisor = dataManagement.generateRandomAdvisor(computerEngineering);
//
//        Lecturer lecturer = dataManagement.generateRandomLecturer(computerEngineering);
//        Lecturer lecturer3 = dataManagement.generateRandomLecturer(computerEngineering);
//
//        dataManagement.createOrChangeAdvisor(advisor);
//        dataManagement.createOrChangeLecturer(lecturer);
//        dataManagement.createOrChangeLecturer(lecturer3);
//
//        ArrayList<Lecturer> lecturersForSections = new ArrayList<>();
//        lecturersForSections.add(lecturer);
//        lecturersForSections.add(lecturer);
//        lecturersForSections.add(lecturer);
//        ArrayList<Day> days = new ArrayList<>();
//        days.add(Day.Monday);
//        days.add(Day.Monday);
//        days.add(Day.Thursday);
//        ArrayList<SectionTime> sectionTimes = new ArrayList<>();
//        sectionTimes.add(SectionTime.Fifth);
//        sectionTimes.add(SectionTime.Sixth);
//        sectionTimes.add(SectionTime.Fifth);
//        Course course = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Introduction to CS", "CS101", new ArrayList<>(), 1, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
//        dataManagement.createOrChangeCourse(course);
//
//        lecturersForSections.clear();
//        lecturersForSections.add(lecturer);
//        lecturersForSections.add(lecturer3);
//        lecturersForSections.add(lecturer3);
//        days.clear();
//        days.add(Day.Tuesday);
//        days.add(Day.Wednesday);
//        days.add(Day.Thursday);
//        sectionTimes.clear();
//        sectionTimes.add(SectionTime.Fifth);
//        sectionTimes.add(SectionTime.First);
//        sectionTimes.add(SectionTime.Fifth);
//
//        ArrayList<CourseInformation> prerequisites = new ArrayList<>();
//        prerequisites.add(course.getCourseInformation());
//
//        Course course1 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Random", "XX001", prerequisites, 1, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
//        dataManagement.createOrChangeCourse(course1);
//
//
//        Student student1 = dataManagement.generateRandomStudent(computerEngineering, 2020, 5, advisor.get_staffId());
//        Student student2 = dataManagement.generateRandomStudent(computerEngineering, 2021, 5, advisor.get_staffId());
//        Student student3 = dataManagement.generateRandomStudent(computerEngineering, 2024, 5, advisor.get_staffId());
//
//        dataManagement.createOrChangeStudent(student1);
//        dataManagement.createOrChangeStudent(student1);
//        dataManagement.createOrChangeStudent(student2);
//        dataManagement.createOrChangeStudent(student3);
//
//        TakenCourse takenCourse = new TakenCourse(course1.getCourseInformation(), 90, 54);
//        student1.getTranscript().addTakenCourse(takenCourse);
//        dataManagement.createOrChangeStudent(student1);
//
//        DepartmentScheduler departmentScheduler = dataManagement.generateRandomDepartmentScheduler(computerEngineering);
//        dataManagement.createOrChangeDepartmentScheduler(departmentScheduler);
//
//        StudentsAffairs studentsAffairs = dataManagement.generateRandomStudentsAffairs(computerEngineering);
//        dataManagement.createOrChangeStudentsAffairs(studentsAffairs);

        //yıldırım

        DataManagement dataManagement = new DataManagement();

        Faculty engineering = dataManagement.generateFaculty(1, "Engineering");
        dataManagement.createOrChangeFaculty(engineering);

        Faculty science = dataManagement.generateFaculty(2, "Science");
        dataManagement.createOrChangeFaculty(science);


        Department computerEngineering = dataManagement.generateDepartment(150, "ComputerEngineering", engineering);
        dataManagement.createOrChangeDepartment(computerEngineering);

        Department mechanicalEngineering = dataManagement.generateDepartment(151, "MechanicalEngineering", engineering);
        dataManagement.createOrChangeDepartment(mechanicalEngineering);

        Department electricalEngineering = dataManagement.generateDepartment(152, "ElectricalEngineering", engineering);
        dataManagement.createOrChangeDepartment(electricalEngineering);

        Department biology = dataManagement.generateDepartment(153, "Biology", science);
        dataManagement.createOrChangeDepartment(biology);

        Department chemistry = dataManagement.generateDepartment(154, "Chemistry", science);
        dataManagement.createOrChangeDepartment(chemistry);


        Advisor advisor = dataManagement.generateRandomAdvisor(computerEngineering);


        Lecturer lecturer = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer2 = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer3 = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer4 = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer5 = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer6 = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer7 = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer8 = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer9 = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer10 = dataManagement.generateRandomLecturer(computerEngineering);
        Lecturer lecturer11 = dataManagement.generateRandomLecturer(computerEngineering);


        dataManagement.createOrChangeAdvisor(advisor);
        dataManagement.createOrChangeLecturer(lecturer);
        dataManagement.createOrChangeLecturer(lecturer3);
        dataManagement.createOrChangeLecturer(lecturer2);
        dataManagement.createOrChangeLecturer(lecturer4);
        dataManagement.createOrChangeLecturer(lecturer5);
        dataManagement.createOrChangeLecturer(lecturer6);
        dataManagement.createOrChangeLecturer(lecturer7);
        dataManagement.createOrChangeLecturer(lecturer8);
        dataManagement.createOrChangeLecturer(lecturer9);
        dataManagement.createOrChangeLecturer(lecturer10);
        dataManagement.createOrChangeLecturer(lecturer11);

        ArrayList<Lecturer> lecturersForSections = new ArrayList<>();
        lecturersForSections.add(lecturer);
        lecturersForSections.add(lecturer);
        lecturersForSections.add(lecturer);
        ArrayList<Day> days = new ArrayList<>();
        days.add(Day.Monday);
        days.add(Day.Monday);
        days.add(Day.Wednesday);
        ArrayList<SectionTime> sectionTimes = new ArrayList<>();
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Fifth);


        Course course = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Introduction to Computer Engineering", "CS1200", new ArrayList<>(), 1, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer2);
        lecturersForSections.add(lecturer2);
        lecturersForSections.add(lecturer2);
        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Tuesday);
        days.add(Day.Thursday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Fourth);
        sectionTimes.add(SectionTime.First);


        Course course1 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Computer Programming", "CSE1241", new ArrayList<>(), 1, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course1);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer3);
        lecturersForSections.add(lecturer3);
        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Sixth);

        Course course2 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Linear Algebra for Computer Engineering", "MATH256", new ArrayList<>(), 1, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course2);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer2);
        lecturersForSections.add(lecturer2);
        lecturersForSections.add(lecturer2);
        days.clear();
        days.add(Day.Monday);
        days.add(Day.Monday);
        days.add(Day.Tuesday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Fifth);
        sectionTimes.add(SectionTime.Sixth);
        sectionTimes.add(SectionTime.Third);

        ArrayList<CourseInformation> prerequisites = new ArrayList<>();
        prerequisites.add(course1.getCourseInformation());

        Course course3 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Data Structures", "CS2225", prerequisites, 2, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course3);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer3);
        lecturersForSections.add(lecturer3);
        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.First);

        Course course4 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Differential Equations", "MATH205", new ArrayList<>(), 2, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course4);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer4);
        lecturersForSections.add(lecturer4);
        days.clear();
        days.add(Day.Thursday);
        days.add(Day.Thursday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Sixth);
        sectionTimes.add(SectionTime.Seventh);
        sectionTimes.add(SectionTime.Fourth);

        Course course5 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Systems Programming", "CS2138", new ArrayList<>(), 2, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course5);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer5);
        lecturersForSections.add(lecturer5);
        lecturersForSections.add(lecturer5);
        days.clear();
        days.add(Day.Monday);
        days.add(Day.Monday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.First);

        ArrayList<CourseInformation> prerequisites1 = new ArrayList<>();
        prerequisites1.add(course3.getCourseInformation());

        Course course6 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Database Systems", "CS3125", prerequisites1, 3, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course6);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer6);
        lecturersForSections.add(lecturer6);
        lecturersForSections.add(lecturer6);
        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Wednesday);
        days.add(Day.Wednesday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Seventh);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);

        ArrayList<CourseInformation> prerequisites2 = new ArrayList<>();
        prerequisites2.add(course6.getCourseInformation());

        Course course7 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Software Engineering", "CS3044", prerequisites2, 3, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course7);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer);
        lecturersForSections.add(lecturer);
        days.clear();
        days.add(Day.Thursday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Fifth);

        Course course8 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Digital Logic Design", "CS3215", new ArrayList<>(), 3, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course8);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer7);
        lecturersForSections.add(lecturer7);
        lecturersForSections.add(lecturer7);
        days.clear();
        days.add(Day.Monday);
        days.add(Day.Wednesday);
        days.add(Day.Wednesday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Second);

        Course course9 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Computer Networks", "CS4074", new ArrayList<>(), 4, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course9);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer6);
        lecturersForSections.add(lecturer6);
        lecturersForSections.add(lecturer6);
        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Friday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Second);

        ArrayList<CourseInformation> prerequisites3 = new ArrayList<>();
        prerequisites3.add(course2.getCourseInformation());

        Course course10 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Introduction to Machine Learning", "CSE4288", prerequisites3, 4, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course10);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer7);
        lecturersForSections.add(lecturer7);
        days.clear();
        days.add(Day.Thursday);
        days.add(Day.Thursday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Fifth);
        sectionTimes.add(SectionTime.Sixth);

        Course course11 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Cloud Computing", "CS4012", new ArrayList<>(), 4, computerEngineering.get_facultyID(), computerEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course11);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer8);
        lecturersForSections.add(lecturer8);
        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Third);

        Course course12 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Mechatronics", "ME3022", new ArrayList<>(), 4, mechanicalEngineering.get_facultyID(), mechanicalEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course12);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer9);
        lecturersForSections.add(lecturer9);
        days.clear();
        days.add(Day.Monday);
        days.add(Day.Monday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);

        Course course13 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Planning and Management of Research", "BIOE4072", new ArrayList<>(), 4, biology.get_facultyID(), biology.getDepartmentID());
        dataManagement.createOrChangeCourse(course13);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer10);
        lecturersForSections.add(lecturer10);
        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Tuesday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Fifth);
        sectionTimes.add(SectionTime.Sixth);

        Course course14 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Financial Engineering", "CHE4068", new ArrayList<>(), 4, chemistry.get_facultyID(), chemistry.getDepartmentID());
        dataManagement.createOrChangeCourse(course14);

        lecturersForSections.clear();
        lecturersForSections.add(lecturer11);
        lecturersForSections.add(lecturer11);
        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Thursday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Fourth);

        Course course15 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Introduction to Image Processing", "EE4062", new ArrayList<>(), 4, electricalEngineering.get_facultyID(), electricalEngineering.getDepartmentID());
        dataManagement.createOrChangeCourse(course15);


        Student student1 = dataManagement.generateRandomStudent(computerEngineering, 2021, 3, advisor.get_staffId());
        Student student2 = dataManagement.generateRandomStudent(computerEngineering, 2022, 15, advisor.get_staffId());
        Student student3 = dataManagement.generateRandomStudent(computerEngineering, 2023, 25, advisor.get_staffId());
        Student student4 = dataManagement.generateRandomStudent(computerEngineering, 2024, 60, advisor.get_staffId());
        Student student5 = dataManagement.generateRandomStudent(computerEngineering, 2021, 70, advisor.get_staffId());
        Student student6 = dataManagement.generateRandomStudent(computerEngineering, 2022, 32, advisor.get_staffId());
        Student student7 = dataManagement.generateRandomStudent(computerEngineering, 2023, 23, advisor.get_staffId());
        Student student8 = dataManagement.generateRandomStudent(computerEngineering, 2024, 45, advisor.get_staffId());

        dataManagement.createOrChangeStudent(student1);
        dataManagement.createOrChangeStudent(student2);
        dataManagement.createOrChangeStudent(student3);
        dataManagement.createOrChangeStudent(student4);

        TakenCourse takenCourse = new TakenCourse(course.getCourseInformation(), 90, 54);
        TakenCourse takenCourse1 = new TakenCourse(course1.getCourseInformation(), 70, 35);
        TakenCourse takenCourse2 = new TakenCourse(course2.getCourseInformation(), 20, 100);
        TakenCourse takenCourse3 = new TakenCourse(course3.getCourseInformation(), 85, 50);
        TakenCourse takenCourse4 = new TakenCourse(course4.getCourseInformation(), 75, 40);
        TakenCourse takenCourse5 = new TakenCourse(course5.getCourseInformation(), 95, 55);
        TakenCourse takenCourse6 = new TakenCourse(course6.getCourseInformation(), 90, 50);
        TakenCourse takenCourse7 = new TakenCourse(course7.getCourseInformation(), 85, 45);
        TakenCourse takenCourse8 = new TakenCourse(course8.getCourseInformation(), 30, 90);

        student1.getTranscript().addTakenCourse(takenCourse);
        student1.getTranscript().addTakenCourse(takenCourse1);
        student1.getTranscript().addTakenCourse(takenCourse2);
        student1.getTranscript().addTakenCourse(takenCourse3);
        student1.getTranscript().addTakenCourse(takenCourse4);
        student1.getTranscript().addTakenCourse(takenCourse5);
        student1.getTranscript().addTakenCourse(takenCourse6);
        student1.getTranscript().addTakenCourse(takenCourse7);
        student1.getTranscript().addTakenCourse(takenCourse8);
        dataManagement.createOrChangeStudent(student1);

        TakenCourse takenCourse9 = new TakenCourse(course.getCourseInformation(), 50, 50);
        TakenCourse takenCourse10 = new TakenCourse(course1.getCourseInformation(), 70, 70);
        TakenCourse takenCourse11 = new TakenCourse(course2.getCourseInformation(), 100, 65);
        TakenCourse takenCourse12 = new TakenCourse(course3.getCourseInformation(), 85, 50);
        TakenCourse takenCourse13 = new TakenCourse(course4.getCourseInformation(), 75, 40);
        TakenCourse takenCourse14 = new TakenCourse(course5.getCourseInformation(), 50, 80);
        TakenCourse takenCourse15 = new TakenCourse(course6.getCourseInformation(), 40, 80);
        TakenCourse takenCourse17 = new TakenCourse(course8.getCourseInformation(), 60, 85);

        student5.getTranscript().addTakenCourse(takenCourse9);
        student5.getTranscript().addTakenCourse(takenCourse10);
        student5.getTranscript().addTakenCourse(takenCourse11);
        student5.getTranscript().addTakenCourse(takenCourse12);
        student5.getTranscript().addTakenCourse(takenCourse13);
        student5.getTranscript().addTakenCourse(takenCourse14);
        student5.getTranscript().addTakenCourse(takenCourse15);
        student5.getTranscript().addTakenCourse(takenCourse17);
        dataManagement.createOrChangeStudent(student5);

        TakenCourse takenCourse18 = new TakenCourse(course.getCourseInformation(), 100, 95);
        TakenCourse takenCourse19 = new TakenCourse(course1.getCourseInformation(), 97, 93);
        TakenCourse takenCourse20 = new TakenCourse(course2.getCourseInformation(), 55, 65);
        TakenCourse takenCourse22 = new TakenCourse(course4.getCourseInformation(), 75, 40);
        TakenCourse takenCourse23 = new TakenCourse(course5.getCourseInformation(), 67, 50);

        student2.getTranscript().addTakenCourse(takenCourse18);
        student2.getTranscript().addTakenCourse(takenCourse19);
        student2.getTranscript().addTakenCourse(takenCourse20);
        student2.getTranscript().addTakenCourse(takenCourse22);
        student2.getTranscript().addTakenCourse(takenCourse23);
        dataManagement.createOrChangeStudent(student2);

        TakenCourse takenCourse24 = new TakenCourse(course.getCourseInformation(), 70, 95);
        TakenCourse takenCourse25 = new TakenCourse(course1.getCourseInformation(), 90, 60);
        TakenCourse takenCourse26 = new TakenCourse(course2.getCourseInformation(), 60, 70);
        TakenCourse takenCourse27 = new TakenCourse(course3.getCourseInformation(), 90, 40);
        TakenCourse takenCourse28 = new TakenCourse(course4.getCourseInformation(), 85, 50);
        TakenCourse takenCourse29 = new TakenCourse(course5.getCourseInformation(), 55, 75);

        student6.getTranscript().addTakenCourse(takenCourse24);
        student6.getTranscript().addTakenCourse(takenCourse25);
        student6.getTranscript().addTakenCourse(takenCourse26);
        student6.getTranscript().addTakenCourse(takenCourse27);
        student6.getTranscript().addTakenCourse(takenCourse28);
        student6.getTranscript().addTakenCourse(takenCourse29);
        dataManagement.createOrChangeStudent(student6);

        TakenCourse takenCourse30 = new TakenCourse(course.getCourseInformation(), 90, 65);
        TakenCourse takenCourse31 = new TakenCourse(course1.getCourseInformation(), 75, 50);
        TakenCourse takenCourse32 = new TakenCourse(course2.getCourseInformation(), 50, 85);

        student3.getTranscript().addTakenCourse(takenCourse30);
        student3.getTranscript().addTakenCourse(takenCourse31);
        student3.getTranscript().addTakenCourse(takenCourse32);
        dataManagement.createOrChangeStudent(student3);

        TakenCourse takenCourse33 = new TakenCourse(course.getCourseInformation(), 50, 85);
        TakenCourse takenCourse34 = new TakenCourse(course1.getCourseInformation(), 90, 55);
        TakenCourse takenCourse35 = new TakenCourse(course2.getCourseInformation(), 90, 70);

        student7.getTranscript().addTakenCourse(takenCourse33);
        student7.getTranscript().addTakenCourse(takenCourse34);
        student7.getTranscript().addTakenCourse(takenCourse35);
        dataManagement.createOrChangeStudent(student7);

        dataManagement.createOrChangeStudent(student4);
        dataManagement.createOrChangeStudent(student8);


        DepartmentScheduler departmentScheduler = dataManagement.generateRandomDepartmentScheduler(computerEngineering);
        dataManagement.createOrChangeDepartmentScheduler(departmentScheduler);

        StudentsAffairs studentsAffairs = dataManagement.generateRandomStudentsAffairs(computerEngineering);
        dataManagement.createOrChangeStudentsAffairs(studentsAffairs);

        //yusuf
        // **************************************************** Faculties ****************************************************
        //new Faculty "Business"
        Faculty Business = dataManagement.generateFaculty(3, "Business");
        dataManagement.createOrChangeFaculty(Business);
        //New Faculty "Science"
        Faculty Science = dataManagement.generateFaculty(2, "Science");
        dataManagement.createOrChangeFaculty(Science);

        // **************************************************** Departments ****************************************************

        //new Department "Business" in Faculty "Business"
        Department BusinessDepartment = dataManagement.generateDepartment(301, "Business", Business);
        dataManagement.createOrChangeDepartment(BusinessDepartment);
        //New Department "Biology" in Faculty "Science"
        Department BiologyDepartment = dataManagement.generateDepartment(201, "Biology", Science);
        dataManagement.createOrChangeDepartment(BiologyDepartment);
        //New Department "Chemistry" in Faculty "Science"
        Department chemistryDepartment = dataManagement.generateDepartment(202, "Chemistry", Science);
        dataManagement.createOrChangeDepartment(chemistryDepartment);

        // **************************************************** Advisors and Lecturers ****************************************************

        //new Advisors and Lecturers for Business Department
        Advisor advisor301 = dataManagement.generateRandomAdvisor(BusinessDepartment);
        Lecturer lecturer301 = dataManagement.generateRandomLecturer(BusinessDepartment);
        Lecturer lecturer302 = dataManagement.generateRandomLecturer(BusinessDepartment);
        Lecturer lecturer303 = dataManagement.generateRandomLecturer(BusinessDepartment);

        dataManagement.createOrChangeAdvisor(advisor301);
        dataManagement.createOrChangeLecturer(lecturer301);
        dataManagement.createOrChangeLecturer(lecturer302);
        dataManagement.createOrChangeLecturer(lecturer303);

        //New Advisors and Lecturers for Biology Department
        Advisor advisor201 = dataManagement.generateRandomAdvisor(BiologyDepartment);
        Lecturer lecturer201 = dataManagement.generateRandomLecturer(BiologyDepartment);
        Lecturer lecturer202 = dataManagement.generateRandomLecturer(BiologyDepartment);
        Lecturer lecturer203 = dataManagement.generateRandomLecturer(BiologyDepartment);
        Lecturer lecturer204 = dataManagement.generateRandomLecturer(BiologyDepartment);

        dataManagement.createOrChangeAdvisor(advisor201);
        dataManagement.createOrChangeLecturer(lecturer201);
        dataManagement.createOrChangeLecturer(lecturer202);
        dataManagement.createOrChangeLecturer(lecturer203);
        dataManagement.createOrChangeLecturer(lecturer204);

        //New Advisors and Lecturers for Chemistry Department
        Advisor advisor211 = dataManagement.generateRandomAdvisor(chemistryDepartment);
        Lecturer lecturer211 = dataManagement.generateRandomLecturer(chemistryDepartment);
        Lecturer lecturer212 = dataManagement.generateRandomLecturer(chemistryDepartment);
        Lecturer lecturer213 = dataManagement.generateRandomLecturer(chemistryDepartment);
        Lecturer lecturer214 = dataManagement.generateRandomLecturer(chemistryDepartment);

        dataManagement.createOrChangeAdvisor(advisor211);
        dataManagement.createOrChangeLecturer(lecturer211);
        dataManagement.createOrChangeLecturer(lecturer212);
        dataManagement.createOrChangeLecturer(lecturer213);
        dataManagement.createOrChangeLecturer(lecturer214);

        // **************************************************** Courses ****************************************************

        lecturersForSections.clear();        //Course1 for Business Department
        lecturersForSections.add(lecturer301);
        lecturersForSections.add(lecturer301);
        lecturersForSections.add(lecturer301);

        days.clear();
        days.add(Day.Monday);
        days.add(Day.Monday);
        days.add(Day.Thursday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Second);
        Course course301 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Principles of Microeconomics", "EC101", new ArrayList<>(), 1, BusinessDepartment.get_facultyID(), BusinessDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course301);

        //Course2 for Business Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer302);
        lecturersForSections.add(lecturer302);
        lecturersForSections.add(lecturer302);
        lecturersForSections.add(lecturer302);

        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Tuesday);
        days.add(Day.Wednesday);
        days.add(Day.Wednesday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Second);

        prerequisites.clear();
        prerequisites.add(course301.getCourseInformation());

        Course course302 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Microeconomics", "EC203", prerequisites, 2, BusinessDepartment.get_facultyID(), BusinessDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course302);

        //Course3 for Business Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer301);
        lecturersForSections.add(lecturer301);
        lecturersForSections.add(lecturer301);
        lecturersForSections.add(lecturer301);

        days.clear();
        days.add(Day.Monday);
        days.add(Day.Tuesday);
        days.add(Day.Tuesday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Fifth);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Fourth);
        sectionTimes.add(SectionTime.Fifth);

        prerequisites.clear();

        Course course303 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Financial Management", "FM311", prerequisites, 3, BusinessDepartment.get_facultyID(), BusinessDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course303);

        //Course4 for Business Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer303);
        lecturersForSections.add(lecturer303);
        lecturersForSections.add(lecturer303);
        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Wednesday);
        days.add(Day.Wednesday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Fourth);
        prerequisites.clear();

        Course course304 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Strategic Management", "AD401", prerequisites, 4, BusinessDepartment.get_facultyID(), BusinessDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course304);

        /* **************************************************************************************************** */


        //Course1 for Biology Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer201);
        lecturersForSections.add(lecturer201);
        lecturersForSections.add(lecturer201);

        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Tuesday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.First);
        prerequisites.clear();

        Course course201 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "General Biology", "BYL1011", prerequisites, 1, BiologyDepartment.get_facultyID(), BiologyDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course201);

        //Course2 for Biology Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer202);
        lecturersForSections.add(lecturer202);
        lecturersForSections.add(lecturer202);
        lecturersForSections.add(lecturer202);

        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Thursday);
        days.add(Day.Thursday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.First);
        prerequisites.clear();

        Course course202 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "History of Biology", "BYL2031", prerequisites, 2, BiologyDepartment.get_facultyID(), BiologyDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course202);

        //Course3 for Biology Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer203);
        lecturersForSections.add(lecturer203);
        lecturersForSections.add(lecturer203);

        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Tuesday);
        days.add(Day.Thursday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Fourth);
        prerequisites.clear();
        prerequisites.add(course201.getCourseInformation());


        Course course203 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Micro Biology", "BYL3042", prerequisites, 3, BiologyDepartment.get_facultyID(), BiologyDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course203);

        //Course4 for Biology Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer204);
        lecturersForSections.add(lecturer204);
        lecturersForSections.add(lecturer204);

        days.clear();
        days.add(Day.Monday);
        days.add(Day.Monday);
        days.add(Day.Monday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Fourth);
        prerequisites.clear();
        prerequisites.add(course201.getCourseInformation());

        Course course204 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Human Anatomy", "BYL4011", prerequisites, 4, BiologyDepartment.get_facultyID(), BiologyDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course204);

        /* **************************************************************************************************** */

        //Course1 for Chemistry Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer211);
        lecturersForSections.add(lecturer211);
        lecturersForSections.add(lecturer211);
        lecturersForSections.add(lecturer211);

        days.clear();
        days.add(Day.Monday);
        days.add(Day.Monday);
        days.add(Day.Friday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Fourth);
        prerequisites.clear();

        Course course211 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "General Chemistry", "CHM1135", prerequisites, 1, chemistryDepartment.get_facultyID(), chemistryDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course211);

        //Course2 for Chemistry Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer211);
        lecturersForSections.add(lecturer211);
        lecturersForSections.add(lecturer211);
        lecturersForSections.add(lecturer211);

        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Tuesday);
        days.add(Day.Wednesday);
        days.add(Day.Thursday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Second);
        prerequisites.clear();
        prerequisites.add(course211.getCourseInformation());

        Course course212 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Analytical Chemistry", "CHM2023", prerequisites, 2, chemistryDepartment.get_facultyID(), chemistryDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course212);

        //Course3 for Chemistry Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer213);
        lecturersForSections.add(lecturer213);
        lecturersForSections.add(lecturer213);

        days.clear();
        days.add(Day.Monday);
        days.add(Day.Monday);
        days.add(Day.Thursday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Fourth);
        prerequisites.clear();

        Course course213 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Industrial Analysis", "CHM3048", prerequisites, 3, chemistryDepartment.get_facultyID(), chemistryDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course213);

        //Course4 for Chemistry Department
        lecturersForSections.clear();
        lecturersForSections.add(lecturer214);
        lecturersForSections.add(lecturer214);
        lecturersForSections.add(lecturer214);
        lecturersForSections.add(lecturer214);

        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Wednesday);
        days.add(Day.Wednesday);
        days.add(Day.Friday);
        sectionTimes.clear();
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.First);
        prerequisites.clear();
        prerequisites.add(course212.getCourseInformation());

        Course course214 = dataManagement.generateCourse(lecturersForSections, days, sectionTimes, "Biochemistry", "CHM4011", prerequisites, 4, chemistryDepartment.get_facultyID(), chemistryDepartment.getDepartmentID());
        dataManagement.createOrChangeCourse(course214);

        // **************************************************** Students ****************************************************
        // for example: student306 is for 6th student in Business Department, student204 is for 4th student in Biology Department, student213 is for 3rd student in Chemistry Department
        Student student301 = dataManagement.generateRandomStudent(BusinessDepartment, 2021, 2, advisor301.get_staffId());
        Student student302 = dataManagement.generateRandomStudent(BusinessDepartment, 2024, 15, advisor301.get_staffId());
        Student student303 = dataManagement.generateRandomStudent(BusinessDepartment, 2023, 66, advisor301.get_staffId());
        Student student304 = dataManagement.generateRandomStudent(BusinessDepartment, 2022, 58, advisor301.get_staffId());
        Student student305 = dataManagement.generateRandomStudent(BusinessDepartment, 2021, 24, advisor301.get_staffId());
        Student student306 = dataManagement.generateRandomStudent(BusinessDepartment, 2023, 13, advisor301.get_staffId());

        Student student201 = dataManagement.generateRandomStudent(BiologyDepartment, 2022, 75, advisor201.get_staffId());
        Student student202 = dataManagement.generateRandomStudent(BiologyDepartment, 2022, 53, advisor201.get_staffId());
        Student student203 = dataManagement.generateRandomStudent(BiologyDepartment, 2024, 34, advisor201.get_staffId());
        Student student204 = dataManagement.generateRandomStudent(BiologyDepartment, 2021, 3, advisor201.get_staffId());
        Student student205 = dataManagement.generateRandomStudent(BiologyDepartment, 2023, 27, advisor201.get_staffId());
        Student student206 = dataManagement.generateRandomStudent(BiologyDepartment, 2024, 11, advisor201.get_staffId());

        Student student211 = dataManagement.generateRandomStudent(chemistryDepartment, 2021, 37, advisor211.get_staffId());
        Student student212 = dataManagement.generateRandomStudent(chemistryDepartment, 2022, 29, advisor211.get_staffId());
        Student student213 = dataManagement.generateRandomStudent(chemistryDepartment, 2024, 1, advisor211.get_staffId());
        Student student214 = dataManagement.generateRandomStudent(chemistryDepartment, 2024, 25, advisor211.get_staffId());
        Student student215 = dataManagement.generateRandomStudent(chemistryDepartment, 2024, 45, advisor211.get_staffId());
        Student student216 = dataManagement.generateRandomStudent(chemistryDepartment, 2023, 8, advisor211.get_staffId());

        //Add students taken courses to the system

        student301.getTranscript().addTakenCourse(new TakenCourse(course301.getCourseInformation(), 90, 54));
        student301.getTranscript().addTakenCourse(new TakenCourse(course302.getCourseInformation(), 80, 65));
        student301.getTranscript().addTakenCourse(new TakenCourse(course303.getCourseInformation(), 70, 75));

        student303.getTranscript().addTakenCourse(new TakenCourse(course301.getCourseInformation(), 90, 64));

        student304.getTranscript().addTakenCourse(new TakenCourse(course301.getCourseInformation(), 93, 74));
        student304.getTranscript().addTakenCourse(new TakenCourse(course302.getCourseInformation(), 85, 65));

        student305.getTranscript().addTakenCourse(new TakenCourse(course301.getCourseInformation(), 75, 70));
        student305.getTranscript().addTakenCourse(new TakenCourse(course302.getCourseInformation(), 65, 85));
        student305.getTranscript().addTakenCourse(new TakenCourse(course303.getCourseInformation(), 75, 75));

        student306.getTranscript().addTakenCourse(new TakenCourse(course301.getCourseInformation(), 85, 75));

        student201.getTranscript().addTakenCourse(new TakenCourse(course201.getCourseInformation(), 90, 85));
        student201.getTranscript().addTakenCourse(new TakenCourse(course202.getCourseInformation(), 68, 75));

        student202.getTranscript().addTakenCourse(new TakenCourse(course201.getCourseInformation(), 88, 72));
        student202.getTranscript().addTakenCourse(new TakenCourse(course202.getCourseInformation(), 65, 85));

        student204.getTranscript().addTakenCourse(new TakenCourse(course201.getCourseInformation(), 75, 85));
        student204.getTranscript().addTakenCourse(new TakenCourse(course202.getCourseInformation(), 55, 100));
        student204.getTranscript().addTakenCourse(new TakenCourse(course203.getCourseInformation(), 75, 85));

        student205.getTranscript().addTakenCourse(new TakenCourse(course201.getCourseInformation(), 38, 90));

        student211.getTranscript().addTakenCourse(new TakenCourse(course211.getCourseInformation(), 45, 85));
        student211.getTranscript().addTakenCourse(new TakenCourse(course212.getCourseInformation(), 85, 75));
        student211.getTranscript().addTakenCourse(new TakenCourse(course213.getCourseInformation(), 75, 85));

        student212.getTranscript().addTakenCourse(new TakenCourse(course211.getCourseInformation(), 55, 80));
        student212.getTranscript().addTakenCourse(new TakenCourse(course212.getCourseInformation(), 70, 85));

        student216.getTranscript().addTakenCourse(new TakenCourse(course211.getCourseInformation(), 90, 80));

        // Add students to the system

        dataManagement.createOrChangeStudent(student301);
        dataManagement.createOrChangeStudent(student302);
        dataManagement.createOrChangeStudent(student303);
        dataManagement.createOrChangeStudent(student304);
        dataManagement.createOrChangeStudent(student305);
        dataManagement.createOrChangeStudent(student306);

        dataManagement.createOrChangeStudent(student201);
        dataManagement.createOrChangeStudent(student202);
        dataManagement.createOrChangeStudent(student203);
        dataManagement.createOrChangeStudent(student204);
        dataManagement.createOrChangeStudent(student205);
        dataManagement.createOrChangeStudent(student206);

        dataManagement.createOrChangeStudent(student211);
        dataManagement.createOrChangeStudent(student212);
        dataManagement.createOrChangeStudent(student213);
        dataManagement.createOrChangeStudent(student214);
        dataManagement.createOrChangeStudent(student215);
        dataManagement.createOrChangeStudent(student216);

        // **************************************************** DepartmentSchedulers and StudentsAffairs ****************************************************

        DepartmentScheduler departmentScheduler301 = dataManagement.generateRandomDepartmentScheduler(BusinessDepartment);
        dataManagement.createOrChangeDepartmentScheduler(departmentScheduler301);
        DepartmentScheduler departmentScheduler201 = dataManagement.generateRandomDepartmentScheduler(BiologyDepartment);
        dataManagement.createOrChangeDepartmentScheduler(departmentScheduler201);
        DepartmentScheduler departmentScheduler202 = dataManagement.generateRandomDepartmentScheduler(chemistryDepartment);
        dataManagement.createOrChangeDepartmentScheduler(departmentScheduler202);

        StudentsAffairs studentsAffairs301 = dataManagement.generateRandomStudentsAffairs(BusinessDepartment);
        dataManagement.createOrChangeStudentsAffairs(studentsAffairs301);
        StudentsAffairs studentsAffairs201 = dataManagement.generateRandomStudentsAffairs(BiologyDepartment);
        dataManagement.createOrChangeStudentsAffairs(studentsAffairs201);
        StudentsAffairs studentsAffairs202 = dataManagement.generateRandomStudentsAffairs(chemistryDepartment);
        dataManagement.createOrChangeStudentsAffairs(studentsAffairs202);

        // berkan

//1;

        Faculty Engineering = dataManagement.generateFaculty(1, "Engineering");
        dataManagement.createOrChangeFaculty(Engineering);

        Department MechanicalEngineering = dataManagement.generateDepartment(101, "Mechanical Engineering", Engineering);
        dataManagement.createOrChangeDepartment(MechanicalEngineering);

        Advisor bAdvisor = dataManagement.generateRandomAdvisor(MechanicalEngineering);
        dataManagement.createOrChangeAdvisor(bAdvisor);

        Lecturer bLecturer1 = dataManagement.generateRandomLecturer(MechanicalEngineering);
        Lecturer bLecturer2 = dataManagement.generateRandomLecturer(MechanicalEngineering);
        Lecturer bLecturer3 = dataManagement.generateRandomLecturer(MechanicalEngineering);
        Lecturer bLecturer4 = dataManagement.generateRandomLecturer(MechanicalEngineering);
        Lecturer bLecturer5 = dataManagement.generateRandomLecturer(MechanicalEngineering);


        dataManagement.createOrChangeLecturer(bLecturer1);
        dataManagement.createOrChangeLecturer(bLecturer2);
        dataManagement.createOrChangeLecturer(bLecturer3);
        dataManagement.createOrChangeLecturer(bLecturer4);
        dataManagement.createOrChangeLecturer(bLecturer5);

        lecturersForSections.clear();
        lecturersForSections.add(bLecturer1);
        lecturersForSections.add(bLecturer1);

        days.clear();
        days.add(Day.Friday);
        days.add(Day.Thursday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Fourth);
        sectionTimes.add(SectionTime.First);

        prerequisites.clear();
        Course Thermodynamics = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Thermodynamics",
                "MATH101",
                prerequisites,
                1,
                MechanicalEngineering.get_facultyID(),
                MechanicalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(Thermodynamics);


        //2;
        lecturersForSections.clear();
        lecturersForSections.add(bLecturer1);
        lecturersForSections.add(bLecturer1);

        days.clear();
        days.add(Day.Thursday);
        days.add(Day.Wednesday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Third);

        ArrayList<CourseInformation> bPrerequisites2 = new ArrayList<>();

        Course MaterialScience = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Material Sci.",
                "MSE272",
                bPrerequisites2,
                2, // Course credits
                MechanicalEngineering.get_facultyID(),
                MechanicalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(MaterialScience);


        //3;
        lecturersForSections.clear();
        lecturersForSections.add(bLecturer3);
        lecturersForSections.add(bLecturer3);
        lecturersForSections.add(bLecturer3);

        days.clear();
        days.add(Day.Thursday);
        days.add(Day.Monday);
        days.add(Day.Friday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Fourth);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Second);

        prerequisites.clear();
        prerequisites.add(MaterialScience.getCourseInformation());

        Course StrengthOfMaterials = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Strength of Mat.",
                "ME271",
                prerequisites,
                3,
                MechanicalEngineering.get_facultyID(),
                MechanicalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(StrengthOfMaterials);
        //4;
        lecturersForSections.clear();
        lecturersForSections.add(bLecturer4);
        lecturersForSections.add(bLecturer5);
        days.clear();
        days.add(Day.Tuesday);
        days.add(Day.Wednesday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Third);

        prerequisites.clear();

        Course FluidMechanics = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Fluid Mechanics",
                "ME361",
                prerequisites,
                3,
                MechanicalEngineering.get_facultyID(),
                MechanicalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(FluidMechanics);

        //5;
        lecturersForSections.clear();
        lecturersForSections.add(bLecturer5);
        lecturersForSections.add(bLecturer5);
        lecturersForSections.add(bLecturer1);

        days.clear();
        days.add(Day.Thursday);
        days.add(Day.Monday);
        days.add(Day.Tuesday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Fourth);

        prerequisites.clear();

        Course HeatTransfer = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Heat Transfer",
                "ME471",
                prerequisites,
                4,
                MechanicalEngineering.get_facultyID(),
                MechanicalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(HeatTransfer);


        Student bStudent2021_2 = dataManagement.generateRandomStudent(MechanicalEngineering, 2021, 4, bAdvisor.get_staffId());
        bStudent2021_2.getTranscript().addTakenCourse(new TakenCourse(Thermodynamics.getCourseInformation(), 90, 85)); //1
        bStudent2021_2.getTranscript().addTakenCourse(new TakenCourse(MaterialScience.getCourseInformation(), 88, 72)); //2
        bStudent2021_2.getTranscript().addTakenCourse(new TakenCourse(StrengthOfMaterials.getCourseInformation(), 75, 85)); //3
        bStudent2021_2.getTranscript().addTakenCourse(new TakenCourse(FluidMechanics.getCourseInformation(), 55, 100)); //3
        dataManagement.createOrChangeStudent(bStudent2021_2);


        Student bStudent2022_1 = dataManagement.generateRandomStudent(MechanicalEngineering, 2022, 3, bAdvisor.get_staffId());
        bStudent2022_1.getTranscript().addTakenCourse(new TakenCourse(Thermodynamics.getCourseInformation(), 67, 80)); //1
        bStudent2022_1.getTranscript().addTakenCourse(new TakenCourse(MaterialScience.getCourseInformation(), 74, 69)); //2
        dataManagement.createOrChangeStudent(bStudent2022_1);

        Student bStudent2023_2 = dataManagement.generateRandomStudent(MechanicalEngineering, 2023, 2, bAdvisor.get_staffId());
        dataManagement.createOrChangeStudent(bStudent2023_2);
        bStudent2022_1.getTranscript().addTakenCourse(new TakenCourse(Thermodynamics.getCourseInformation(), 31, 90)); //1


        Student bStudent2024_2 = dataManagement.generateRandomStudent(MechanicalEngineering, 2024, 1, bAdvisor.get_staffId());
        dataManagement.createOrChangeStudent(bStudent2024_2);


        //Industrial Engineering

        Department IndustrialEngineering = dataManagement.generateDepartment(101, "Industrial Engineering", Engineering);
        dataManagement.createOrChangeDepartment(IndustrialEngineering);

        Lecturer ieLecturer1 = dataManagement.generateRandomLecturer(IndustrialEngineering);
        dataManagement.createOrChangeLecturer(ieLecturer1);

        Lecturer ieLecturer2 = dataManagement.generateRandomLecturer(IndustrialEngineering);
        dataManagement.createOrChangeLecturer(ieLecturer2);

        Lecturer ieLecturer3 = dataManagement.generateRandomLecturer(IndustrialEngineering);
        dataManagement.createOrChangeLecturer(ieLecturer3);

        Lecturer ieLecturer4 = dataManagement.generateRandomLecturer(IndustrialEngineering);
        dataManagement.createOrChangeLecturer(ieLecturer4);

        Advisor bbAdvisor = dataManagement.generateRandomAdvisor(IndustrialEngineering);
        dataManagement.createOrChangeAdvisor(bAdvisor);

        lecturersForSections.clear();
        lecturersForSections.add(ieLecturer1);
        lecturersForSections.add(ieLecturer1);
        lecturersForSections.add(ieLecturer1);

        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Monday);
        days.add(Day.Friday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Fourth);
        sectionTimes.add(SectionTime.Fourth);

        prerequisites.clear();

        Course OperationsResearch = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Operations Research",
                "IE3003",
                prerequisites,
                3,
                IndustrialEngineering.get_facultyID(),
                IndustrialEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(OperationsResearch);


        //7;
        lecturersForSections.clear();
        lecturersForSections.add(ieLecturer2);
        lecturersForSections.add(ieLecturer2);
        lecturersForSections.add(ieLecturer4);

        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Friday);
        days.add(Day.Monday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.First);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Third);

        prerequisites.clear();

        Course Probability = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Probability",
                "IE2151",
                prerequisites,
                2,
                IndustrialEngineering.get_facultyID(),
                IndustrialEngineering.getDepartmentID()

        );
        dataManagement.createOrChangeCourse(Probability);

        //8;
        lecturersForSections.clear();
        lecturersForSections.add(ieLecturer3);
        lecturersForSections.add(ieLecturer3);
        lecturersForSections.add(ieLecturer3);

        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Monday);
        days.add(Day.Tuesday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Fourth);
        sectionTimes.add(SectionTime.Fourth);
        sectionTimes.add(SectionTime.Third);

        prerequisites.clear();
        prerequisites.add(Probability.getCourseInformation());

        Course Simulation = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Simulation",
                "IE3064",
                prerequisites,
                3,
                IndustrialEngineering.get_facultyID(),
                IndustrialEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(Simulation);

        //9;
        lecturersForSections.clear();
        lecturersForSections.add(ieLecturer4);
        lecturersForSections.add(ieLecturer4);

        days.clear();
        days.add(Day.Friday);
        days.add(Day.Wednesday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Third);

        prerequisites.clear();

        Course TurkishLanguage = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Turkish Language",
                "TRD121",
                prerequisites,
                1,
                IndustrialEngineering.get_facultyID(),
                IndustrialEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(TurkishLanguage);

        Student ieStudent2021_1 = dataManagement.generateRandomStudent(IndustrialEngineering, 2021, 101, bbAdvisor.get_staffId());
        ieStudent2021_1.getTranscript().addTakenCourse(new TakenCourse(OperationsResearch.getCourseInformation(), 90, 85)); //1
        ieStudent2021_1.getTranscript().addTakenCourse(new TakenCourse(Probability.getCourseInformation(), 88, 72)); //2
        ieStudent2021_1.getTranscript().addTakenCourse(new TakenCourse(Simulation.getCourseInformation(), 75, 85)); //3
        ieStudent2021_1.getTranscript().addTakenCourse(new TakenCourse(TurkishLanguage.getCourseInformation(), 55, 100)); //3
        dataManagement.createOrChangeStudent(ieStudent2021_1);

        Student ieStudent2022_2 = dataManagement.generateRandomStudent(IndustrialEngineering, 2022, 47, bbAdvisor.get_staffId());
        ieStudent2022_2.getTranscript().addTakenCourse(new TakenCourse(OperationsResearch.getCourseInformation(), 67, 80)); //1
        ieStudent2022_2.getTranscript().addTakenCourse(new TakenCourse(Probability.getCourseInformation(), 74, 69)); //2
        dataManagement.createOrChangeStudent(ieStudent2022_2);

        Student ieStudent2023_1 = dataManagement.generateRandomStudent(IndustrialEngineering, 2023, 33, bbAdvisor.get_staffId());
        ieStudent2023_1.getTranscript().addTakenCourse(new TakenCourse(OperationsResearch.getCourseInformation(), 31, 90)); //1
        dataManagement.createOrChangeStudent(ieStudent2023_1);

        Student ieStudent2024_1 = dataManagement.generateRandomStudent(IndustrialEngineering, 2024, 26, bbAdvisor.get_staffId());
        dataManagement.createOrChangeStudent(ieStudent2024_1);

        //10;
        Department ElectricalEngineering = dataManagement.generateDepartment(101, "Electrical Engineering", Engineering);
        dataManagement.createOrChangeDepartment(ElectricalEngineering);

        Lecturer eeLecturer1 = dataManagement.generateRandomLecturer(ElectricalEngineering);
        dataManagement.createOrChangeLecturer(eeLecturer1);

        Lecturer eeLecturer2 = dataManagement.generateRandomLecturer(ElectricalEngineering);
        dataManagement.createOrChangeLecturer(eeLecturer2);

        Advisor bbbAdvisor = dataManagement.generateRandomAdvisor(ElectricalEngineering);
        dataManagement.createOrChangeAdvisor(bAdvisor);


        lecturersForSections.clear();
        lecturersForSections.add(eeLecturer1);
        lecturersForSections.add(eeLecturer1);
        lecturersForSections.add(eeLecturer1);

        days.clear();
        days.add(Day.Friday);
        days.add(Day.Tuesday);
        days.add(Day.Thursday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Second);
        sectionTimes.add(SectionTime.Fourth);

        prerequisites.clear();

        Course PhysicsI = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Physics I",
                "PHYS1101",
                prerequisites,
                1,
                ElectricalEngineering.get_facultyID(),
                ElectricalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(PhysicsI);


        //11;
        lecturersForSections.clear();
        lecturersForSections.add(eeLecturer2);
        lecturersForSections.add(eeLecturer2);

        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Thursday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Fourth);
        sectionTimes.add(SectionTime.Second);

        prerequisites.clear();

        Course DigitalDesign = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Digital Design",
                "EE2003",
                prerequisites,
                2,
                ElectricalEngineering.get_facultyID(),
                ElectricalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(DigitalDesign);

        //12;
        lecturersForSections.clear();
        lecturersForSections.add(eeLecturer1);
        lecturersForSections.add(eeLecturer1);

        days.clear();
        days.add(Day.Thursday);
        days.add(Day.Monday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Third);

        prerequisites.clear();

        Course CommunicationSystems = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Communication Systems",
                "EE3082",
                prerequisites,
                3,
                ElectricalEngineering.get_facultyID(),
                ElectricalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(CommunicationSystems);
        //13;
        lecturersForSections.clear();
        lecturersForSections.add(eeLecturer2);
        lecturersForSections.add(eeLecturer1);


        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Friday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Third);
        sectionTimes.add(SectionTime.Third);

        prerequisites.clear();
        prerequisites.add(DigitalDesign.getCourseInformation());

        Course ElectromagneticWaves = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Electromagnetic Waves",
                "EE4051",
                prerequisites,
                4,
                ElectricalEngineering.get_facultyID(),
                ElectricalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(ElectromagneticWaves);


        //14
        lecturersForSections.clear();
        lecturersForSections.add(eeLecturer1);
        lecturersForSections.add(eeLecturer1);

        days.clear();
        days.add(Day.Wednesday);
        days.add(Day.Tuesday);

        sectionTimes.clear();
        sectionTimes.add(SectionTime.Seventh);
        sectionTimes.add(SectionTime.Ninth);

        prerequisites.clear();

        Course SignalsAndSystems = dataManagement.generateCourse(
                lecturersForSections,
                days,
                sectionTimes,
                "Signals and Systems",
                "EE3061",
                prerequisites,
                3,
                ElectricalEngineering.get_facultyID(),
                ElectricalEngineering.getDepartmentID()
        );
        dataManagement.createOrChangeCourse(SignalsAndSystems);

        Student eeStudent2021 = dataManagement.generateRandomStudent(ElectricalEngineering, 2021, 4, bbbAdvisor.get_staffId());
        eeStudent2021.getTranscript().addTakenCourse(new TakenCourse(PhysicsI.getCourseInformation(), 90, 85)); //1
        eeStudent2021.getTranscript().addTakenCourse(new TakenCourse(DigitalDesign.getCourseInformation(), 88, 72)); //2
        eeStudent2021.getTranscript().addTakenCourse(new TakenCourse(CommunicationSystems.getCourseInformation(), 75, 85)); //3
        eeStudent2021.getTranscript().addTakenCourse(new TakenCourse(SignalsAndSystems.getCourseInformation(), 55, 100)); //3
        dataManagement.createOrChangeStudent(eeStudent2021);

        Student eeStudent2022_2 = dataManagement.generateRandomStudent(ElectricalEngineering, 2022, 3, bbbAdvisor.get_staffId());
        eeStudent2022_2.getTranscript().addTakenCourse(new TakenCourse(PhysicsI.getCourseInformation(), 67, 80)); //1
        eeStudent2022_2.getTranscript().addTakenCourse(new TakenCourse(DigitalDesign.getCourseInformation(), 74, 69)); //2
        dataManagement.createOrChangeStudent(eeStudent2022_2);

        Student eeStudent2023_1 = dataManagement.generateRandomStudent(ElectricalEngineering, 2023, 2, bbbAdvisor.get_staffId());
        eeStudent2023_1.getTranscript().addTakenCourse(new TakenCourse(PhysicsI.getCourseInformation(), 31, 90)); //1
        dataManagement.createOrChangeStudent(eeStudent2023_1);

        Student eeStudent2024_2 = dataManagement.generateRandomStudent(ElectricalEngineering, 2024, 1, bbbAdvisor.get_staffId());
        dataManagement.createOrChangeStudent(eeStudent2024_2);


    }


    public ArrayList<Student> getAllStudents() {
        // Read all students from the files
        ArrayList<Student> students = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(STUDENTS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(STUDENTS_FILE_PATH + filePath)) {
                    students.add(gson.fromJson(reader, Student.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return students;
    }

    public void createOrChangeStudent(Student student) {
        // Save student to the file
        String filePath = STUDENTS_FILE_PATH + student.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {

            gson.toJson(student, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Student getStudent(String university_email) {
        // Read student from the file
        String filePath = STUDENTS_FILE_PATH + university_email + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Student.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeStudent(Student student) {
        if (student == null) {
            return false;
        }
        String filePath = STUDENTS_FILE_PATH + student.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try {
            java.io.File file = new java.io.File(filePath);
            if (file.exists()) {
                file.delete();
                return true;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }


        return false;
    }

    public ArrayList<Lecturer> getAllLecturers() {
        // Read all lecturers from the files
        ArrayList<Lecturer> lecturers = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(LECTURERS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(LECTURERS_FILE_PATH + filePath)) {
                    lecturers.add(gson.fromJson(reader, Lecturer.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lecturers;
    }

    public void createOrChangeLecturer(Lecturer lecturer) {
        String filePath = LECTURERS_FILE_PATH + lecturer.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(lecturer, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Lecturer getLecturer(String university_email) {
        String filePath = LECTURERS_FILE_PATH + university_email + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Lecturer.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeLecturer(Lecturer lecturer) {
        String filePath = LECTURERS_FILE_PATH + lecturer.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    public ArrayList<Course> getAllCourses() {
        // Read all courses from the files
        ArrayList<Course> courses = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(COURSES_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(COURSES_FILE_PATH + filePath)) {
                    courses.add(gson.fromJson(reader, Course.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return courses;
    }

    public void createOrChangeCourse(Course course) {
        // Save course to the file
        String filePath = COURSES_FILE_PATH + course.getCourseInformation().getCourseName() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(course, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Course getCourse(String courseName) {
        // Read course from the file
        String filePath = COURSES_FILE_PATH + courseName + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Course.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeCourse(Course course) {
        String filePath = COURSES_FILE_PATH + course.getCourseInformation().getCourseName() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }
        return false;
    }

    public ArrayList<Advisor> getAllAdvisors() {
        // Read all advisors from the files
        ArrayList<Advisor> advisors = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(ADVISORS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(ADVISORS_FILE_PATH + filePath)) {
                    advisors.add(gson.fromJson(reader, Advisor.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return advisors;
    }

    public void createOrChangeAdvisor(Advisor advisor) {
        // Save advisor to the file
        String filePath = ADVISORS_FILE_PATH + advisor.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(advisor, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Advisor getAdvisor(String university_email) {
        // Read advisor from the file
        String filePath = ADVISORS_FILE_PATH + university_email + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Advisor.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeAdvisor(Advisor advisor) {
        String filePath = ADVISORS_FILE_PATH + advisor.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    public ArrayList<Faculty> getAllFaculties() {
        // Read all faculties from the files
        ArrayList<Faculty> faculties = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(FACULTIES_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(FACULTIES_FILE_PATH + filePath)) {
                    faculties.add(gson.fromJson(reader, Faculty.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return faculties;
    }

    public void createOrChangeFaculty(Faculty faculty) {
        // Save faculty to the file
        String filePath = FACULTIES_FILE_PATH + faculty.getFacultyID().getFacultyName() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(faculty, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Faculty getFaculty(String facultyName) {
        // Read faculty from the file
        String filePath = FACULTIES_FILE_PATH + facultyName + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Faculty.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeFaculty(Faculty faculty) {
        String filePath = FACULTIES_FILE_PATH + faculty.getFacultyID().getFacultyName() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    public ArrayList<Department> getAllDepartments() {
        // Read all departments from the files
        ArrayList<Department> departments = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(DEPARTMENTS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(DEPARTMENTS_FILE_PATH + filePath)) {
                    departments.add(gson.fromJson(reader, Department.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return departments;
    }

    public void createOrChangeDepartment(Department department) {
        // Save department to the file
        String filePath = DEPARTMENTS_FILE_PATH + department.getDepartmentID().getDepartmentName() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(department, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Department getDepartment(String departmentName) {
        // Read department from the file
        String filePath = DEPARTMENTS_FILE_PATH + departmentName + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, Department.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeDepartment(Department department) {
        String filePath = DEPARTMENTS_FILE_PATH + department.getDepartmentID().getDepartmentName() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    public ArrayList<DepartmentScheduler> getAllDepartmentSchedulers() {
        // Read all department schedulers from the files
        ArrayList<DepartmentScheduler> departmentSchedulers = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(DEPARTMENT_SCHEDULERS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(DEPARTMENT_SCHEDULERS_FILE_PATH + filePath)) {
                    departmentSchedulers.add(gson.fromJson(reader, DepartmentScheduler.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return departmentSchedulers;
    }

    public void createOrChangeDepartmentScheduler(DepartmentScheduler departmentScheduler) {
        // Save department scheduler to the file
        String filePath = DEPARTMENT_SCHEDULERS_FILE_PATH + departmentScheduler.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(departmentScheduler, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public DepartmentScheduler getDepartmentScheduler(String university_email) {
        // Read department scheduler from the file
        String filePath = DEPARTMENT_SCHEDULERS_FILE_PATH + university_email + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, DepartmentScheduler.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeDepartmentScheduler(DepartmentScheduler departmentScheduler) {
        String filePath = DEPARTMENT_SCHEDULERS_FILE_PATH + departmentScheduler.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    public ArrayList<StudentsAffairs> getAllStudentsAffairs() {
        // Read all students affairs from the files
        ArrayList<StudentsAffairs> studentsAffairs = new ArrayList<>();
        try {
            for (String filePath : new java.io.File(STUDENTS_AFFAIRS_FILE_PATH).list()) {
                try (FileReader reader = new FileReader(STUDENTS_AFFAIRS_FILE_PATH + filePath)) {
                    studentsAffairs.add(gson.fromJson(reader, StudentsAffairs.class));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return studentsAffairs;
    }

    public void createOrChangeStudentsAffairs(StudentsAffairs studentsAffairs) {
        // Save students affairs to the file
        String filePath = STUDENTS_AFFAIRS_FILE_PATH + studentsAffairs.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(studentsAffairs, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public StudentsAffairs getStudentsAffairs(String university_email) {
        // Read students affairs from the file
        String filePath = STUDENTS_AFFAIRS_FILE_PATH + university_email + ".json";
        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, StudentsAffairs.class);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean removeStudentsAffairs(StudentsAffairs studentsAffairs) {
        String filePath = STUDENTS_AFFAIRS_FILE_PATH + studentsAffairs.getUserInformation().get_UNIVERSITY_EMAIL() + ".json";
        java.io.File file = new java.io.File(filePath);
        if (file.exists()) {
            file.delete();
            return true;
        }

        return false;
    }

    //helper methods and variables for generating random objects
    private final String[] names = {"Ali", "Fatma", "Zeynep", "Ahmet", "Ayse", "Mehmet", "Emine", "Hasan", "Huseyin", "Elif", "Mustafa", "Sibel", "Burak", "Busra", "Omer", "Halime", "Murat", "Gizem", "Eren", "Esra", "Yusuf", "Melis", "Can", "Hatice", "Oguz", "Rabia", "Kerem", "Derya", "Furkan", "Sevgi", "Kadir", "Selin", "Ibrahim", "Tugce", "Cem", "Pelin", "Baris", "Leyla", "Serkan", "Sule", "Deniz", "Cansu", "Hakan", "Damla", "Merve", "Tolga", "Ezgi", "Volkan", "Dilara", "Uğur", "Selma", "Ece", "Adem", "Zeynep", "Burcu", "Ozan", "Cemile", "Yasemin", "Alper", "Duygu", "Serdar", "Gul", "Okan", "Seda", "Bora", "Nurgul", "Cagri", "Seyma", "Dogukan", "Gulsah", "Tuna", "Hande", "Gokhan", "Berna", "Caner", "Bahar", "Arda", "Necla", "Batuhan", "Hilal", "Atakan", "Tulay", "Cengiz", "Berke", "Perihan", "Ece", "Tayfun", "Ceyda", "Emirhan", "Gonca", "Erdem", "Ayla", "Tamer", "Isil", "Havva", "Sevda", "Gokce", "Alime"};
    private final String[] surnames = {"Yilmaz", "Kaya", "Demir", "Celik", "Sahin", "Arslan", "Aydin", "Eren", "Ozturk", "Yildiz", "Aslan", "Keskin", "Polat", "Dogan", "Koc", "Gunes", "Aksoy", "Karaca", "Uzun", "Kilic", "Tas", "Candan", "Erdogan", "Gul", "Yalcin", "Balci", "Kaplan", "Can", "Durmaz", "Cetin", "Turkmen", "Simsek", "Duman", "Sari", "Saglam", "Ucar", "Kurt", "Ozdemir", "Isik", "Ersoy", "Soylu", "Korkmaz", "Bulut", "Kavak", "Turan", "Altun", "Ozkan", "Kara", "Gunduz", "Ates", "Yucel", "Erdem", "Keser", "Celikkan", "Toprak", "Yalman", "Ari", "Bayrak", "Deniz", "Durak", "Gultekin", "Orhan", "Aktas", "Sezer", "Pala", "Karatas", "Aksu", "Goksel", "Bozkurt", "Yuksel", "Albayrak", "Ozen", "Seker", "Erol", "Akcay", "Ozdem", "Arman", "Karahan", "Tunc", "Oztan", "Batur", "Tokgoz", "Acar", "Ergin", "Ulu", "Uz", "Altay", "Soydan", "Koroglu", "Torun", "Akbas", "Kalayci", "Koksal", "Tuna", "Akin", "Guler", "Erkan", "Gokce"};
    private final String[] cities = {"Adana", "Adiyaman", "Afyonkarahisar", "Agri", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", "Aydin", "Balikesir", "Bartin", "Batman", "Bayburt", "Bilecik", "Bingol", "Bitlis", "Bolu", "Burdur", "Bursa", "Canakkale", "Cankiri", "Corum", "Denizli", "Diyarbakir", "Duzce", "Edirne", "Elazig", "Erzincan", "Erzurum", "Eskisehir", "Gaziantep", "Giresun", "Gumushane", "Hakkari", "Hatay", "Igdir", "Isparta", "Istanbul", "Izmir", "Kahramanmaras", "Karabuk", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kirikkale", "Kirklareli", "Kirsehir", "Kilis", "Kocaeli", "Konya", "Kutahya", "Malatya", "Manisa", "Mardin", "Mersin", "Mugla", "Mus", "Nevsehir", "Nigde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Sanliurfa", "Siirt", "Sinop", "Sirnak", "Sivas", "Tekirdag", "Tokat", "Trabzon", "Tunceli", "Usak", "Van", "Yalova", "Yozgat", "Zonguldak"};

    private String generateRandomName() {
        return names[(int) (Math.random() * names.length)];
    }

    private String generateRandomSurname() {
        return surnames[(int) (Math.random() * surnames.length)];
    }

    private String generateRandomCity() {
        return cities[(int) (Math.random() * cities.length)];
    }

    private String generateEmail(String name, String surname) {
        return name.toLowerCase() + surname.toLowerCase() + (int) (Math.random() * 1000) + "@gmail.com";
    }

    public String generateUniversityEmail(String name, String surname) {
        return name.toLowerCase() + surname.toLowerCase() + "@marun.edu.tr";
    }

    private String generatePhoneNumber() {
        String phoneNumber = "+90 5";
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10) + " ";
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10) + " ";
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10) + " ";
        phoneNumber += (int) (Math.random() * 10);
        phoneNumber += (int) (Math.random() * 10);
        return phoneNumber;
    }

    private String generatePassword(String name, String city, String phoneNumber) {
        return name.toLowerCase() + city.toUpperCase() + phoneNumber.substring(15);
    }

    private UserInformation generateRandomUserInformation() {
        String firstName = generateRandomName();
        String lastName = generateRandomSurname();
        String city = generateRandomCity();
        String phoneNumber = generatePhoneNumber();
        String password = generatePassword(firstName, city, phoneNumber);
        return new UserInformation(firstName, lastName, generateUniversityEmail(firstName, lastName), generateEmail(firstName, lastName), city, phoneNumber, LoginAuthService.hashPassword(password));
    }

    private Faculty generateFaculty(int FacultyID, String FacultyName) {
        return new Faculty(new FacultyID(FacultyID, FacultyName));
    }

    private Department generateDepartment(int DepartmentID, String DepartmentName, Faculty faculty) {
        Department d = new Department(new DepartmentID(DepartmentID, DepartmentName), faculty.getFacultyID());
        faculty.addDepartment(d);
        return d;
    }

    private Lecturer generateRandomLecturer(Department department) {
        UserInformation userInformation = generateRandomUserInformation();
        return new Lecturer(userInformation);
    }

    private Advisor generateRandomAdvisor(Department department) {
        UserInformation userInformation = generateRandomUserInformation();
        return new Advisor(userInformation);
    }

    public Student generateRandomStudent(Department department, int entrance_date, int entrance_rank, StaffId
            advisorID) {
        UserInformation userInformation = generateRandomUserInformation();
        StudentID studentID = new StudentID(department.getDepartmentID(), entrance_date, entrance_rank, department.get_facultyID());
        Transcript transcript = new Transcript(studentID);
        return new Student(userInformation, studentID, transcript, advisorID, 2024 - entrance_date + 1);
    }

    public Student generateNonRandomStudent(UserInformation userInformation, Department department,
                                            int entrance_date, int entrance_rank, StaffId advisorID) {
        StudentID studentID = new StudentID(department.getDepartmentID(), entrance_date, entrance_rank, department.get_facultyID());
        Transcript transcript = new Transcript(studentID);
        return new Student(userInformation, studentID, transcript, advisorID, 2024 - entrance_date + 1);
    }

    private CourseInformation generateCourseInformation(String courseName, String courseCode) {
        return new CourseInformation(courseName, courseCode);
    }

    private CourseRequirements generateCourseRequirements(ArrayList<CourseInformation> prerequisiteCourses,
                                                          int minimumCurrentClass, FacultyID facultyID, DepartmentID departmentID) {
        return new CourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID);
    }

    public Course generateCourse
            (ArrayList<Lecturer> lecturersForSections, ArrayList<Day> days, ArrayList<SectionTime> sectionTimes, String
                     courseName, String courseCode, ArrayList<CourseInformation> prerequisiteCourses,
             int minimumCurrentClass, FacultyID facultyID, DepartmentID departmentID) {
        CourseInformation courseInformation = generateCourseInformation(courseName, courseCode);
        CourseRequirements courseRequirements = generateCourseRequirements(prerequisiteCourses, minimumCurrentClass, facultyID, departmentID);
        ArrayList<CourseSection> courseSections = new ArrayList<>();
        for (int i = 0; i < lecturersForSections.size(); i++) {
            CourseSection courseSection = new CourseSection(days.get(i), sectionTimes.get(i), lecturersForSections.get(i));
            courseSections.add(courseSection);
        }
        return new Course(courseInformation, courseRequirements, courseSections);
    }

    private DepartmentScheduler generateRandomDepartmentScheduler(Department department) {
        UserInformation userInformation = generateRandomUserInformation();
        return new DepartmentScheduler(userInformation);
    }

    private StudentsAffairs generateRandomStudentsAffairs(Department department) {
        UserInformation userInformation = generateRandomUserInformation();
        return new StudentsAffairs(userInformation);
    }

}
