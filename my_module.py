# my_module.py

import re
import string
from datetime import datetime
import atexit
from database import Database
from random import random

# Define regex patterns for username and password
username_pattern = r"^[a-zA-Z0-9_]{3,20}$"
password_pattern = r"^[a-zA-Z0-9_]{6}$"


def is_valid_username(username):
    return re.match(username_pattern, username)


def is_valid_password(password):
    return re.match(password_pattern, password)


def load_user_accounts():
    db = Database()
    return db.load_user_accounts()


def save_user_accounts(user_accounts):
    db = Database()
    db.save_user_accounts(user_accounts)


def create_account(user_accounts, username, initial_balance, password):
    user_accounts[username] = {'balance': initial_balance, 'password': password}
    save_user_accounts(user_accounts)


def deposit(user_accounts, username, amount):
    user_accounts[username]['balance'] += amount
    save_user_accounts(user_accounts)


def withdraw(user_accounts, username, amount):
    user_balance = user_accounts[username]['balance']
    if user_balance >= amount:
        user_accounts[username]['balance'] -= amount
        save_user_accounts(user_accounts)
    else:
        raise ValueError("Insufficient funds")


def log_transaction(username, transaction_type, amount, balance):
    db = Database()
    db.log_transaction(username, transaction_type, amount, balance)


def view_transactions(username):
    db = Database()
    return db.view_transactions(username)


def generate_random_password(length=12):
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


# At the end of the file
atexit.register(Database().close_connection)
