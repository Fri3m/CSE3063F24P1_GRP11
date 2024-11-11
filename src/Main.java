package src;

import java.util.Scanner;

public class Main {
    private LoginAuthService _login_auth_service;
    private CourseRegistrationService _course_registration_service;
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
//                register();
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

    private void login() {
        System.out.println("Please enter your university email:");
        Scanner scanner = new Scanner(System.in);
        String email = scanner.nextLine();
        System.out.println("Please enter your password:");
        String password = scanner.nextLine();
        if (_login_auth_service.login(email, password)) {
            System.out.println("Login successful");
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


}
