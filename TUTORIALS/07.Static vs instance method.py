class BankAccount:
    MIN_BALANCE = 100

    def __init__(self,owner, balance = 0):
        self.owner=owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)

        else:
            print("Deposit amount must be positive")


    def _is_valid_amount(Self, amount):
        return amount>0
    
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of {amount} . New balance is {self._balance}")


    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5 #it means that the rate is between 0 and 5. return 0 means false and 1 means true.

account = BankAccount("Alice", 5100)
account.deposit(200)


print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))