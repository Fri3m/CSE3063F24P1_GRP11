import hashlib
import re
import logging

class UserInformation:
    def __init__(self, university_email, encoded_password):
        logging.info(f"Creating UserInformation for email: {university_email}")
        self._university_email = university_email
        self._encoded_password = encoded_password

    def get_university_email(self):
        logging.info(f"Getting university email: {self._university_email}")
        return self._university_email

    def get_encoded_password(self):
        logging.info(f"Getting encoded password for email: {self._university_email}")
        return self._encoded_password


class User:
    def __init__(self, user_information):
        logging.info(f"Creating User with email: {user_information.get_university_email()}")
        self._user_information = user_information

    def get_user_information(self):
        logging.info("Getting user information")
        return self._user_information


class LoginAuthService:
    def __init__(self):
        logging.info("Initializing LoginAuthService")
        self._users = []

    def login(self, email, password):
        logging.info(f"Trying to log in with email: {email}")
        password = self.hashPassword(password)
        
        for user in self._users:
            user_info = user.get_user_information()
            logging.info(f"Checking email: {user_info.get_university_email()}")
            if user_info.get_university_email() == email:
                if user_info.get_encoded_password() == password:
                    logging.info(f"Login successful for email: {email}")
                    return user
                else:
                    logging.info(f"Password mismatch for email: {email}")
                    return None

        logging.info(f"No user found with email: {email}")
        return None

    def hashPassword(self, password):
        logging.info("Hashing password")
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()
        logging.info("Password hashed successfully")
        return hashed_password

    def validateEmail(self, email):
        logging.info(f"Validating email: {email}")
        regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        is_valid = bool(re.match(regex, email))
        if is_valid:
            logging.info(f"Email is valid: {email}")
        else:
            logging.info(f"Email is invalid: {email}")
        return is_valid

    def isEmailRegistered(self, university_email):
        logging.info(f"Checking if email is registered: {university_email}")
        for user in self._users:
            if user.get_user_information().get_university_email() == university_email:
                logging.info(f"Email is already registered: {university_email}")
                return True

        logging.info(f"Email is not registered: {university_email}")
        return False
