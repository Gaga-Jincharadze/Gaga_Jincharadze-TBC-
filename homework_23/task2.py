class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Not enough money")
        elif amount > 0:
            self._balance -= amount
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self._balance

Start_Balance = BankAccount(1000)

Start_Balance.deposit(500)
print(Start_Balance.get_balance())

Start_Balance.withdraw(200)
print(Start_Balance.get_balance())

Start_Balance.withdraw(2000)
print(Start_Balance.get_balance())
