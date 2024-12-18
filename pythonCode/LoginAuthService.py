import hashlib
import re

class UserInformation:
    def __init__(self, university_email, encoded_password):
        self._university_email = university_email
        self._encoded_password = encoded_password

    def get_university_email(self):
        return self._university_email

    def get_encoded_password(self):
        return self._encoded_password


class User:
    def __init__(self, user_information):
        self._user_information = user_information

    def get_user_information(self):
        return self._user_information


class LoginAuthService:
    def __init__(self):
        self._users = []

    def login(self, email, password):
        password = self.hash_password(password)

        # Check if the email and password match any user
        for user in self._users:
            user_info = user.get_user_information()
            if user_info.get_UNIVERSITY_EMAIL() == email:
                if user_info.get_encoded_password() == password:
                    return user
                else:
                    return None
        return None

    def hash_password(password):
        hash_object = hashlib.sha256(password.encode())
        return hash_object.hexdigest()

    def validate_email(email):
        # Validate email using a regex
        regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.match(regex, email))

    def isEmailRegistered(self, university_email):
        # Check if an email is already registered
        for user in self._users:
            if user.get_user_information().get_UNIVERSITY_EMAIL() == university_email:
                return True
        return False
