# Bank Menu class

class BankMenu:
    def __init__(self):
        pass

    # Function to print the menu at the beginning
    def print_menu_start(self):
        print("Welcome!")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")

    def print_menu_user(self, user):
        print(f"Welcome {user['username']}")
        print("What would you like to do today?")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change Information")
        print("5. View Information")
        print("6. Sign Out")

    def print_user_change(self):
        print("\n")
        print("What information would you like to change?")
        print("1. Password")
        print("2. First Name")
        print("3. Last Name")
        print("4. Email")
        print("5. Back")