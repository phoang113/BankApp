from bank_menu import BankMenu
from accounts import Account
from user import User

# Initialize class
bank_menu = BankMenu()
user = User()
accounts = Account()

# Turn on the machine
is_on = True

# While the machine is on
def logged_in(current_account):
    user_logged_in = True

    while user_logged_in:
        bank_menu.print_menu_user()
        user_choice = input("Please make your selection: ")
        if user_choice == '5':
            print("\n")
            user_logged_in = False


while is_on:
    # Prints the starting menu
    bank_menu.print_menu_start()

    # Ask user to pick a choice
    choice = input("Please provide your selection: ")

    # If user wants to turn off the app
    if choice == '3':
        is_on = False
    # If user wants to sign up for a new account
    elif choice == '2':
        # First ask for a username then check if username already exists in the database
        username = input("Please enter a username: ")
        if accounts.check_user(username):
            print("Username already taken, please provide another username!\n")
        else:
            accounts.add_user(username)
    # If user wants to sign in to an existing account
    elif choice == '1':
        username = input("Please enter a username: ")
        if accounts.account_exist(username):
            current_account = accounts.return_user(username)
            # Make sure to login
            if accounts.login(current_account):
                logged_in(current_account)
        else:
            print("Username does not exist!\n")
    else:
        print("Invalid choice.\n")
