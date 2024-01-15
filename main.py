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
while is_on:
    # Prints the starting menu
    bank_menu.print_menu_start()

    choice = input("Please provide your selection: ")

    if choice == '3':
        is_on = False
    elif choice == '2':
        username = input("Please enter a username: ")
        if accounts.check_user(username):
            print("Username already taken, please provide another username!\n")
        else:
            accounts.add_user(username)

