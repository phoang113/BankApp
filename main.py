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
        bank_menu.print_menu_user(current_account)
        user_choice = input("Please make your selection: ")
        if user_choice == '6':
            print("\n")
            accounts.save()
            user_logged_in = False
        elif user_choice == '5':
            print(current_account)
        elif user_choice == '2':
            amount = float(input("Please enter the amount you want to deposit: "))
            accounts.deposit(current_account, amount)
        elif user_choice == '3':
            amount = float(input("Please enter the amount you want to withdraw:  "))
            accounts.withdraw(current_account, amount)
        elif user_choice == '1':
            accounts.view_balance(current_account)
        elif user_choice == '4':
            bank_menu.print_user_change()
            change_info(current_account)
        else:
            print("Invalid choice. ")
            print("\n")

def change_info(account):
    choice = input("Please make a selection: ")
    key = ""
    new = ""
    if choice == '1':
        new = input("What is the new password?: ")
        key = "password"
    elif choice == '2':
        new = input("What is the new first name?: ")
        key = 'first'
    elif choice == '3':
        new = input("What is the new last name?: ")
        key = 'last'
    elif choice == '4':
        new = input("What is the new email?: ")
        key = 'email'
    else:
        print("Invalid input.\n")
    if key != "":
        accounts.update(account, key, new)


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
