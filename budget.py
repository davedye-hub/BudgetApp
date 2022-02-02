class Budget():
    def __init__(self, balance, category):
        self.balance = balance
        self.category = category
    
    def __repr__(self):
        return f"The balance in this budget is £{self.balance}."
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

