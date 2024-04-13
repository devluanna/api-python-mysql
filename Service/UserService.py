from abc import ABC, abstractmethod


class UserService(ABC):
    @abstractmethod
    def create_user(self, username, email, first_name, last_name, password_user):
        pass
