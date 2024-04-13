from Repository.UserRepository import UserRepository
from Service.UserService import UserService

import random


class UserServiceImpl(UserService):
    def __init__(self):
        self.user_repository = UserRepository()

    @staticmethod
    def generate_id():
        caracts = '0123456789'
        identity = ""
        length = 6

        for i in range(length):
            identity += random.choice(caracts)

        return identity

    def create_user(self, username, email, first_name, last_name, password_user):
        identity_value = self.generate_id()

        create_success = self.user_repository.create_user(username, email, first_name, last_name,
                                                          password_user, identity_value)

        return create_success
