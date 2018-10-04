# ATM program Alex version using python

class Account:                          # making class called Account
    def __init__(self,name,balance):    # initialize name and balance
        self.name = name                # declare that name is part of the class Account   
        self.balance = float(balance)   # declare that balance is part of the class Account   

    def getName(self):                  # make a getName function 
        return self.name                # show self.name 

    def getCash(self):                  # make a getCash function
        return self.cash                # show self.cash

    def Balance(self):                  # make a function for balance
        return self.balance             # show self.balance

    def deposit(self,amount,cash):      # make a deposit function 
        self.amount = float(amount)     # make amount that will be used for how much money you deposit (its local to this function)
        self.cash = float(cash)         # declare cash as a part of this class
        if self.amount > 0:             # if the amount of money we want to deposit is greater than 0
            
            if self.cash >= self.amount:    # if your cash is greater or equal to the amount, run the code
                self.balance += self.amount # for deposit, balance will be added by amount (ex: balance=0 amount=400, deposit=0+400)
                self.cash -= self.amount   # for deposit, our real money/cash will be decreased by the amount  
                return print("balance = {} cash = {}".format(self.balance, self.cash))
                # print result for the balance and cash after depositing
            
            else:                           # if cash is less than amount,run the code
                return print("go get some money!!") # print this sentence
        
        else:                               # if the amount is less or equal to 0 ,run the code
            return print("where is your money???") # print this sentence

    def withdraw(self,amount):              # function for withdraw 
        self.amount = float(amount)         # make amount that will be used for how much money you deposit (its local to this function)
        if self.balance >= self.amount:     # if balance is greater or equal to the amount,run the code
            self.balance -= self.amount     # for withdraw, balance is decreased by amount
            self.cash += self.amount        # for withdraw, our cash is increased by amount
            return print("balance = {} cash = {}".format(self.balance, self.cash)) 
            # print the result of balance and cash after withdrawing
        
        else:                 
            return print("go make some money!!")    #else,print the sentence

    def debit(self,amount):                 # function for debit
        self.amount = float(amount)         # make amount that will be used for how much money you deposit (its local to this function)
        if self.balance >= self.amount:     # if balance is greater or equal to the amount, run the code
            self.balance -= self.amount     # for debit, balance is decreased by amount
            self.cash += 0                  # for debit, our cash won't increased by amount so its +0
            return print("balance = {} cash = {}".format(self.balance, self.cash))
            # print the result of balance and cash after debit
        else:
            return print("not enough balance")  # else , print this sentence

N = input("enter your name: ")              # type your name for the ATM (up to you)
A= Account(N,0)                             # A is an object to call class Account
Cash = input("cash = ")                     # enter how much money you want for your cash (up to you)
print(Cash)                                 # print cash

while True:    # use while looping to make this endless until you choose to quit
    print("option:","1.deposit" , "2.withdraw", "3.debit", "4.check balance", "5.quit")   # show the available option
    choice = input("choose: ")  # enter your choice from the option
    
    if choice == "1":           # if your choice is option 1         
        Amount = float(input("enter the amount: ")) # enter the amount that you want to deposit
        print(A.deposit(Amount,Cash))               # print the resul of deposit (will show you balance and cash)

    elif choice == "2":         # if your choice is option 2
        Amount = float(input("enter the amount: ")) # enter the amount that you want to withdraw
        print(A.withdraw(Amount))                   # print the result of withdraw(will show you balance and cash)
    
    elif choice == "3":         # if your choice is option 3
        Amount = float(input("enter the amount: ")) # enter the amount that you want to debit
        print(A.debit(Amount))                      # print the result of debit (will show you balance and cash)
    
    elif choice == "4":         # if your choice is option 4
        print(A.Balance())      # print the balance
    
    elif choice == "5":         # if your choice is option 5
        print("have a nice day")# print this sentence
        break                   # to break the loop and stop the program
    





