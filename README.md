# 🏦 Bank Management System

A simple **Bank Management System** built with Python using Object-Oriented Programming (OOP).

The program provides a menu-driven interface for creating and managing bank accounts. Users can check balances, deposit and withdraw money, transfer money between accounts, and delete accounts.

## ✨ Features

* Create a new bank account
* View all accounts
* Check account balance
* Deposit money
* Withdraw money
* Transfer money between accounts
* Delete an account
* Exit the system
* Prevent withdrawals and transfers when the balance is insufficient

## 🧠 OOP Concepts Used

### 1. Classes and Objects

The `BankAccount` class represents a bank account.

```python
class BankAccount:
```

An individual account is created as an object:

```python
new_acc = BankAccount(name, balance)
```

### 2. Encapsulation

The account balance is stored as a private attribute:

```python
self.__balance = balance
```

The balance is not accessed directly outside the class. Instead, methods such as `get_balance()`, `deposit()`, and `withdraw()` are used to interact with it.

### 3. Methods

The `BankAccount` class contains several methods:

| Method          | Purpose                                          |
| --------------- | ------------------------------------------------ |
| `show()`        | Displays the account holder's name and balance   |
| `deposit()`     | Adds money to the account                        |
| `withdraw()`    | Removes money if sufficient balance is available |
| `get_balance()` | Returns the current balance                      |

### 4. Searching Objects

The `find_account()` function searches through the list of account objects:

```python
def find_account(accounts, name):
    for acc in accounts:
        if acc.name == name:
            return acc
    return None
```

This allows the program to find a specific account using the account holder's name.

### 5. List of Objects

All created accounts are stored in a list:

```python
accounts = []
```

Whenever a new account is created, its object is added to the list.

## 📋 Menu Options

```text
--Bank Management System--

1. Add Account
2. Show All Accounts
3. Check Balance
4. Deposit
5. Withdraw
6. Transfer Money
7. Delete Account
8. Exit
```

### 1. Add Account

Creates a new account using the account holder's name and initial balance.

### 2. Show All Accounts

Displays the information of every account currently stored in the system.

### 3. Check Balance

Searches for an account and displays its current balance.

### 4. Deposit

Adds a specified amount to an account.

### 5. Withdraw

Withdraws money from an account if there is sufficient balance.

If the requested amount is greater than the available balance, the program displays:

```text
Insufficient Balance
```

### 6. Transfer Money

Transfers money from one account to another.

The program checks:

* Whether the sender exists
* Whether the receiver exists
* Whether the sender has enough money

If all conditions are satisfied, the amount is withdrawn from the sender and deposited into the receiver.

### 7. Delete Account

Removes an existing account from the list.

### 8. Exit

Closes the Bank Management System.

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python main.py
```

## 💻 Example

```text
--Bank Management System--
1. Add Account
2. Show All Accounts
3. Check Balance
4. Deposit
5. Withdraw
6. Transfer Money
7. Delete Account
8. Exit

Enter your choice: 1

Account holder name: Alice
Initial Balance: 5000

Account created successfully for Alice
Balance: 5000.0
```

A transfer might look like:

```text
Enter sender account name: Alice
Enter receiver account name: Bob
Enter transfer amount: 1000

Transfer successful!
Sender Balance: 4000.0
Receiver Balance: 6000.0
```

## 📁 Project Structure

```text
Bank-Management-System/
│
├── main.py
└── README.md
```

## 🎯 Purpose

This project was created to practice Python **Object-Oriented Programming** concepts through a practical example.

The main concepts demonstrated are:

* Classes and objects
* Constructors
* Encapsulation
* Private attributes
* Instance methods
* Functions
* Lists of objects
* Object searching
* Conditional logic
* Menu-driven programs
* Basic banking operations

## 🚀 Future Improvements

Possible improvements for future versions include:

* Unique account numbers instead of searching by name
* PIN/password authentication
* Transaction history
* Saving accounts to a file or database
* Input validation for negative amounts
* Preventing duplicate account names
* A graphical user interface (GUI)
* Database integration
