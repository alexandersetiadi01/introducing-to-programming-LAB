# ATM program Alex version using python

class Account:
    def __init__(self,name,balance):    # initialize name and balance
        self.name = name    #
        self.balance = float(balance)

    def getName(self):
        return self.name

    def getCash(self):
        return self.cash

    def Balance(self):
        return self.balance

    def deposit(self,amount,cash):
        self.amount = float(amount)
        self.cash = float(cash)
        if self.amount > 0:
            if self.cash >= self.amount:
                self.balance += self.amount
                self.cash -= self.balance
                return print("balance = {} cash = {}".format(self.balance, self.cash))
            else:
                return print("go get some money!!")
        else:
            return print("where is your money???")

    def withdraw(self,amount):
        self.amount = float(amount)
        if self.balance >= self.amount:
            self.balance -= self.amount
            self.cash += self.amount
            return print("balance = {} cash = {}".format(self.balance, self.cash))
        else:
            return print("go make some money!!")

    def debit(self,amount):
        self.amount = float(amount)
        if self.balance >= self.amount:
            self.balance -= self.amount
            self.cash += 0
            return print("balance = {} cash = {}".format(self.balance, self.cash))
        else:
            return print("not enough balance")

N = input("enter your name: ")
A= Account(N,0)
Cash = input("cash = ")
print(Cash)
while True:
    print("1.deposit" , "2.withdraw", "3.debit", "4.check balance", "5.quit")
    choice = input("choose: ")
    if choice == "1":
        Amount = float(input("enter the amount: "))
        print(A.deposit(Amount,Cash))

    elif choice == "2":
        Amount = float(input("enter the amount: "))
        print(A.withdraw(Amount))
    elif choice == "3":
        Amount = float(input("enter the amount: "))
        print(A.debit(Amount))
    elif choice == "4":
        print(A.Balance())
    elif choice == "5":
        print("have a nice day")
        break






