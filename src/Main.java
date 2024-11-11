package src;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    private LoginAuthService _login_auth_service;
    private CourseRegistrationService _course_registration_service;
    private ArrayList<Faculty> _faculties;
    private ArrayList<Department> _departments;
    private ArrayList<Student> _students;
    private ArrayList<Advisor> _advisors;
    private ArrayList<Lecturer> _lecturers;
    private ArrayList<Course> _courses;
    User user;
    String user_type;

    public static void main(String[] args) {
        Main main = new Main();
        main.startMenu();
    }
    private Main() {
        _login_auth_service = new LoginAuthService();
        _course_registration_service = new CourseRegistrationService();
        _faculties = _login_auth_service.loadFacultiesFromFile();
        _departments = _login_auth_service.loadDepartmentsFromFile();
        _students = _login_auth_service.loadStudentsFromFile();
        _advisors = _login_auth_service.loadAdvisorsFromFile();
        _lecturers = _login_auth_service.loadLecturersFromFile();
        _courses = _login_auth_service.loadCourseFromFile();
        ArrayList<User> users = new ArrayList<>();
        users.addAll(_students);
        users.addAll(_advisors);
        users.addAll(_lecturers);
        _login_auth_service._users = users;
        for (Student student : _students) {
            for(Department department : _departments) {
                if (student.get_studentID().get_departmentID().getDepartmentID() == department.getDepartmentID().getDepartmentID()) {
                   department.get_students().add(student);
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
                for(Course course : _courses) {
                    System.out.println(course.getCourseName());
                }
                String course_name = scanner.nextLine();
                for(Course course : _courses) {
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
                break;
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
                break;
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
                break;
            default:
                System.out.println("Invalid input");
        }
        advisorMainMenu();
    }

    private void login() {
        Scanner scanner = new Scanner(System.in);
        user = _login_auth_service.login();
        if (user!=null) {
            System.out.println("Login successful");
            if(user instanceof Student) {
                user_type = "Student";
                studentMainMenu();

            }
            else if(user instanceof Advisor) {
                user_type = "Advisor";
                advisorMainMenu();
            }else if(user instanceof Lecturer) {
                user_type = "Lecturer";
                lecturerMainMenu();
            }
        } else {
            System.out.println("Login failed");
            System.out.println("If you want to try again enter 1, for returning to the main menu enter any other key");
            String input = scanner.nextLine();
            if (input.equals("1")) {
                login();
            } else {
                startMenu();
            }
        }
    }/*
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
        if(user.getUserInformation().changePassword(LoginAuthService.hashPassword(current_password), LoginAuthService.hashPassword(new_password))) {
            System.out.println("Password updated successfully");
        }
        else {
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
