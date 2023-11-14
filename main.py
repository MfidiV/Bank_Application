import datetime
import random
import string
import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk

from database import Database
from my_module import load_user_accounts,is_valid_username, is_valid_password, create_account, deposit, withdraw, \
    view_transactions


class BankApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Thee Best Bank")
        # Set the window size and center it
        self.button_width = 20
        self.button_height = 2
        self.custom_font = ("Helvetica", 14)
        self.db = Database
        # Initialize user_accounts dictionary
        self.user_accounts = load_user_accounts()

        # Load and set the logo
        self.logo_path = "Bank Best.png"  # Assuming the image is in the root directory
        try:
            self.logo = PhotoImage(file=self.logo_path)
            self.root.iconphoto(False, self.logo)
        except Exception as e:
            print(f"Error loading image: {e}")

        self.main_menu()  # Call the main_menu method

    def main_menu(self):
        window_width = 800
        window_height = 600

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # GUI components
        self.main_frame = tk.Frame(self.root, bg='#ADD8E6')  # Set the background color to #ADD8E6
        self.main_frame.pack()

        label = tk.Label(self.main_frame, text="Welcome to Thee Best Bank", font=self.custom_font)
        label.grid(row=0, column=0, columnspan=3, pady=20, sticky='n')

        # Load and set the logo
        logo_label = tk.Label(self.main_frame, image=self.logo, bg='#ADD8E6')
        logo_label.grid(row=1, column=0, rowspan=3, padx=10, pady=10)

        # Style for buttons
        style = ttk.Style()
        style.configure("TButton", padding=10, relief="flat", font=self.custom_font)

        # New Account Button
        new_account_btn = ttk.Button(self.main_frame, text="New Account", command=self.new_account)
        new_account_btn.grid(row=1, column=1, columnspan=2, pady=(10))

        # Login Button
        login_btn = ttk.Button(self.main_frame, text="Login", command=self.login)
        login_btn.grid(row=2, column=1, columnspan=2, pady=10, padx=20)

        # Exit Button
        exit_btn = ttk.Button(self.main_frame, text="Exit", command=self.root.destroy)
        exit_btn.grid(row=3, column=1, columnspan=2, pady=(10, 5))

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def go_to_main_menu(self):
        self.clear_frame()
        self.root.destroy()  # Destroy the current root window

        # Recreate and run the BankApp instance
        app = BankApp()
        app.run()

    def generate_random_password(self, length=12):
        # Define the characters that can be used in the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Ensure that the password contains at least one of each category
        lowercase_letter = random.choice(string.ascii_lowercase)
        uppercase_letter = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        symbol = random.choice(string.punctuation)

        # Combine all characters
        all_chars = characters + lowercase_letter + uppercase_letter + digit + symbol

        # Generate the remaining characters randomly
        remaining_length = length - 4  # 4 characters are fixed as per the categories
        password = ''.join(random.choice(all_chars) for _ in range(remaining_length))

        # Shuffle the password characters to make it more random
        password = ''.join(random.sample(password, len(password)))

        return lowercase_letter + uppercase_letter + digit + symbol + password

    def generate_password(self, password_entry):
        if self.generate_password_var.get():
            # Generate and insert password if checkbox is selected
            generated_password = self.generate_random_password()
            password_entry.delete(0, tk.END)  # Clear the current content
            password_entry.insert(0, generated_password)  # Insert the new password

    def new_account(self):
        self.clear_frame()

        # Labels and Entry widgets
        tk.Label(self.main_frame, text="Username:", font=self.custom_font).grid(row=0, column=0, pady=10)
        username_entry = tk.Entry(self.main_frame, font=self.custom_font)
        username_entry.grid(row=0, column=1, pady=10)

        tk.Label(self.main_frame, text="Password:", font=self.custom_font).grid(row=1, column=0, pady=10)
        password_entry = tk.Entry(self.main_frame, font=self.custom_font)
        password_entry.grid(row=1, column=1, pady=10, padx=20)

        # Checkbox to generate password
        self.generate_password_var = tk.BooleanVar()
        generate_password_checkbox = tk.Checkbutton(self.main_frame, text="Generate Password",
                                                    variable=self.generate_password_var, font=self.custom_font,
                                                    command=lambda: self.generate_password(password_entry))
        generate_password_checkbox.grid(row=2, column=0, columnspan=2, pady=5, padx=20)

        tk.Label(self.main_frame, text="Enter initial balance:", font=self.custom_font).grid(row=3, column=0, pady=10)
        balance_entry = tk.Entry(self.main_frame, font=self.custom_font)
        balance_entry.grid(row=3, column=1, pady=10, padx=20)

        # Buttons
        create_account_btn = tk.Button(self.main_frame, text="Create Account",
                                       command=lambda: self.process_new_account(
                                           username_entry.get(), password_entry.get(), balance_entry.get()),
                                       font=self.custom_font)
        create_account_btn.grid(row=4, column=0, columnspan=2, pady=20)

        # Back button
        ttk.Button(self.main_frame, text="Back", command=self.go_to_main_menu).grid(row=5, column=0, columnspan=2,
                                                                                    pady=10)

        # back_to_menu_btn = tk.Button(self.main_frame, text="Back to Main Menu", command=lambda: self.main_menu()).pack(pady=10)
        # back_to_menu_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def process_new_account(self, username, password, balance):
        try:
            balance = float(balance)
        except ValueError:
            messagebox.showerror("Error", "Invalid balance. Please enter a valid number.")
            return

        if username == "" or not is_valid_username(username):
            messagebox.showerror("Error", "Invalid username. Please follow the criteria.")
            return

        if username in self.user_accounts:
            messagebox.showerror("Error", "Username already exists. Please choose another username.")
            return

        create_account(self.user_accounts, username, balance, password)
        messagebox.showinfo("Success", f"Account created successfully for {username} with balance R{balance}")
        self.show_transaction_menu(username)  # Use main_menu to go back to the main menu

    def login(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Username:", font=self.custom_font).pack(pady=10)
        username_entry = tk.Entry(self.main_frame, font=10)
        username_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Password:", font=self.custom_font).pack()
        password_entry = tk.Entry(self.main_frame, show="*", font=10)
        password_entry.pack(pady=5)

        # Style for buttons
        style = ttk.Style()
        style.configure("TButton", padding=10, relief="flat", font=self.custom_font)

        ttk.Button(self.main_frame, text="Login", command=lambda: self.process_login(
            username_entry.get(), password_entry.get())).pack(pady=10)

        ttk.Button(self.main_frame, text="Back", command=self.go_to_main_menu).pack(pady=10)



    def process_login(self, username, password):
        if username == "" or username not in self.user_accounts or self.user_accounts[username]['password'] != password:
            messagebox.showerror("Error", "Invalid username or password. Please try again.")
            return

        self.show_transaction_menu(username)

    def show_transaction_menu(self, username):
        self.clear_frame()

        balance_label = tk.Label(self.main_frame,
                                 text=f"Current Balance for {username}: R{self.user_accounts[username]['balance']:.2f}",
                                 font=self.custom_font)
        balance_label.pack(pady=10,padx=50)

        # Style for buttons
        style = ttk.Style()
        style.configure("TButton", padding=10, relief="flat", font=self.custom_font)

        ttk.Button(self.main_frame, text="Deposit",
                   command=lambda: self.process_deposit_withdraw(username, "deposit")).pack(pady=5)
        ttk.Button(self.main_frame, text="Withdraw",
                   command=lambda: self.process_deposit_withdraw(username, "withdraw")).pack(pady=5)
        ttk.Button(self.main_frame, text="Statement", command=lambda: self.view_transactions(username)).pack(pady=5)
        ttk.Button(self.main_frame, text="Exit", command=self.root.destroy).pack(pady=5)

    def process_deposit_withdraw(self, username, transaction_type):
        self.clear_frame()

        # Display current balance
        balance_label = tk.Label(self.main_frame,
                                 text=f"Current Balance: R{self.user_accounts[username]['balance']:.2f}",
                                 font=self.custom_font)
        balance_label.pack(pady=20, padx=50)

        # Entry for entering the transaction amount
        amount_label_text = f"Enter amount to {transaction_type}: R"
        amount_label = tk.Label(self.main_frame, text=amount_label_text, font=self.custom_font)
        amount_label.pack()

        amount_entry = tk.Entry(self.main_frame, font=self.custom_font)
        amount_entry.pack(pady=5)

        # Button to perform the transaction
        action = deposit if transaction_type == "deposit" else withdraw

        transaction_button = tk.Button(self.main_frame, text=f"{transaction_type.capitalize()}",
                                       command=lambda: self.process_deposit_withdraw_action(
                                           username, action, amount_entry.get().strip().replace(" ", "")), font=self.custom_font, width=15,
                                       height=2)
        transaction_button.pack(pady=20)

        # Button to go back to the Transaction Menu
        back_to_menu_button = tk.Button(self.main_frame, text="Back",
                                        command=lambda: self.show_transaction_menu(username), font=self.custom_font,
                                        width=15, height=2, padx=20, pady=10)
        back_to_menu_button.pack()

    def process_deposit_withdraw_action(self, username, action, amount_str):
        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
            return

        if amount <= 0:
            messagebox.showerror("Error", "Amount must be positive.")
            return

        if amount % 10 != 0:
            messagebox.showerror("Error", "Deposit/Withdrawal amount must be in multiples of 10.")
            return
        if action == withdraw and amount > self.user_accounts[username]['balance']:
            messagebox.showerror("Error", "Withdrawal amount exceeds the current balance.")
            return
        action(self.user_accounts, username, amount)
        messagebox.showinfo("Success", f"Transaction completed successfully. New balance: "
                                       f"R{self.user_accounts[username]['balance']:.2f}")
        self.show_transaction_menu(username)

    def view_transactions(self, username):
        self.clear_frame()

        tk.Label(self.main_frame, text="===== TRANSACTIONS =====", font=self.custom_font).pack()

        transactions = self.db.view_transactions(username)

        if not transactions:
            tk.Label(self.main_frame, text="No transactions available.", font=self.custom_font).pack()
        else:
            for transaction_info in transactions:
                timestamp, _, transaction_type, amount, current_balance = transaction_info
                amount = float(amount)
                current_balance = float(current_balance)
                transaction_time = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime(
                    "%Y-%m-%d %H:%M:%S")

                transaction_text = f"\nTime: {transaction_time}\n{transaction_type}: R{amount:.2f}, " \
                                   f"Current Balance: R{current_balance:.2f}\n"

                tk.Label(self.main_frame, text=transaction_text, font=self.custom_font).pack(pady=5)

        tk.Label(self.main_frame, text="===== END OF TRANSACTIONS =====", font=self.custom_font).pack()

        ttk.Button(self.main_frame, text="Back to Transaction Menu",
                   command=lambda: self.show_transaction_menu(username)).pack(pady=10)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = BankApp()
    app.run()
