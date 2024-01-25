from tkinter import *
from accounts import Account
from tkinter import messagebox

# GUI class
class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Bank App")
        self.window.config(padx=100, pady=100, bg="white")

        self.username = ""
        self.password = ""

        # Welcome Title
        self.welcome_label = Label(text="Welcome")
        self.welcome_label.grid(row=0, column=1)

        # Buttons
        self.sign_in_button = Button(text="Sign In", command=self.sign_in)
        self.sign_in_button.grid(row=1, column=1)

        self.sign_up_button = Button(text="Sign Up")
        self.sign_up_button.grid(row=2, column=1)

        self.clear_button = Button(text="Clear", command=self.clear)
        self.clear_button.grid(row=3, column=1)

        # Labels
        self.username_label = Label(text="Username")
        self.password_label = Label(text="Password")

        # Entries
        self.username_entry = Entry(width=25)
        self.password_entry = Entry(width=25)



        # Accounts class
        self.account = Account()


    def open_gui(self):
        self.window.mainloop()

    def clear(self):
        for widget in self.window.winfo_children():
            widget.destroy()



    def sign_in(self):
        self.clear()
        # Labels

        self.username_label = Label(text="Username")
        self.password_label = Label(text="Password")

        # Entries
        self.username_entry = Entry(width=25)
        self.password_entry = Entry(width=25)
        self.username_label.grid(row=1, column=0)
        self.password_label.grid(row=2, column=0)
        self.username_entry.grid(row=1, column=1)
        self.password_entry.grid(row=2, column=1)

        self.login_button = Button(text="Login", command=lambda:[self.save_info(), self.check_info()])
        self.login_button.grid(row=3, column=1)


    def save_info(self):

        self.username = self.username_entry.get()
        self.password = self.password_entry.get()


    def check_info(self):
        if self.account.check_user(self.username):
            self.current_account = self.account.return_user(self.username)

        else:
            messagebox.showerror(title="Error", message="Account does not exist!")

        if self.account.updated_login(self.current_account, self.password):
            self.user_main()
        else:
            messagebox.showerror(title="Error", message="Account/Password combination incorrect!")



    def user_main(self):
        self.clear()
        self.current_account = self.account.return_user(self.username)
        self.username_text = self.account.return_username(self.current_account)
        self.user_label = Label(text=self.username_text)

        self.user_balance_text = self.account.return_balace(self.current_account)
        self.user_balance_label = Label(text=self.user_balance_text)

        self.user_label.grid(row=1, column=1)
        self.user_balance_label.grid(row=1, column=2)

        self.withdraw_button = Button(text="Withdraw")
        self.deposit_button = Button(text="Deposit")
        self.deposit_button.grid(row=2, column=1)
        self.withdraw_button.grid(row=2, column=2)



