# class A:
#     def set_balance(self,balance):
#         self.balance=balance
#
#     def check_balance(self):
#         print("your balance is",self.balance)
#
#     def withdraw(self,amount):
#         if amount <=self.balance:
#             self.balance-=amount
#             print("withdwar succfll",amount)
#         else:
#             print("enter valid amount")
#
# atm=A()
# atm.set_balance(1000)
#
# while True:
#     while True:
#         print("\n=== ATM MENU ===")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")
#
#         choice=int(input("enter choice"))
#
#         if choice==1:
#             atm.check_balance()
#         elif choice==3:
#             amount=int(input("enter amount to withdraw"))
#             atm.withdraw(amount)
#             atm.check_balance()
#             break


class b:
    def __init__(self):
        self.balance=500

    def check_balance(self):
        print("your balance is",self.balance)

    def withdrwaw(self,amount):
        if amount <=self.balance:
            self.balance-=amount
            print("wihrdraw sucees",amount)
        else:
            print("not sufficient")
obj=b()


while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")


        choice=int(input("enter your choice"))

        if choice==1:
            obj.check_balance()
        elif choice==3:
            amount = int(input("enter amount to withdraw"))
            obj.withdrwaw(amount)
            obj.check_balance()
            break







