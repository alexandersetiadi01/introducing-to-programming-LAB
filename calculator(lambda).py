a = input(": ")
b = input(': ')
operator = input("choose operator: ")

A = int(a)
B = int(b)
op = str(operator)


if op == "+":
    add = lambda A,B: A+B
    print(add(A,B))
elif op == "-":
    min = lambda A,B: A-B
    print(min(A,B))lamb
elif op == "/":
    div = lambda A,B: A/B
    print(div(A,B))
elif op == "*":
    mul =lambda A,B: A*B
    print(mul(A,B))

