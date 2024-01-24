from tkinter import *


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

        self.login_button = Button(text="Login", command=lambda:[self.save_info(), self.extra_func()])
        self.login_button.grid(row=3, column=1)


    def save_info(self):

        self.username = self.username_entry.get()
        print(self.username)


    def extra_func(self):
        self.password = self.password_entry.get()
        print(self.password)

