package src;

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

    //new constructor
    public UserInformation(String first_name, String last_name, String university_email, String email, String address, String phone_number, String encoded_password) {
        this._FIRST_NAME = first_name;
        this._LAST_NAME = last_name;
        this._UNIVERSITY_EMAIL = university_email;
        this._email = email;
        this._address = address;
        this._phone_number = phone_number;
        this._encoded_password = encoded_password;
    }
    //new constructors can be created

    boolean changePassword(String encoded_password, String new_encoded_password) {

        return true;
    }
    boolean changeEmail(String encoded_password,String email) {
        return true;
    }
    boolean changeAddress(String encoded_password,String address) {
        return true;
    }
    boolean changePhoneNumber(String encoded_password,String phone_number) {
        return true;
    }

    //needed getters and setters

    public String get_UNIVERSITY_EMAIL() {
        return _UNIVERSITY_EMAIL;
    }

    public String get_encoded_password() {
        return _encoded_password;
    }
}