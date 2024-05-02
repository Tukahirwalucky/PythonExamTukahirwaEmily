#NUMBER 4(b)

class Sacco:
    def __init__(self):
        self.balance = 0

#deositing money
    def deposit(self, amount):
        if amount >= 1000:
            self.balance += amount
            print(f"Deposit of {amount} successfully made.")
        else:
            print("Minimum deposit amount is 1000.")

#withdrawing money
    def withdraw(self, amount):
        if amount >= 500 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successfully made.")
        elif amount < 500:
            print("Minimum withdrawal amount is 500.")
        else:
            print("Insufficient funds.")

#checking balance
    def check_balance(self):
        print(f"Your account balance is: {self.balance}")


def main():
    sacco = Sacco()
    print("Welcome  WITU Sacco")

    while True:
        print("\nMenu:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")

#checking for input choices    
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            sacco.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            sacco.withdraw(amount)
        elif choice == '3':
            sacco.check_balance()
        elif choice == '4':
            print("Thank you for using Witu Sacco.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
