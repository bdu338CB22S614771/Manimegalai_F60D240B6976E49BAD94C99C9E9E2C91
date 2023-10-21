class BankAccount:
    def __init__(self):
     self. balance=0
    print(" Hello!!! welcome to deposit & withdrawal machine")
    def deposit(self):
        amount = float(input("enter amount to be deposited:"))
        self.balance += amount
        print("\n Amount Deposited:", amount)
    def withdraw(self):
        amount =float(input("enter amount to be withdrawn:"))
        if self.balance >=amount:
           self. balance-=amount
           print("\nAmount withdrawn:", amount)
        else:
            print("\nInsufficient balance ")
    def display(self):
            print("\nAccount balance=", self. balance)
s = BankAccount()
s.deposit()
s.withdraw()
s.display()




