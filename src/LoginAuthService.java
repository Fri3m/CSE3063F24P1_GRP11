package src;



import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class LoginAuthService {

    public ArrayList<User> _users = new ArrayList<>();

    public LoginAuthService() {
    }


    public User login(String email,String password) {
        password = hashPassword(password);

        for (User user : _users) {
            if (user.getUserInformation().get_UNIVERSITY_EMAIL().equals(email)) {
                if (user.getUserInformation().get_encoded_password().equals(password)) {
                    return user;
                } else {
                    return null;
                }
            }
        }

        return null;
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
}