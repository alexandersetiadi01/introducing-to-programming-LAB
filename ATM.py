class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = float(balance)

    def getName(self):
        return self.name

    def getCash(self,cash):
        self.cash = cash
        return self.cash

    def Balance(self):
        return self.balance

    def deposit(self,amount):
        self.amount = float(amount)
        if self.amount >= 500 :
            self.balance += self.amount
            return print(self.balance)
        else:
            return print("can't deposit below 500 !!! ")

    def withdraw(self,amount):
        self.amount = float(amount)
        if self.balance >= self.amount:
            self.balance -= self.amount
            return print(self.balance)

        else:
            return print("not enough balance")

    def debit(self,amount):
        self.amount = float(amount)
        if self.balance >= self.amount:
            self.balance -= self.amount
            return print(self.balance)

        else:
            return print("not enough balance")

A= Account("Alex",0)
while True:
    print("1.deposit" , "2.withdraw", "3.debit", "4.check balance", "5.quit")
    choice = input("choose: ")
    if choice == "1":
        Amount = float(input("enter the amount: "))
        print(A.deposit(Amount))
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






