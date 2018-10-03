print("available operator: + - * / % ")
class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        add = float(self.a) + float(self.b)
        return add
    def sub(self):
        sub = float(self.a) - float(self.b)
        return sub
    def mul(self):
        mul = float(self.a) * float(self.b)
        return mul
    def div(self):
        div = float(self.a) / float(self.b)
        return div
    def mod(self):
        mod = float(self.a) % float(self.b)


a = input("insert the number : ")
b = input("insert the number : ")
op = str(input("operator: "))
object = calculator(a,b)

if op == "+":
    print(object.add())
elif op == "-":
    print(object.sub())
elif op == "*":
    print(object.mul())
elif op == "/":
    print(object.div())
elif op == "%":
    print(object.mod())
