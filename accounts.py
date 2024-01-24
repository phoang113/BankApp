# Class accounts that will eventually read in a file to access prior accounts
from user import User
import json

user = User()


class Account:
    def __init__(self):
        self.account_list = []

        # Reads in file to get account information
        f = open("account_file.json", "r")
        self.account_list = json.loads(f.read())
        f.close()

    # Function that checks if username already exists
    def check_user(self, username):
        for user in self.account_list:
            if user['username'] == username:
                return True

        # In the case the username is available
        return False

    # Function to create a new dictionary of a new account
    def add_user(self, username):
        new_user = user.create_new_user(username)
        self.account_list.append(new_user)

    # Function to first check if the username exist in the list
    def account_exist(self, username):
        for users in self.account_list:
            if users['username'] == username:
                return True
        return False

    # Function to return the dictionary of the current account
    def return_user(self, username):
        for account in self.account_list:
            if account['username'] == username:
                return account

    # Function to keep asking for user's password until it is correct
    def login(self, user):
        password = ""
        while (password != user['password']):
            password = input("Please enter your password: ")

        return True

    # Function to deposit money into the account
    def deposit(self, user, amount):
        user['balance'] += amount

    # Function to withdraw money from the account, assuming they have enough
    def withdraw(self, user, amount):
        if user['balance'] >= amount:
            user['balance'] -= amount
        else:
            print("Sorry, not enough money to withdraw\n")

    # Function to view the user's current balance
    def view_balance(self, user):
        print("${:.2f}".format(user['balance']))
        print("\n")

    # Function to update the user information
    def update(self, user, key, new_info):
        user[key] = new_info

    # Function to save all the accounts created in the session for the future
    def save(self):
        output_file = open("account_file.json", "w")

        json.dump(self.account_list, output_file)

        output_file.close()

    # For testers, just to print current usernames saved
    def print_usernames(self):
        for username in self.account_list:
            print(username['username'])
