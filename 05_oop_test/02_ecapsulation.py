class BankAccount:
    def __init__(self,balance):
        # self.balance = balance
        self.__balance = balance # __balance is private

    def set_deposit(self, amount):
        self.__balance += amount
        # self.__balance = self.__balance + amount


    def get_balance(self):
        return  self.__balance


account = BankAccount(10000)
account.set_deposit(5000)
print(f"Account 1 {account.get_balance()}")


account2 = BankAccount(7000000)
account2.set_deposit(500000)
print(f"Account 2 {account2.get_balance()}")