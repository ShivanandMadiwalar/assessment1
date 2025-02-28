class CustomerAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

def main():
    accounts = {}
    menu = ("\nBanking System Menu:\n"
            "1. Create Account\n"
            "2. Deposit Money\n"
            "3. Withdraw Money\n"
            "4. Check Balance\n"
            "5. Exit")
    while True:
        print(menu)
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            if account_number in accounts:
                print("Account already exists.")
            else:
                accounts[account_number] = CustomerAccount(account_number, account_holder)
                print("Account created successfully.")

        elif choice in {'2', '3', '4'}:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                if choice == '2':
                    amount = float(input("Enter amount to deposit: "))
                    accounts[account_number].deposit(amount)
                elif choice == '3':
                    amount = float(input("Enter amount to withdraw: "))
                    accounts[account_number].withdraw(amount)
                elif choice == '4':
                    accounts[account_number].check_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            print("Exiting the banking system. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
