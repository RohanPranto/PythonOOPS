class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

class BankAccount:
    def __init__(self):
        self._balance = int(input("Enter your main balance: "))

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Deposit amount must be positive")
        self._balance+=amount

    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Withdraw amount must be positive")
        if amount>=self._balance:
            raise ValueError("Insufficient funds!")
        self._balance-=amount


account=BankAccount()
print(f"Current balance: {account.balance}rs")
account.deposit(int(input("Enter the money you want to deposite:  ")))

print(f"Current balance: {account.balance}rs")
account.withdraw(int(input("Enter the money you want to withdraw:  ")))
 
print(f"Bro you have only {account.balance}rs left in your account. why dont you use wallet for that? Why do you need bank account for {account.balance}rs?")


'''
This class is an example of **encapsulation** because it hides the internal balance variable 
(_balance) from direct access outside the class. Access and modification to the balance are 
only allowed through defined methods (deposit, withdraw) and a read-only property (balance).
This protects the data and ensures that any changes to the balance go through validation checks.
'''