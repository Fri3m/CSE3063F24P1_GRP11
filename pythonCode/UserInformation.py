import logging

from pythonCode.Logger import setup_logger
logger = setup_logger("UserInformation")
class UserInformation:
    def __init__(self, first_name, last_name, encoded_password, university_email, email, address, phone_number):
        logging.getLogger().handlers.clear()
        logger.info(f"{self.__class__.__name__} classes created.")
        self._FIRST_NAME = first_name
        self._LAST_NAME = last_name
        self._encoded_password = encoded_password
        self._UNIVERSITY_EMAIL = university_email
        self._email = email
        self._address = address
        self._phone_number = phone_number
        # I didn't write main method we didn't need it

    @staticmethod
    def from_dict(data):
        return UserInformation(data["_FIRST_NAME"], data[
            "_LAST_NAME"], data["_encoded_password"], data["_UNIVERSITY_EMAIL"], data["_email"], data["_address"], data[
                            "_phone_number"])

    def _verifyPassword(self, encoded_password):
        logger.info("Verify password method in the UserInformation class is called.")
        return self._encoded_password == encoded_password

    def changePassword(self, current_encoded_password, new_encoded_password):
        logger.info("Change password method in the UserInformation class is called.")
        if self._verifyPassword(current_encoded_password):
            self._encoded_password = new_encoded_password
            return True
        return False

    def changeEmail(self, current_encoded_password, new_email):
        logger.info("Change email method in the UserInformation class is called.")
        if self._verifyPassword(current_encoded_password):
            self._email = new_email
            return True
        return False

    def changeAddress(self, current_encoded_password, new_address):
        logger.info("Change address method in the UserInformation class is called.")
        if self._verifyPassword(current_encoded_password):
            self._address = new_address
            return True
        return False

    def changePhoneNumber(self, current_encoded_password, new_phone_number):
        logger.info("Change phone number method in the UserInformation class is called.")
        if self._verifyPassword(current_encoded_password):
            self._phone_number = new_phone_number
            return True
        return False

    def get_FIRST_NAME(self):
        logger.info("Get first name method in the UserInformation class is called.")
        return self._FIRST_NAME

    def get_LAST_NAME(self):
        logger.info("Get last name method in the UserInformation class is called.")
        return self._LAST_NAME

    def get_UNIVERSITY_EMAIL(self):
        logger.info("Get university email method in the UserInformation class is called.")
        return self._UNIVERSITY_EMAIL

    def get_encoded_password(self):
        logger.info("Get encoded password method in the UserInformation class is called.")
        return self._encoded_password

    def get_email(self):
        logger.info("Get email method in the UserInformation class is called.")
        return self._email

    def get_address(self):
        logger.info("Get address method in the UserInformation class is called.")
        return self._address

    def get_phone_number(self):
        logger.info("Get phone number method in the UserInformation class is called.")
        return self._phone_number
