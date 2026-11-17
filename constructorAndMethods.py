class BankAccount:
    def __init__(self, accountHolder, accountBalance):
        self.accountHolder = accountHolder
        self.accountBalance = accountBalance

    def depositAmount(self, amount):
        self.accountBalance += amount
        print("Deposited:", amount)

    def displayBalance(self):
        print("Account Holder:", self.accountHolder)
        print("Current Balance:", self.accountBalance)


myAccount = BankAccount("Aman Verma", 5000)
myAccount.displayBalance()
myAccount.depositAmount(1500)
myAccount.displayBalance()
