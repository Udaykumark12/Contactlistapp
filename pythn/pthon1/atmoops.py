class ATM:
    def balance_a(self):
        self.balance=500

    def check_balance(self):
        self.balance_a()
        print("Your balance is:", self.balance)

    def withdraw_amount(self, amount):
        self.balance_a()
        if self.balance >= amount:
            self.balance -= amount
            print("Transaction complete. Amount withdrawn:", amount)
            self.check_balance()
        else:
            print("Insufficient balance. Cannot withdraw", amount)


my_atm = ATM()

my_atm.withdraw_amount(200)

# print("Welcome to the ATM machine")
#
# while True:
#     print("\n1. Check balance")
#     print("2. Withdraw")
#     print("3. Exit")
#
#     try:
#         choice = int(input("Enter your choice: "))
#
#         if choice == 1:
#             my_atm.check_balance()
#
#         elif choice == 2:
#             amount = int(input("Enter amount to withdraw: "))
#             my_atm.withdraw_amount(amount)
#
#         elif choice == 3:
#             print("Thank you for using the ATM. Goodbye!")
#             break
#
#         else:
#             print("Invalid choice. Please enter 1, 2, or 3.")
#
#     except ValueError:
#         print("Please enter a valid number.")
