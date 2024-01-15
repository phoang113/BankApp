# Class accounts that will eventually read in a file to access prior accounts
from user import User

user = User()

class Account:
    def __init__(self):
        self.account_list = []

    # Function that checks if username already exists
    def check_user(self, username):
        for user in self.account_list:
            if user['username'] == username:
                return True

        # In the case the username is available
        return False

    def add_user(self, username):
        new_user = user.create_new_user(username)
        self.account_list.append(new_user)