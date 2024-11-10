package src;

public class UserInformation {
    private String _first_name;
    private String _last_name;
    private String _encoded_password; // use sha256
    private final String _UNIVERSITY_EMAIL;
    private String _email;
    private String _address;
    private String _phone_number;

    public UserInformation(String first_name, String last_name, String university_email) {
        this._first_name = first_name;
        this._last_name = last_name;
        this._UNIVERSITY_EMAIL = university_email;
    }

    boolean changePassword(String encoded_password, String new_encoded_password) {
        return true;
    }


    //needed getters and setters
}