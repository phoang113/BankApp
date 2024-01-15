class User:
    def __init__(self):
        self.user = {
            "username": "",
            "password": "",
            "first": "",
            "last": "",
            "email": "",
            "balance": 0
        }

    def create_new_user(self, username):
        password = input("Please enter a password: ")
        first = input("Please enter your first name: ")
        last = input("Please enter your last name: ")
        email = input("Please enter your email address: ")
        print("\n")

        new_user = {
            "username": username,
            "password": password,
            "first": first,
            "last": last,
            "email": email,
            "balance": 0
        }

        return new_user
