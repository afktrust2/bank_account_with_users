class BankAccount:
    bank_name = "Ninja Bank"
    accounts = []
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: {self.balance:.2f}")
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insuffient funds. Charging a $5 fee")
        else:
            self.balance -= amount
            print(f"Balance: {self.balance:.2f}")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance:.2f}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest 
            print(f"Balance: {self.balance:.2f}")
        return self

    @classmethod
    def all_account_info(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self):
        amount = int(input("How much do you want to deposit?: "))
        self.account.deposit(amount)
        return self

    def make_withdrawal(self):
        amount = int(input("How much do you want to withdraw?: "))
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")


User("Mark").make_deposit().make_withdrawal().display_user_balance()
