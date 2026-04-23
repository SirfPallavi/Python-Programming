class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self,amount):
        self.balance -= amount
        print("debited amount is :" ,amount)

    def credit(self,amount):
        self.balance += amount
        print("credited amount is :", amount)


    def display_balance(self):
        print("balance is :" , self.balance)

        def get_balance(self):
            return self.balance


        acc1 =Account(1000, "123456789")
        print(acc1.balance)
        print(acc1.account_number)