package src;
import java.util.Scanner;

public class UserInformation {

    private final String _FIRST_NAME;
    private final String _LAST_NAME;
    private String _encoded_password; // use sha256
    private final String _UNIVERSITY_EMAIL;
    private String _email;
    private String _address;
    private String _phone_number;

    public UserInformation(String first_name, String last_name, String university_email) {
        this._FIRST_NAME = first_name;
        this._LAST_NAME = last_name;
        this._UNIVERSITY_EMAIL = university_email;
    }

    // New constructor
    public UserInformation(String first_name, String last_name, String university_email, String email, String address, String phone_number, String encoded_password) {
        this._FIRST_NAME = first_name;
        this._LAST_NAME = last_name;
        this._UNIVERSITY_EMAIL = university_email;
        this._email = email;
        this._address = address;
        this._phone_number = phone_number;
        this._encoded_password = encoded_password;
    }

    public static void main(String[] args) {
        // Example password encoding for initial password setup
        String initialPassword = "password123";
        String encodedPassword = LoginAuthService.hashPassword(initialPassword);

        // Create a sample user with some initial data
        UserInformation user = new UserInformation(
                "John", "Doe", "john.doe@marun.edu.tr",
                "john.doe@example.com", "123 Main St", "555-1234", encodedPassword
        );

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- User Information System ---");
            System.out.println("1. Change Password");
            System.out.println("2. Change Email");
            System.out.println("3. Change Address");
            System.out.println("4. Change Phone Number");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            if (choice == 1) {
                System.out.print("Enter current password: ");
                String currentPassword = scanner.nextLine();
                System.out.print("Enter new password: ");
                String newPassword = scanner.nextLine();
                String encodedNewPassword = LoginAuthService.hashPassword(newPassword);

                if (user.changePassword(LoginAuthService.hashPassword(currentPassword), encodedNewPassword)) {
                    System.out.println("Password updated successfully.");
                } else {
                    System.out.println("Incorrect password. Password not updated.");
                }

            } else if (choice == 2) {
                System.out.print("Enter current password: ");
                String currentPassword = scanner.nextLine();
                System.out.print("Enter new email: ");
                String newEmail = scanner.nextLine();

                if (user.changeEmail(LoginAuthService.hashPassword(currentPassword), newEmail)) {
                    System.out.println("Email updated successfully to " + user.get_email());
                } else {
                    System.out.println("Incorrect password. Email not updated.");
                }

            } else if (choice == 3) {
                System.out.print("Enter current password: ");
                String currentPassword = scanner.nextLine();
                System.out.print("Enter new address: ");
                String newAddress = scanner.nextLine();

                if (user.changeAddress(LoginAuthService.hashPassword(currentPassword), newAddress)) {
                    System.out.println("Address updated successfully to " + user.get_address());
                } else {
                    System.out.println("Incorrect password. Address not updated.");
                }

            } else if (choice == 4) {
                System.out.print("Enter current password: ");
                String currentPassword = scanner.nextLine();
                System.out.print("Enter new phone number: ");
                String newPhoneNumber = scanner.nextLine();

                if (user.changePhoneNumber(LoginAuthService.hashPassword(currentPassword), newPhoneNumber)) {
                    System.out.println("Phone number updated successfully to " + user.get_phone_number());
                } else {
                    System.out.println("Incorrect password. Phone number not updated.");
                }

            } else if (choice == 5) {
                System.out.println("Exiting the program.");
                break;
            } else {
                System.out.println("Invalid option. Please try again.");
            }
        }

        scanner.close();
    }
    private boolean verifyPassword(String encoded_password) {
        return this._encoded_password.equals(encoded_password);
    }


    public boolean changePassword(String current_encoded_password, String new_encoded_password) {
        if (verifyPassword(current_encoded_password)) {
            this._encoded_password = new_encoded_password;
            return true;
        }
        return false;
    }


    public boolean changeEmail(String current_encoded_password, String new_email) {
        if (verifyPassword(current_encoded_password)) {
            this._email = new_email;
            return true;
        }
        return false;
    }


    public boolean changeAddress(String current_encoded_password, String new_address) {
        if (verifyPassword(current_encoded_password)) {
            this._address = new_address;
            return true;
        }
        return false;
    }


    public boolean changePhoneNumber(String current_encoded_password, String new_phone_number) {
        if (verifyPassword(current_encoded_password)) {
            this._phone_number = new_phone_number;
            return true;
        }
        return false;
    }

    public String get_FIRST_NAME() {
        return _FIRST_NAME;
    }

    public String get_LAST_NAME() {
        return _LAST_NAME;
    }

    public String get_UNIVERSITY_EMAIL() {
        return _UNIVERSITY_EMAIL;
    }

    public String get_encoded_password() {
        return _encoded_password;
    }

    public String get_email() {
        return _email;
    }

    public String get_address() {
        return _address;
    }

    public String get_phone_number() {
        return _phone_number;
    }


}
