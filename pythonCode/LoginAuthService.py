import hashlib
import re



class LoginAuthService:
    def __init__(self):

        self._users = []

    def login(self, email, password):

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

        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()

        return hashed_password

    def validateEmail(self, email):

        regex = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        is_valid = bool(re.match(regex, email))


    def isEmailRegistered(self, university_email):

        for user in self._users:
            if user.get_user_information().get_university_email() == university_email:

                return True


        return False
