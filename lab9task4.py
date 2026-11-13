class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


account1 = BankAccount("Aimal", 5000)

account1.deposit(2000)
account1.withdraw(1000)
account1.display_balance()