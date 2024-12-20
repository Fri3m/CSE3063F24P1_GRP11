class UserInformation:
    def __init__(self, first_name = "", last_name = "", encoded_password = "", university_email= "", email= "", address= "", phone_number= ""):
        self._FIRST_NAME = first_name
        self._LAST_NAME = last_name
        self._encoded_password = encoded_password
        self._UNIVERSITY_EMAIL = university_email
        self._email = email
        self._address = address
        self._phone_number = phone_number

        # I didnt write main method we didint need it

    def _verifyPassword(self, encoded_password):
        return self._encoded_password == encoded_password

    def changePassword(self, current_encoded_password, new_encoded_password):
        if self.verifyPassword(current_encoded_password):
            self._encoded_password = new_encoded_password
            return True
        return False

    def changeEmail(self, current_encoded_password, new_email):
        if self.verifyPassword(current_encoded_password):
            self._email = new_email
            return True
        return False

    def changeAddress(self, current_encoded_password, new_address):
        if self.verifyPassword(current_encoded_password):
            self._address = new_address
            return True
        return False

    def changePhoneNumber(self, current_encoded_password, new_phone_number):
        if self.verifyPassword(current_encoded_password):
            self._phone_number = new_phone_number
            return True
        return False

    def verifyPassword(self, encoded_password):
        return self._encoded_password == encoded_password

    def get_FIRST_NAME(self):
        return self._FIRST_NAME

    def get_LAST_NAME(self):
        return self._LAST_NAME

    def get_UNIVERSITY_EMAIL(self):
        return self._UNIVERSITY_EMAIL

    def get_encoded_password(self):
        return self._encoded_password

    def get_email(self):
        return self._email

    def get_address(self):
        return self._address

    def get_phone_number(self):
        return self._phone_number
