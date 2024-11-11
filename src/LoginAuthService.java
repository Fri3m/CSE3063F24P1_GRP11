package src;
import java.util.Scanner;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.FileWriter;
import java.io.IOException;
//import com.google.gson.Gson;
//import com.google.gson.GsonBuilder;

public class LoginAuthService {
    private ArrayList<User> _users;
    public LoginAuthService() {}
    private String encoded_password;

    public static void main(String[] args) {
        LoginAuthService authService = new LoginAuthService();

        // Initialize the user list
        authService._users = new ArrayList<>();

        // Register a user
        System.out.println("Registering a new user:");
        boolean registrationSuccess = authService.register("john.doe", "password123");
        if (registrationSuccess) {
            System.out.println("Registration successful.\n");
        } else {
            System.out.println("Registration failed.\n");
            return;
        }

        // Attempt to log in with the registered user
        System.out.println("Attempting to log in:");
        boolean loginSuccess = authService.login("john.doe@marun.edu.tr", "password123");
        if (loginSuccess) {
            System.out.println("Login successful.");
        } else {
            System.out.println("Login failed.");
        }
    }
    public boolean login(String university_email, String password) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your university email: ");
        university_email = scanner.nextLine();

        System.out.println("Enter your password: ");
        password = scanner.nextLine();

        for (User user : _users) {
            if (user.getUserInformation().get_UNIVERSITY_EMAIL().equals(university_email)) {
                if (user.getUserInformation().get_encoded_password().equals(encoded_password)) {
                    System.out.println("Login successful");
                    return true;
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

        while (university_email.contains("@")) {
            System.out.println("Please enter until the part before the @ sign.");
            university_email = scanner.nextLine();
        }

        university_email += "@marun.edu.tr";

        System.out.println("Enter your password: ");
        password = scanner.nextLine();

        System.out.println("Choose your role: ");
        System.out.println("1. Student" + "\n" + "2. Lecturer" + "\n" + "3. Advisor");
        int role = scanner.nextInt();

        encoded_password = hashPassword(password);

        if(role == 1){
            Student student = new Student(new UserInformation(first_name, last_name, university_email, email, address, phone_number, password),new StudentID( new Department(new DepartmentID(2)), 2021, 1));
        }
        else if(role == 2){
            Lecturer lecturer = new Lecturer(new UserInformation(first_name, last_name, university_email, email, address, phone_number, encoded_password));
        }
        else if(role == 3){
            Advisor advisor = new Advisor(new UserInformation(first_name, last_name, university_email, email, address, phone_number, encoded_password));
        }
        else{
            System.out.println("Invalid role");
        }



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
  /*  private void saveUsersToJson() {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();

        try (FileWriter writer = new FileWriter("users.json")) {
            gson.toJson(_users, writer);
            System.out.println("User data saved to users.json.");
        } catch (IOException e) {
            System.err.println("An error occurred while saving user data: " + e.getMessage());
        }
    }
*/
//    private void getFromFile(){
//
//    }
}
