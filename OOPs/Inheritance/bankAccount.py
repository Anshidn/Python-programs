class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

    def get_balance(self):
        print(self.__balance)
        return self.__balance

account=BankAccount()

account.deposit(1000)
account.withdraw(500)

print(account.get_balance())
