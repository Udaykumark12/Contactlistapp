class A:
    def set_balance(self):
        self.balance = 500

    def check_balance(self):
        print("Your balance:", self.balance)

    def deposit_money(self, amount):
        self.balance += amount
        print("₹{} deposited.".format(amount))

    def withdraw_balance(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("₹{} withdrawn.".format(amount))
        else:
            print("Not enough balance.")
            

# Create object and set initial balance
atm = A()
atm.set_balance()

# Menu
while True:
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        atm.deposit_money(amount)
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        atm.withdraw_balance(amount)
    elif choice == 4:
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice. Try again.")
