import hashlib
import re

class UserInformation:
    def __init__(self, university_email, encoded_password):
        print(f"Creating UserInformation for email: {university_email}")
        self._university_email = university_email
        self._encoded_password = encoded_password

    def get_university_email(self):
        print(f"Getting university email: {self._university_email}")
        return self._university_email

    def get_encoded_password(self):
        print(f"Getting encoded password for email: {self._university_email}")
        return self._encoded_password


class User:
    def __init__(self, user_information):
        print(f"Creating User with email: {user_information.get_university_email()}")
        self._user_information = user_information

    def get_user_information(self):
        print("Getting user information")
        return self._user_information


class LoginAuthService:
    def __init__(self):
        print("Initializing LoginAuthService")
        self._users = []

    def login(self, email, password):
        print(f"Trying to log in with email: {email}")
        password = self.hashPassword(password)
        
        for user in self._users:
            user_info = user.get_user_information()
            print(f"Checking email: {user_info.get_university_email()}")
            if user_info.get_university_email() == email:
                if user_info.get_encoded_password() == password:
                    print(f"Login successful for email: {email}")
                    return user
                else:
                    print(f"Password mismatch for email: {email}")
                    return None

        print(f"No user found with email: {email}")
        return None

    def hashPassword(self, password):
        print("Hashing password")
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()
        print("Password hashed successfully")
        return hashed_password

    def validateEmail(self, email):
        print(f"Validating email: {email}")
        regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        is_valid = bool(re.match(regex, email))
        if is_valid:
            print(f"Email is valid: {email}")
        else:
            print(f"Email is invalid: {email}")
        return is_valid

    def isEmailRegistered(self, university_email):
        print(f"Checking if email is registered: {university_email}")
        for user in self._users:
            if user.get_user_information().get_university_email() == university_email:
                print(f"Email is already registered: {university_email}")
                return True

        print(f"Email is not registered: {university_email}")
        return False
