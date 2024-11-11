package src;


import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.File;
import java.io.FileReader;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Scanner;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.FileWriter;
import java.io.IOException;


public class LoginAuthService {

    private ArrayList<User> _users = new ArrayList<>();
    public LoginAuthService() {
    }
    private String encoded_password;


    public boolean login() {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your university email: ");
        String email = scanner.nextLine();
        System.out.println("Enter your password: ");
        String password = scanner.nextLine();
        password = hashPassword(password);

        for (User user : _users) {
            if (user.getUserInformation().get_UNIVERSITY_EMAIL().equals(email)) {
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

    public boolean register() {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your first name: ");
        String first_name = scanner.nextLine();
        System.out.println("Enter your last name: ");
        String last_name = scanner.nextLine();
        System.out.println("Enter your address: ");
        String address = scanner.nextLine();
        System.out.println("Enter your phone number: ");
        String phone_number = scanner.nextLine();

        System.out.println("Enter your email: ");
        String email = scanner.nextLine();
        while (!validateEmail(email)) {
            System.out.println("Invalid email. Please enter a valid email");
            email = scanner.nextLine();
        }

        System.out.println("Enter your university email. (Please enter until before the @ sign): ");
        String university_email = scanner.nextLine();

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
        String password = scanner.nextLine();

        System.out.println("Choose your role: ");
        System.out.println("1. Student" + "\n" + "2. Lecturer" + "\n" + "3. Advisor");
        int role = scanner.nextInt();

        encoded_password = hashPassword(password);

        User user;

        if (role == 1) {
            user = new Student(new UserInformation(first_name, last_name, university_email, email, address, phone_number, encoded_password), new StudentID(new DepartmentID(100), 2024, 1));
        } else if (role == 2) {
            user = new Lecturer(new UserInformation(first_name, last_name, university_email, email, address, phone_number, encoded_password));
        } else if (role == 3) {
            user = new Advisor(new UserInformation(first_name, last_name, university_email, email, address, phone_number, encoded_password));
        } else {
            System.out.println("Invalid role");
            return false;
        }

        _users.add(user);

        //saveUsersToJson();

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
                return true;
            }
        }
        return false;
    }
    public ArrayList<Student> loadStudentsFromFile() { // read all students from the file
        String filePath = "students.json";
        Gson gson = new Gson();
        Type studentListType = new TypeToken<ArrayList<Student>>() {
        }.getType();

        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, studentListType);  // Read existing list of students
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    public ArrayList<Lecturer> loadLecturersFromFile() { // read all lecturers from the file
        String filePath = "lecturers.json";
        Gson gson = new Gson();
        Type lecturerListType = new TypeToken<ArrayList<Lecturer>>() {
        }.getType();

        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, lecturerListType);  // Read existing list of lecturers
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    public ArrayList<Advisor> loadAdvisorsFromFile() { // read all advisors from the file
        String filePath = "advisors.json";
        Gson gson = new Gson();
        Type advisorListType = new TypeToken<ArrayList<Advisor>>() {
        }.getType();

        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, advisorListType);  // Read existing list of advisors
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    public ArrayList<Department> loadDepartmentsFromFile() { // read all departments from the file
        String filePath = "departments.json";
        Gson gson = new Gson();
        Type departmentListType = new TypeToken<ArrayList<Department>>() {
        }.getType();

        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, departmentListType);  // Read existing list of departments
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    public ArrayList<Faculty> loadFacultiesFromFile() { // read all faculties from the file
        String filePath = "faculties.json";
        Gson gson = new Gson();
        Type facultyListType = new TypeToken<ArrayList<Faculty>>() {
        }.getType();

        try (FileReader reader = new FileReader(filePath)) {
            return gson.fromJson(reader, facultyListType);  // Read existing list of faculties
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

/*
    private void saveUsersToJson() {
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            File file = new File("src/main/resources/database/data.json");
            ArrayList<User> existingUsers = new ArrayList<>();

            // Check if the file exists and is not empty
            if (file.exists() && file.length() != 0) {

                JavaType type = objectMapper.getTypeFactory().constructCollectionType(ArrayList.class, User.class);
                existingUsers = objectMapper.readValue(file, type);

            }

            // Add new users to the existing users list
            existingUsers.addAll(_users);

            // Write the updated users list back to the file
            objectMapper.writerWithDefaultPrettyPrinter().writeValue(file, existingUsers);
            System.out.println("User data saved to data.json.");
        } catch (IOException e) {
            System.err.println("An error occurred while saving user data: " + e.getMessage());
        }
    }*/
//    private void getFromFile(){
//
//    }
}