class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited: ₹{amount}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrew: ₹{amount}")
        else:
            print("Insufficient balance or invalid amount")
    def get_balance(self):
        return self.__balance
class B(BankAccount):
    def __init__(self,balance=0):
        super().__init__(balance)
    def display(self):

        print(f"Balance: ₹{self.get_balance()}")
ob=BankAccount()
ob.deposit(5000)
ob.withdraw(2000)
print(f"Current Balance: ₹{ob.get_balance()}")
ob1=B(3000)
ob1.display()