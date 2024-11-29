package src;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    private LoginAuthService _login_auth_service;
    private DataManagement _data_management;
    private CourseRegistrationService _course_registration_service;
    private ArrayList<Faculty> _faculties;
    private ArrayList<Department> _departments;
    private ArrayList<Student> _students;
    private ArrayList<Advisor> _advisors;
    private ArrayList<Lecturer> _lecturers;
    private ArrayList<Course> _courses;
    private Admin _admin;
    User user;
    String user_type;

    public static void main(String[] args) {
        Main main = new Main();
        main.startMenu();
    }

    private Main() {
        _data_management = new DataManagement();
        _login_auth_service = new LoginAuthService();
        _course_registration_service = new CourseRegistrationService();

        _faculties = _data_management.getAllFaculties();
        _departments = _data_management.getAllDepartments();
        _students = _data_management.getAllStudents();
        _advisors = _data_management.getAllAdvisors();
        _lecturers = _data_management.getAllLecturers();
        _courses = _data_management.getAllCourses();

        _admin = new Admin(new UserInformation(("admin"), ("admin"), ("admin"), ("admin"), ("admin"), ("admin"), LoginAuthService.hashPassword("admin")));

        ArrayList<User> users = new ArrayList<>();
        users.addAll(_students);
        users.addAll(_advisors);
        users.addAll(_lecturers);
        users.add(_admin);

        _login_auth_service._users = users;
        for (Department department : _departments) {
            for (Lecturer lecturer : _lecturers) {
                if (lecturer.get_departmentID() != null && lecturer.get_departmentID().getDepartmentID() == department.getDepartmentID().getDepartmentID()) {
                    department.addLecturer(lecturer);
                }
            }
        }
    }

    private void startMenu() {
        System.out.println("Welcome to the Course Registration System");
        System.out.println("Please choose an option:");
        System.out.println("1. Login");
        System.out.println("2. Exit");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        switch (input) {
            case "1":
                login();
                break;
            case "2":
                System.exit(0);
                break;
            default:
                System.out.println("Invalid input");
                startMenu();
        }
    }

    private void studentMainMenu() {
        Student student = (Student) user;
        System.out.println("Please choose an option:");
        System.out.println("1. Register for a course");
        System.out.println("2. Update user information");
        System.out.println("3. Show user information");
        System.out.println("4. Logout");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        switch (input) {
            case "1":
                System.out.println("Please choose a course to register:");
                for (Course course : _courses) {
                    System.out.println(course.getCourseName());
                }
                String course_name = scanner.nextLine();
                for (Course course : _courses) {
                    if (course.getCourseName().equals(course_name)) {
                        student.takeCourse(course, _course_registration_service);
                        break;
                    }
                }
                break;

            case "2":
                System.out.println("Please choose an information for update:");
                System.out.println("1. Change Password");
                System.out.println("2. Change Email");
                System.out.println("3. Change Address");
                System.out.println("4. Change Phone Number");
                System.out.println("5. Exit");
                String input_for_update = scanner.nextLine();
                switch (input_for_update) {
                    case "1":
                        changePassword();
                        break;
                    case "2":
                        changeEmail();
                        break;
                    case "3":
                        changeAddress();
                        break;
                    case "4":
                        changePhoneNumber();
                        break;
                    case "5":
                        System.out.println("Return to the main menu.");
                        break;
                }
                break;
            case "3":
                System.out.println("Name: " + student.getUserInformation().get_FIRST_NAME());
                System.out.println("Surname: " + student.getUserInformation().get_LAST_NAME());
                System.out.println("Email: " + student.getUserInformation().get_email());
                System.out.println("Address: " + student.getUserInformation().get_address());
                System.out.println("Phone Number: " + student.getUserInformation().get_phone_number());
                System.out.println("Student ID: " + student.get_studentID().get_ID());
                break;
            case "4":
                startMenu();
                return;
            default:
                System.out.println("Invalid input");

        }
        studentMainMenu();
    }

    private void lecturerMainMenu() {
        Lecturer lecturer = (Lecturer) user;
        System.out.println("Please choose an option:");
        System.out.println("1. Show user information");
        System.out.println("2. Update user information");
        System.out.println("3. Logout");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        switch (input) {
            case "1":
                System.out.println("Name: " + lecturer.getUserInformation().get_FIRST_NAME());
                System.out.println("Surname: " + lecturer.getUserInformation().get_LAST_NAME());
                System.out.println("Email: " + lecturer.getUserInformation().get_email());
                System.out.println("Address: " + lecturer.getUserInformation().get_address());
                System.out.println("Phone Number: " + lecturer.getUserInformation().get_phone_number());
                break;
            case "2":
                System.out.println("Please choose an information for update:");
                System.out.println("1. Change Password");
                System.out.println("2. Change Email");
                System.out.println("3. Change Address");
                System.out.println("4. Change Phone Number");
                System.out.println("5. Exit");
                String input_for_update = scanner.nextLine();
                switch (input_for_update) {
                    case "1":
                        changePassword();
                        break;
                    case "2":
                        changeEmail();
                        break;
                    case "3":
                        changeAddress();
                        break;
                    case "4":
                        changePhoneNumber();
                        break;
                    case "5":
                        System.out.println("Returning to the main menu.");
                        break;
                }
                break;
            case "3":
                startMenu();
                return;
            default:
                System.out.println("Invalid input");

        }
        lecturerMainMenu();
    }

    private void advisorMainMenu() {
        Advisor advisor = (Advisor) user;
        System.out.println("Please choose an option:");
        System.out.println("1. Check request of course request");
        System.out.println("2. Show user information");
        System.out.println("3. Update user information");
        System.out.println("4. Logout");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        switch (input) {
            case "1":
                advisor.checkRegistration(_course_registration_service);
                break;
            case "2":
                System.out.println("Name: " + user.getUserInformation().get_FIRST_NAME());
                System.out.println("Surname: " + user.getUserInformation().get_LAST_NAME());
                System.out.println("Email: " + user.getUserInformation().get_email());
                System.out.println("Address: " + user.getUserInformation().get_address());
                System.out.println("Phone Number: " + user.getUserInformation().get_phone_number());

                break;
            case "3":
                System.out.println("Please choose an information for update:");
                System.out.println("1. Change Password");
                System.out.println("2. Change Email");
                System.out.println("3. Change Address");
                System.out.println("4. Change Phone Number");
                System.out.println("5. Exit");
                String input_for_update = scanner.nextLine();
                switch (input_for_update) {
                    case "1":
                        changePassword();
                        break;
                    case "2":
                        changeEmail();
                        break;
                    case "3":
                        changeAddress();
                        break;
                    case "4":
                        changePhoneNumber();
                        break;
                    case "5":
                        System.out.println("Exiting the program.");
                        break;
                }
                break;
            case "4":
                startMenu();
                return;
            default:
                System.out.println("Invalid input");
        }
        advisorMainMenu();
    }

    private void adminMainMenu() {
        System.out.println("Please choose an option:");
        System.out.println("1. Add a new student");
        System.out.println("2. Add a new randomly generated student");
        System.out.println("3. Remove a student");
        System.out.println("4. Logout");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        switch (input) {
            case "1":
                UserInformation userInformation = adminCreateUserInformation();
                System.out.println("Please choose a department:");
                for (Department department : _departments) {
                    System.out.println(department.getDepartmentID().getDepartmentName());
                }
                Department department = null;
                while (true) {
                    String department_name = scanner.nextLine();
                    for (Department d : _departments) {
                        if (d.getDepartmentID().getDepartmentName().equals(department_name)) {
                            department = d;
                            break;
                        }
                    }
                    if (department != null) {
                        break;
                    }
                    System.out.println("Invalid department name. Please try again.");
                }
                System.out.println("Enter entrance date: ");
                int entrance_date;
                while (true) {
                    try {
                        entrance_date = Integer.parseInt(scanner.nextLine());
                        break;
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid entrance date. Please try again.");
                    }
                }
                System.out.println("Enter entrance rank: ");
                int entrance_rank;
                while (true) {
                    try {
                        entrance_rank = Integer.parseInt(scanner.nextLine());
                        break;
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid entrance rank. Please try again.");
                    }
                }

                System.out.println("Select a advisor: ");
                for (Advisor advisor : _advisors) {
                    System.out.println(advisor.getUserInformation().get_FIRST_NAME() + " " + advisor.getUserInformation().get_LAST_NAME());
                }
                StaffId advisorID = null;
                while (true) {
                    String advisor_name = scanner.nextLine();
                    for (Advisor advisor : _advisors) {
                        if ((advisor.getUserInformation().get_FIRST_NAME() + " " + advisor.getUserInformation().get_LAST_NAME()).equals(advisor_name)) {
                            advisorID = advisor.get_staffId();
                            break;
                        }
                    }
                    if (advisorID != null) {
                        break;
                    }
                    System.out.println("Invalid advisor name. Please try again.");
                }

                Student student = _data_management.generateNonRandomStudent(userInformation, department, entrance_date, entrance_rank, advisorID);
                _data_management.createOrChangeStudent(student);
                _students.add(student);
                _login_auth_service._users.add(student);
                System.out.println("Student " + student.getUserInformation().get_FIRST_NAME() + " " + student.getUserInformation().get_LAST_NAME() + " added successfully.");

                break;
            case "2":
                Department d = _departments.get((int) (Math.random() * _departments.size()));
                int entranceRank = (int) (Math.random() * 1000);

                while (true) {
                    boolean found = false;
                    for (Student s : _students) {
                        if (s.get_studentID().get_entrance_rank() == entranceRank && s.get_studentID().get_entrance_date() == 2024) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        break;
                    }
                    entranceRank = (int) (Math.random() * 1000);
                }

                StaffId advisorID2 = _advisors.get((int) (Math.random() * _advisors.size())).get_staffId();
                Student student2 = _data_management.generateRandomStudent(d, 2024, entranceRank, advisorID2);
                _data_management.createOrChangeStudent(student2);
                _students.add(student2);
                _login_auth_service._users.add(student2);
                System.out.println("Student " + student2.getUserInformation().get_FIRST_NAME() + " " + student2.getUserInformation().get_LAST_NAME() + " added successfully.");
                break;
            case "3":
                System.out.println("Please choose a student to remove:");
                for (Student student1 : _students) {
                    System.out.println(student1.getUserInformation().get_UNIVERSITY_EMAIL());
                }
                String student_email = scanner.nextLine();
                boolean studentExists = false;
                for (Student student1 : _students) {
                    if (student1.getUserInformation().get_UNIVERSITY_EMAIL().equals(student_email)) {
                        _students.remove(student1);
                        _login_auth_service._users.remove(student1);
                        _data_management.removeStudent(student1);
                        System.out.println("Student " + student1.getUserInformation().get_FIRST_NAME() + " " + student1.getUserInformation().get_LAST_NAME() + " removed successfully.");
                        studentExists = true;
                        break;
                    }
                }
                if (!studentExists) {
                    System.out.println("Student not found.");
                }

                break;
            case "4":
                startMenu();
                return;
            default:
                System.out.println("Invalid input");
        }
        advisorMainMenu();
    }

    private UserInformation adminCreateUserInformation() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter name: ");
        String name = scanner.nextLine();
        System.out.println("Enter surname: ");
        String surname = scanner.nextLine();
        String universityEmail = _data_management.generateUniversityEmail(name, surname);
        System.out.println("Created university email is: " + universityEmail);
        System.out.println("Enter email: ");
        String email = scanner.nextLine();
        System.out.println("Enter address (City only): ");
        String address = scanner.nextLine();
        System.out.println("Enter phone number: ");
        String phone_number = scanner.nextLine();
        System.out.println("Enter password: ");
        String password = scanner.nextLine();
        return new UserInformation(name, surname, universityEmail, email, address, phone_number, LoginAuthService.hashPassword(password));
    }

    private void departmentSchedulerMainMenu() {
        DepartmentScheduler departmentScheduler = (DepartmentScheduler) user;
        System.out.println("Please choose an option:");
        System.out.println("1. Change Course Section");
        System.out.println("2. Show user information");
        System.out.println("3. Update user information");
        System.out.println("4. Logout");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        switch (input) {
            case "1":
                System.out.println("Select department to continue");
                for (Department department : _departments) {
                    System.out.println(department.getDepartmentID().getDepartmentName());
                }
                Department department = null;
                while (true) {
                    String departmentSelection = scanner.nextLine();
                    boolean found = false;
                    for (Department d : _departments) {
                        if (departmentSelection.equals(d.getDepartmentID().getDepartmentName())) {
                            found = true;
                            department = d;
                            break;
                        }
                    }
                    if (found) {
                        break;
                    }
                }
                System.out.println("Select course to continue");
                ArrayList<Course> coursesForThisDepartment = new ArrayList<>();
                for (Course c : _courses) {
                    if (c.getCourseRequirements().get_departmentID().getDepartmentID() == 0 || c.getCourseRequirements().get_departmentID().getDepartmentID() == department.getDepartmentID().getDepartmentID()) {
                        coursesForThisDepartment.add(c);
                        System.out.println(c.getCourseRequirements().get_departmentID().getDepartmentName());
                    }
                }
                Course course = null;
                while (true) {
                    String courseSelection = scanner.nextLine();
                    boolean found = false;
                    for (Course c : coursesForThisDepartment) {
                        if (c.getCourseName().equals(courseSelection)) {
                            found = true;
                            course = c;
                            break;
                        }
                    }
                    if (found) break;
                }
                ;
                if (course.getCourseSections().isEmpty()) {
                    System.out.println("There is no course section for this course!");
                    break;
                }

                for (CourseSection courseSection : course.getCourseSections()) {
                    System.out.println("This course section is in day " + courseSection._day + " time " + courseSection._sectionTime);
                    System.out.println("Do you want to change this section day or time? Yes if continue: ");
                    String inp = scanner.nextLine();
                    if (!inp.equals("yes") && !inp.equals("Yes")) break;
                    while (true) {
                        boolean x = true;
                        System.out.println("Enter the day(Monday, Tuesday, Wednesday, Thursday, Friday): ");
                        inp = scanner.nextLine();
                        switch (inp.toLowerCase()) {
                            case "monday":
                                System.out.println("This section day changed to Monday");
                                courseSection._day = Day.Monday;
                                break;
                            case "tuesday":
                                System.out.println("This section day changed to Tuesday");
                                courseSection._day = Day.Tuesday;
                                break;
                            case "wednesday":
                                System.out.println("This section day changed to Wednesday");
                                courseSection._day = Day.Wednesday;
                                break;
                            case "thursday":
                                System.out.println("This section day changed to Thursday");
                                courseSection._day = Day.Thursday;
                                break;
                            case "friday":
                                System.out.println("This section day changed to Friday");
                                courseSection._day = Day.Friday;
                                break;
                            default:
                                x = false;
                                System.out.println("Invalid input!");
                                break;
                        }
                        if (x) break;
                    }

                    while (true) {
                        boolean x = true;
                        System.out.println("Enter the section time(First, Second, Third,Fourth, Fifth, Sixth, Seventh, Eighth, Ninth)");
                        inp = scanner.nextLine();
                        switch (inp.toLowerCase()) {
                            case "first":
                                courseSection._sectionTime = SectionTime.First;
                                System.out.println("This section time changed to First");
                                break;
                            case "second":
                                courseSection._sectionTime = SectionTime.Second;
                                System.out.println("This section time changed to Second");
                                break;
                            case "third":
                                courseSection._sectionTime = SectionTime.Third;
                                System.out.println("This section time changed to Third");
                                break;
                            case "fourth":
                                courseSection._sectionTime = SectionTime.Fourth;
                                System.out.println("This section time changed to Fourth");
                            case "fifth":
                                courseSection._sectionTime = SectionTime.Fifth;
                                System.out.println("This section time changed to Fifth");
                                break;
                            case "sixth":
                                courseSection._sectionTime = SectionTime.Sixth;
                                System.out.println("This section time changed to Sixth");
                                break;
                            case "seventh":
                                courseSection._sectionTime = SectionTime.Seventh;
                                System.out.println("This section time changed to Seventh");
                                break;
                            case "eighth":
                                courseSection._sectionTime = SectionTime.Eighth;
                                System.out.println("This section time changed to Eighth");
                                break;
                            case "ninth":
                                courseSection._sectionTime = SectionTime.Ninth;
                                System.out.println("This section time changed to Ninth");
                                break;
                            default:
                                x = false;
                                System.out.println("Invalid input!");
                                break;

                        }
                        if (x) break;


                    }

                }
                _data_management.createOrChangeCourse(course);
                System.out.println("Course sections changed successfully!");


                break;
            case "2":
                System.out.println("Name: " + departmentScheduler.getUserInformation().get_FIRST_NAME());
                System.out.println("Surname: " + departmentScheduler.getUserInformation().get_LAST_NAME());
                System.out.println("Email: " + departmentScheduler.getUserInformation().get_email());
                System.out.println("Address: " + departmentScheduler.getUserInformation().get_address());
                System.out.println("Phone Number: " + departmentScheduler.getUserInformation().get_phone_number());
                break;
            case "3":
                System.out.println("Please choose an information for update:");
                System.out.println("1. Change Password");
                System.out.println("2. Change Email");
                System.out.println("3. Change Address");
                System.out.println("4. Change Phone Number");
                System.out.println("5. Exit");
                String input_for_update = scanner.nextLine();
                switch (input_for_update) {
                    case "1":
                        changePassword();
                        break;
                    case "2":
                        changeEmail();
                        break;
                    case "3":
                        changeAddress();
                        break;
                    case "4":
                        changePhoneNumber();
                        break;
                    case "5":
                        System.out.println("Returning to the main menu.");
                        break;
                }
                break;
            case "4":
                startMenu();
                return;
            default:
                System.out.println("Invalid input");

        }
        departmentSchedulerMainMenu();
    }

    private void studentsAffairMainMenu() {
        StudentsAffairs studentsAffairs = (StudentsAffairs) user;
        System.out.println("Please choose an option:");
        System.out.println("1. Add new course");
        System.out.println("2. Remove course");
        System.out.println("3. Show user information");
        System.out.println("4. Update user information");
        System.out.println("5. Logout");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        switch (input) {
            case "1":
                System.out.println("Enter course name: ");
                String course_name = scanner.nextLine();
                System.out.println("Enter course code: ");
                String course_code = scanner.nextLine();
                int min_current_class;
                while (true) {
                    boolean x = true;
                    System.out.println("Enter minimum current class requirement: ");
                    try {
                        min_current_class = Integer.parseInt(scanner.nextLine());
                    } catch (NumberFormatException e) {
                        x = false;
                        System.out.println("Invalid input!");
                        continue;
                    }
                    if (x) break;
                }
                System.out.println("If your course has a department requirement, enter the department name. If not, enter anything: ");
                for (Department department : _departments) {
                    System.out.println(department.getDepartmentID().getDepartmentName());
                }
                String inp = scanner.nextLine();
                Department department = null;
                for (Department d : _departments) {
                    if (d.getDepartmentID().getDepartmentName().equals(inp)) {
                        department = d;
                        break;
                    }
                }
                if (department == null) {
                    department = new Department(new DepartmentID(0, "No Department"), new FacultyID(0, "No Faculty"));
                }
                System.out.println("Enter all the prerequisites for this course. When you are finished, type 'finished'");
                for (Course course : _courses) {
                    System.out.println(course.getCourseName());
                }
                ArrayList<CourseInformation> prerequisites = new ArrayList<>();
                do {
                    inp = scanner.nextLine();
                    for (Course course : _courses) {
                        if (course.getCourseName().equals(inp)) {
                            prerequisites.add(course.getCourseInformation());
                            break;
                        }
                    }
                } while (!inp.toLowerCase().equals("finished"));

                System.out.println("Enter the number of sections for this course: ");
                int section_number;
                while (true) {
                    boolean x = true;
                    try {
                        section_number = Integer.parseInt(scanner.nextLine());
                    } catch (NumberFormatException e) {
                        x = false;
                        System.out.println("Invalid input!");
                        continue;
                    }
                    if (x) break;
                }
                ArrayList<Lecturer> lecturerArrayList = new ArrayList<>();
                System.out.println("Select lecturers for this course: ");
                for (Lecturer lecturer : _lecturers) {
                    System.out.println(lecturer.getUserInformation().get_FIRST_NAME() + " " + lecturer.getUserInformation().get_LAST_NAME());
                }
                for (int i = 0; i< section_number;i++){
                    System.out.println("Enter lecturer name for section " + (i+1) + ": ");
                    String lecturer_name = scanner.nextLine();
                    for (Lecturer lecturer : _lecturers) {
                        if ((lecturer.getUserInformation().get_FIRST_NAME() + " " + lecturer.getUserInformation().get_LAST_NAME()).equals(lecturer_name)) {
                            lecturerArrayList.add(lecturer);
                            break;
                        }
                    }
                }

                ArrayList<Day> dayArrayList = new ArrayList<>();
                ArrayList<SectionTime> sectionTimeArrayList = new ArrayList<>();

                for (int i = 0; i< section_number;i++){
                    System.out.println("Enter day for section " + (i+1) + ": ");
                    String day = scanner.nextLine();
                    switch (day.toLowerCase()) {
                        case "monday":
                            dayArrayList.add(Day.Monday);
                            break;
                        case "tuesday":
                            dayArrayList.add(Day.Tuesday);
                            break;
                        case "wednesday":
                            dayArrayList.add(Day.Wednesday);
                            break;
                        case "thursday":
                            dayArrayList.add(Day.Thursday);
                            break;
                        case "friday":
                            dayArrayList.add(Day.Friday);
                            break;
                        default:
                            System.out.println("Invalid input!");
                            i--;
                            continue;
                    }
                    System.out.println("Enter section time for section " + (i+1) + ": ");
                    String sectionTime = scanner.nextLine();
                    switch (sectionTime.toLowerCase()) {
                        case "first":
                            sectionTimeArrayList.add(SectionTime.First);
                            break;
                        case "second":
                            sectionTimeArrayList.add(SectionTime.Second);
                            break;
                        case "third":
                            sectionTimeArrayList.add(SectionTime.Third);
                            break;
                        case "fourth":
                            sectionTimeArrayList.add(SectionTime.Fourth);
                            break;
                        case "fifth":
                            sectionTimeArrayList.add(SectionTime.Fifth);
                            break;
                        case "sixth":
                            sectionTimeArrayList.add(SectionTime.Sixth);
                            break;
                        case "seventh":
                            sectionTimeArrayList.add(SectionTime.Seventh);
                            break;
                        case "eighth":
                            sectionTimeArrayList.add(SectionTime.Eighth);
                            break;
                        case "ninth":
                            sectionTimeArrayList.add(SectionTime.Ninth);
                            break;
                        default:
                            System.out.println("Invalid input!");
                            i--;
                            continue;
                    }
                }

                Course course = _data_management.generateCourse(lecturerArrayList, dayArrayList, sectionTimeArrayList,course_name,course_code,prerequisites,min_current_class, department.get_facultyID(), department.getDepartmentID());
                _data_management.createOrChangeCourse(course);
                _courses.add(course);
                break;
            case "2":
                System.out.println("Enter a course name to remove: ");
                String cName = scanner.nextLine();
                boolean x = false;
                for (Course c : _courses) {
                    if (c.getCourseName().equals(cName)) {
                        _data_management.removeCourse(c);
                        _courses.remove(c);
                        System.out.println("Course " + cName + " removed successfully.");
                        x = true;
                        break;
                    }
                }
                if (!x) {
                    System.out.println("Course not found.");
                }
                break;
            case "3":
                System.out.println("Name: " + studentsAffairs.getUserInformation().get_FIRST_NAME());
                System.out.println("Surname: " + studentsAffairs.getUserInformation().get_LAST_NAME());
                System.out.println("Email: " + studentsAffairs.getUserInformation().get_email());
                System.out.println("Address: " + studentsAffairs.getUserInformation().get_address());
                System.out.println("Phone Number: " + studentsAffairs.getUserInformation().get_phone_number());
                break;
            case "4":
                System.out.println("Please choose an information for update:");
                System.out.println("1. Change Password");
                System.out.println("2. Change Email");
                System.out.println("3. Change Address");
                System.out.println("4. Change Phone Number");
                System.out.println("5. Exit");
                String input_for_update = scanner.nextLine();
                switch (input_for_update) {
                    case "1":
                        changePassword();
                        break;
                    case "2":
                        changeEmail();
                        break;
                    case "3":
                        changeAddress();
                        break;
                    case "4":
                        changePhoneNumber();
                        break;
                    case "5":
                        System.out.println("Returning to the main menu.");
                        break;
                }
                break;
            case "5":
                startMenu();
                return;
            default:
                System.out.println("Invalid input");

        }
        studentsAffairMainMenu();
    }


    private void login() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Which type of user are you? (Student, Advisor, Lecturer, Admin, DepartmentScheduler, StudentAffair)");
        user_type = scanner.nextLine();
        System.out.println("Enter your university email: ");
        String email = scanner.nextLine();
        System.out.println("Enter your password: ");
        String password = scanner.nextLine();

        user = _login_auth_service.login(email, password);
        if (user == null) user_type = "null";

        switch (user_type) {
            case "Student":
                studentMainMenu();
                break;
            case "Advisor":
                advisorMainMenu();
                break;
            case "Lecturer":
                lecturerMainMenu();
                break;
            case "Admin":
                adminMainMenu();
                break;
            case "DepartmentScheduler":
                departmentSchedulerMainMenu();
                break;
            case "StudentAffair":
                studentsAffairMainMenu();
                break;
            default:
                System.out.println("Invalid login. To retry enter 1, to return to the main menu enter any other key");
                String input = scanner.nextLine();
                if (input.equals("1")) {
                    login();
                } else {
                    startMenu();
                }
        }
    }

    /*
    private void register() {
        Scanner scanner = new Scanner(System.in);

        if (_login_auth_service.register()) {
            System.out.println("Registration successful. Please login to continue.");
            startMenu();
        } else {
            System.out.println("Registration failed");
            System.out.println("If you want to try again enter 1, for returning to the main menu enter any other key");
            String input = scanner.nextLine();
            if (input.equals("1")) {
                register();
            } else {
                startMenu();
            }
        }
    }*/
    private void changePassword() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your current password: ");
        String current_password = scanner.nextLine();
        System.out.println("Enter your new password: ");
        String new_password = scanner.nextLine();
        if (user.getUserInformation().changePassword(LoginAuthService.hashPassword(current_password), LoginAuthService.hashPassword(new_password))) {
            System.out.println("Password updated successfully");
        } else {
            System.out.println("Password update failed. Please try again.");
        }
    }

    private void changeEmail() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter current password: ");
        String currentPassword = scanner.nextLine();
        System.out.print("Enter new email: ");
        String newEmail = scanner.nextLine();

        if (user.getUserInformation().changeEmail(LoginAuthService.hashPassword(currentPassword), newEmail)) {
            System.out.println("Email updated successfully to " + user.getUserInformation().get_email());
        } else {
            System.out.println("Incorrect password. Email not updated.");
        }
    }

    private void changeAddress() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter current password: ");
        String currentPassword = scanner.nextLine();
        System.out.print("Enter new address: ");
        String newAddress = scanner.nextLine();

        if (user.getUserInformation().changeAddress(LoginAuthService.hashPassword(currentPassword), newAddress)) {
            System.out.println("Address updated successfully to " + user.getUserInformation().get_address());
        } else {
            System.out.println("Incorrect password. Address not updated.");
        }
    }

    private void changePhoneNumber() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter current password: ");
        String currentPassword = scanner.nextLine();
        System.out.print("Enter new phone number: ");
        String newPhoneNumber = scanner.nextLine();

        if (user.getUserInformation().changePhoneNumber(LoginAuthService.hashPassword(currentPassword), newPhoneNumber)) {
            System.out.println("Phone number updated successfully to " + user.getUserInformation().get_phone_number());
        } else {
            System.out.println("Incorrect password. Phone number not updated.");
        }

    }


}
