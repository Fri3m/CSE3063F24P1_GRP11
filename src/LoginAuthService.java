package src;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.util.Scanner;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.FileWriter;
import java.io.IOException;


public class LoginAuthService {

    private ArrayList<User> _users;
    public LoginAuthService() {
        _users = new ArrayList<>();
    }
    private String encoded_password;


    public static void main(String[] args) {
        LoginAuthService authService = new LoginAuthService();

        // Initialize the user list
        authService._users = new ArrayList<>();
        while(true) {
            System.out.println("1. Register\n2. Login\n3. Exit");
            Scanner scanner = new Scanner(System.in);
            int choice = scanner.nextInt();
            if (choice == 1) {
                authService.register("john.doe", "password123");
            } else if (choice == 2) {
                authService.login("john.doe@marun.edu.tr", "password123");
            } else if (choice == 3) {
                break;
            }
        }

    }
    public boolean login(String university_email, String password) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your university email: ");
        university_email = scanner.nextLine();

        System.out.println("Enter your password: ");
        password = scanner.nextLine();

        password = hashPassword(password);

        for (User user : _users) {
            if (user.getUserInformation().get_UNIVERSITY_EMAIL().equals(university_email)) {
                if (user.getUserInformation().get_encoded_password().equals(password)) {
                    System.out.println("Login successful");
                    return true;
                }
                else {
                    System.out.println("Please check your information and try again.");
                    return false;
                }
            }
        }

        return true;
    }

    public boolean register(String university_email, String password) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your first name: ");
        String first_name = scanner.nextLine();

        System.out.println("Enter your last name: ");
        String last_name = scanner.nextLine();

        System.out.println("Enter your phone number: ");
        String phone_number = scanner.nextLine();

        System.out.println("Enter your address: ");
        String address = scanner.nextLine();

        System.out.println("Enter your email: ");
        String email = scanner.nextLine();

        while (!validateEmail(email)) {
            System.out.println("Invalid email. Please enter a valid email");
            email = scanner.nextLine();
        }

        System.out.println("Enter your university email (Please enter until the part before the @ sign): ");
        university_email = scanner.nextLine();

        while (university_email.contains("@")|| isEmailRegistered(university_email + "@marun.edu.tr")) {
            if (university_email.contains("@")) {
                System.out.println("Please enter until the part before the @ sign.");
            } else {
                System.out.println("This email is already registered. Please enter a different university email.");
            }
            university_email = scanner.nextLine();
        }

        university_email += "@marun.edu.tr";

        System.out.println("Enter your password: ");
        password = scanner.nextLine();

        System.out.println("Choose your role: ");
        System.out.println("1. Student" + "\n" + "2. Lecturer" + "\n" + "3. Advisor");
        int role = scanner.nextInt();

        encoded_password = hashPassword(password);


        User user;

        if (role == 1) {
            user = new Student(new UserInformation(first_name, last_name, university_email, email, address, phone_number, encoded_password), new StudentID(new Department(new DepartmentID(2)), 2021, 1));
        } else if (role == 2) {
            user = new Lecturer(new UserInformation(first_name, last_name, university_email, email, address, phone_number, encoded_password));
        } else if (role == 3) {
            user = new Advisor(new UserInformation(first_name, last_name, university_email, email, address, phone_number, encoded_password));
        } else {
            System.out.println("Invalid role");
            return false;
        }

        _users.add(user);

        saveUsersToJson();

        return true;
    }
    //new function for UML
    public static String hashPassword(String password) {
        try {
            // Create MessageDigest instance for SHA-256
            MessageDigest digest = MessageDigest.getInstance("SHA-256");

            // Apply SHA-256 algorithm to password
            byte[] hash = digest.digest(password.getBytes());

            // Convert byte array into hexadecimal string
            StringBuilder hexString = new StringBuilder();
            for (byte b : hash) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }
            return hexString.toString();

        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
    //new function for UML
    public static boolean validateEmail(String email) {
        String regex = "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(email);
        return matcher.matches();
    }

    private boolean isEmailRegistered(String university_email) {
        for (User user : _users) {
            if (user.getUserInformation().get_UNIVERSITY_EMAIL().equals(university_email)) {
                return true; // Email is already registered
            }
        }
        return false; // Email is not registered
    }


    private void saveUsersToJson() {
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            File file = new File("src/main/resources/database/data.json");
            objectMapper.writerWithDefaultPrettyPrinter().writeValue(file, _users);

            System.out.println("User data saved to data.json.");
        } catch (IOException e) {
            System.err.println("An error occurred while saving user data: " + e.getMessage());
        }
    }

//    private void getFromFile(){
//
//    }
}