#right triangle
m = 10
for x in range(0, m):
    print(" ")
    for y in range(0, x+1):
        print("*", end=" ")

print("")

#left triangle
num = 10
x = 1
while x <= num:
    print(" "*(num-x)+"*"*x)
    x +=1


#pyramid
num = 10
x = 1
while x <= num:
    print(" "*(num-x)+"*"*(x+(x-1)))
    x +=1


#diamond
num = 10
x = 1
while x <= num:
    print(" "*(num-x) + "*"*(2*x-1))
    x +=1


#reverse pyramid
num = 10
x = 1
while x <= num:
    print(" "*x + "*"*((num-x)*2-1))
    x +=1


#reverse left triangle
num = 10
x = 1
while x <= num:
    print(" "*x + "*"*(num-x))
    x +=1

#reverse right triangle
num = 10
x = 1
while x <= num:
    print(" "*num + "*"*(num-x))
    x +=1