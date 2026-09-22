class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def show(self):
        print("Name:", self.name)
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited amount:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Withdrawn Amount:", amount)

    def get_balance(self):
        return self.__balance


def find_account(accounts, name):
    for acc in accounts:
        if acc.name == name:
            return acc
    return None


accounts = []

while True:
    print('\n --Bank Management System--')
    print("1. Add Account")
    print("2. Show All Accounts")
    print("3. Check Balance")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Transfer Money")
    print("7. Delete Account")
    print("8. Exit")

    choice = input('Enter your choice: ')

    if choice == '1':
        name = input("Account holder name: ")
        balance = float(input("Initial Balance: "))

        new_acc = BankAccount(name, balance)
        accounts.append(new_acc)

        print(f"Account created successfully for {name}")
        print("Balance:", new_acc.get_balance())

    elif choice == '2':
        if len(accounts) == 0:
            print("No accounts found")
        else:
            for acc in accounts:
                print("\n --Account Info--")
                acc.show()

    elif choice == '3':
        name = input("Enter account holder name: ")
        acc = find_account(accounts, name)

        if acc is None:
            print("Account not found")
        else:
            print("Balance:", acc.get_balance())

    elif choice == '4':
        name = input("Enter account holder name: ")
        acc = find_account(accounts, name)

        if acc is None:
            print("Account not found")
        else:
            deposit_amount = float(input("Enter deposit amount: "))
            acc.deposit(deposit_amount)
            print("Final Balance:", acc.get_balance())
    elif choice == '5':
        name = input("Enter account holder name: ")
        acc = find_account(accounts, name)

        if acc is None:
            print("Account not found")
        else:
            withdraw_amount = float(input("Enter Withdraw Amount: "))
            acc.withdraw(withdraw_amount)
            print("Final Balance:", acc.get_balance())   

    elif choice == '6':
        sender_name = input("Enter sender account name: ")
        sender = find_account(accounts, sender_name)

        if sender is None:
            print("Sender account not found")

        else:
            receiver_name = input("Enter receiver account name: ")
            receiver = find_account(accounts, receiver_name)

            if receiver is None:
                print("Receiver account not found")

            else:
                amount = float(input("Enter transfer amount: "))

                if amount > sender.get_balance():
                    print("Insufficient Balance")

                else:
                    sender.withdraw(amount)
                    receiver.deposit(amount)

                    print("Transfer successful!")
                    print("Sender Balance:", sender.get_balance())
                    print("Receiver Balance:", receiver.get_balance())

    elif choice == '7':
        name = input("Enter account holder name: ")
        acc = find_account(accounts, name)

        if acc is None:
            print("Account not found")

        else:
            accounts.remove(acc)
            print(f"Account of {name} deleted successfully")


    elif choice == '8':
        print("System closed")
        break

    else:
        print("Invalid choice")

