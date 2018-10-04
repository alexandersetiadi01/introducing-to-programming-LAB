# program for calculator using class in python languange
# class calculator Alex version

print("available operator: + - * / % ")     ''' show all available operator so that the 
                                             user know what kind of calculation this calculator can'''

class calculator():                         # making class called calculator
    
    def __init__(self,a,b):                 # initialize a and b
        self.a = a                          # declare that a is part of the class
        self.b = b                          # declare that b is part of the class
    
    def add(self):                          # function for adding / (+)
        add = float(self.a) + float(self.b) # add is a result from a+b
        return add                          # show the result of add
    
    def sub(self):                          # function for subtracting
        sub = float(self.a) - float(self.b) # sub is a result from a-b
        return sub                          # show the result of sub
    
    def mul(self):                          # function for multiplying
        mul = float(self.a) * float(self.b) # mul is a result from a*b or axb 
        return mul                          # show the result of mul
    
    def div(self):                          # function for divide 
        div = float(self.a) / float(self.b) # div is a result from a/b or a divided by b
        return div                          # show the resulf of div
    
    def mod(self):                          # function for modulus
        mod = float(self.a) % float(self.b) # mod is a result from a%b 
        return mod                          # show the result of mod

a = input("insert the number : ")           # input the first number (the number is up to you)
b = input("insert the number : ")           # input the second number (the number is up to you)
op = str(input("operator: "))               ''' input the operator for what kind of calculation you want
                                                ex: "-" for subtract calculation'''
object = calculator(a,b)                    # make an object called object to call the class calculator

# using if statement to choose the operator 
if op == "+":                               # if the operator is "+" that means add                          
    print(object.add())                     # print the result of add from object (the add that we made in the class calculator) 
elif op == "-":                             # if the operator is "-" that means subtract
    print(object.sub())                     # print the result of sub from object (the add that we made in the class calculator) 
elif op == "*":                             # if the operator is "*" that means multiply
    print(object.mul())                     # print the result of mul from object (the add that we made in the class calculator) 
elif op == "/":                             # if the operator is "/" that means divide
    print(object.div())                     # print the result of div from object (the add that we made in the class calculator) 
elif op == "%":                             # if the operator is "%" that means modulus
    print(object.mod())                     # print the result of mod from object (the add that we made in the class calculator) 
