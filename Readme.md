# `Thee Best Bank - Python Banking Application`

## **`Overview`**
Thee Best Bank is a simple banking application written in Python using the Tkinter library for the GUI. It allows users to create accounts, log in, perform transactions (deposit/withdraw), view transaction history, and reset passwords.

## **`Dependencies`**
- Tkinter
- SQLite

## **`Installation`**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository```

## **`Usage`**
### 1. Account Creation
- Launch the application.
- Select "New Account" from the main menu.
- Fill in the required information:
  - Username: Follow the specified criteria.
  - Password: Follow the specified criteria or generate one.
  - Childhood Hero: Enter the name of your childhood hero.
  - Initial Balance: Enter the initial balance for the new account.
- Click "Create Account" to complete the process.
- You can also choose to generate a password automatically.

### 2. Login
- Launch the application.
- Select "Login" from the main menu.
- Enter your username and password.
- Click "Login" to access your account.

### 3. Forgot Password
- If you forget your password, click on "Forgot Password" during the login process.
- Enter your account username.
- Provide the name of your childhood hero for verification.
- Set a new password when prompted.

### 4. Transactions
#### 4.1. Deposit
- Log in to your account.
- Click on the "Deposit" button.
- Enter the amount you want to deposit (must be in multiples of 10).
- Confirm the transaction.

#### 4.2. Withdraw
- Log in to your account.
- Click on the "Withdraw" button.
- Enter the amount you want to withdraw (must be in multiples of 10).
- Confirm the transaction, ensuring sufficient funds.

#### 4.3. View Transactions
- Log in to your account.
- Click on the "Statement" button.
- View a detailed list of your transactions, including timestamps.

### 5. Changing Password
- Log in to your account.
- Navigate to the "Forgot Password" section if you want to change your password.
- Follow the steps provided to set a new password.

### 6. Exiting the Application
- Click on "Exit" from any menu to close the application.

## **`File Structure`**
- `main.py` : Main applicaton file
- `my_module.py` : Module for user-related functions
- `database.py` : Database module for SQLite operations

## **Contributing**
- Contributions are welcome! If you find any bugs or have ideas for improvements, feel free to open an issue or submit a pull request.

## **`Aknowledgements`**
- Thanks to the **`Tkinter`** and **`SQLite`** developers for providing the tools used in this project

## **`License`**
- This project is licensed under the MIT License.