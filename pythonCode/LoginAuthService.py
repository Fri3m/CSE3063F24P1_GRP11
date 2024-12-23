import hashlib
import re
import logging

from pythonCode.Logger import setup_logger
logger = setup_logger("LoginAuthService")


class LoginAuthService:
    def __init__(self):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._users = []

    def login(self, email, password):
        logger.info(f"The login method in the {self.__class__.__name__} class is called.")
        logger.info("Login method checking user credentials.")
        #password = self.hashPassword(password)
        
        for user in self._users:
            user_info = user.getUserInformation()

            if user_info.get_UNIVERSITY_EMAIL() == email:
                if user_info.get_encoded_password() == password:

                    return user
                else:

                    return None


        return None

    def hashPassword(self, password):
        logger.info("Hashing password.")
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()

        return hashed_password

    def validateEmail(self, email):
        logger.info("Validating email.")
        regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        is_valid = bool(re.match(regex, email))


    def isEmailRegistered(self, university_email):
        logger.info("Checking if email is registered.")
        for user in self._users:
            if user.get_user_information().get_university_email() == university_email:

                return True


        return False
