import sqlite3
import atexit


class Database:
    def __init__(self):
        self.db_conn = sqlite3.connect('bank_data.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT,
                balance REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                transaction_type TEXT,
                amount REAL,
                current_balance REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.db_conn.commit()

    def load_user_accounts(self):
        user_accounts = {}
        cursor = self.db_conn.cursor()
        cursor.execute('SELECT * FROM users')
        for row in cursor.fetchall():
            username, password, balance = row
            user_accounts[username] = {'password': password, 'balance': balance}
        return user_accounts

    def save_user_accounts(self, user_accounts):
        cursor = self.db_conn.cursor()
        cursor.execute('DELETE FROM users')
        for username, account_info in user_accounts.items():
            cursor.execute('INSERT INTO users VALUES (?, ?, ?)',
                           (username, account_info['password'], account_info['balance']))
        self.db_conn.commit()

    def log_transaction(self, username, transaction_type, amount, balance):
        cursor = self.db_conn.cursor()
        cursor.execute('INSERT INTO transactions (username, transaction_type, amount, balance) VALUES (?, ?, ?, ?)',
                       (username, transaction_type, amount, balance))
        self.db_conn.commit()

    def view_transactions(self, username):
        transactions = []
        self.cursor.execute(
            'SELECT timestamp, transaction_type, amount, current_balance FROM transactions WHERE username = ? ORDER BY timestamp DESC',
            (username,))
        for row in self.cursor.fetchall():
            transactions.append(row)
        return transactions

    def close_connection(self):
        self.db_conn.close()


atexit.register(Database().close_connection)
