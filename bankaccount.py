class BankAccount:
    def __init__(self, number, name, city, balance=0):
        print("A new bank account was created")
        self.number = number
        self.name = name
        self.city = city
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough balance to withdraw")    
    def __str__(self):
        return f" Bank account details for: {self.name} with account_number:{self.number} and amount: {self.balance}"                