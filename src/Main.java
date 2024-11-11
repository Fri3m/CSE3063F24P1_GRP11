package src;

import java.util.Scanner;

public class Main {
    private LoginAuthService _login_auth_service;
    private CourseRegistrationService _course_registration_service;
    private UserInformation _user_information;

    public static void main(String[] args) {
        Main main = new Main();
        main.startMenu();
    }
    private Main() {
        _login_auth_service = new LoginAuthService();
        _course_registration_service = new CourseRegistrationService();
    }

    private void startMenu() {
        System.out.println("Welcome to the Course Registration System");
        System.out.println("Please choose an option:");
        System.out.println("1. Login");
        System.out.println("2. Register");
        System.out.println("3. Exit");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        switch (input) {
            case "1":
            case "Login":
            case "login":
            case "log in":
            case "LOGIN":
                login();
                break;
            case "2":
            case "Register":
            case "register":
            case "REGISTER":
                register();
                break;
            case "3":
            case "exit":
            case "Exit":
            case "e":
            case "E":
            case "EXIT":
                System.exit(0);
                break;
            default:
                System.out.println("Invalid input");
                startMenu();
        }
    }
    private void mainMenu() {
        System.out.println("Please choose an option:");
        System.out.println("1. Register for a course");
        System.out.println("2. View registered courses");
        System.out.println("3. Update user information");
        System.out.println("4. Logout");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        switch (input) {
            case "1":
            case "Register":
            case "register":
            case "REGISTER":
             //   registerCourse();
                break;
            case "2":
            case "View":
            case "view":
            case "VIEW":
              //  viewCourses();
                break;
            case "3":
            case "Update":
            case "update":
            case "UPDATE":
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
            case "Logout":
            case "logout":
            case "LOGOUT":
                startMenu();
                break;
            default:
                System.out.println("Invalid input");
                mainMenu();
        }
    }

    private void login() {
        Scanner scanner = new Scanner(System.in);

        if (_login_auth_service.login()) {
            System.out.println("Login successful");
            mainMenu();
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
    }
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
    }
    private void changePassword() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your current password: ");
        String current_password = scanner.nextLine();
        System.out.println("Enter your new password: ");
        String new_password = scanner.nextLine();
        if (_user_information.changePassword(current_password, new_password)) {
            System.out.println("Password updated successfully");
        } else {
            System.out.println("Password update failed");
        }
    }
    private void changeEmail() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter current password: ");
        String currentPassword = scanner.nextLine();
        System.out.print("Enter new email: ");
        String newEmail = scanner.nextLine();

        if (_user_information.changeEmail(LoginAuthService.hashPassword(currentPassword), newEmail)) {
            System.out.println("Email updated successfully to " + _user_information.get_email());
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

        if (_user_information.changeAddress(LoginAuthService.hashPassword(currentPassword), newAddress)) {
            System.out.println("Address updated successfully to " + _user_information.get_address());
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

        if (_user_information.changePhoneNumber(LoginAuthService.hashPassword(currentPassword), newPhoneNumber)) {
            System.out.println("Phone number updated successfully to " + _user_information.get_phone_number());
        } else {
            System.out.println("Incorrect password. Phone number not updated.");
        }

    }



}
