#right triangle
m = 10                          # the number of column that you want to make
for x in range(0, m):           # a loop for the column
    print(" ")                  # create space 
    for y in range(0, x+1):     # a loop for the row    
        print("*", end=" ")     # create the star with "*" until the loop stop  
        
print("")                      


#left triangle
num = 10                        # the number of column that you want to make
x = 1                           # starting row and column 
while x <= num:                 
    print(" "*(num-x)+"*"*x)    # create space to make it go down or new row (num-x) times and for each row, create star("*") x times    
    x +=1                       # each times it loop, increase the value of x by 1


#pyramid                        
num = 10                        
x = 1
while x <= num:
    print(" "*(num-x)+"*"*(x+(x-1)))    #create space to make it go down or new row (num-x) times and for each row, create star("*") (x+(x-1)) times
    x +=1                               #each times it loop, increase the value of x by 1


#diamond
num = 10
x = 1
while x <= num:
    print(" "*(num-x) + "*"*(2*x-1))    #create space to make it go down or new row (num-x) times and for each row, create star (2*x-1) times
    x +=1                               #for each loop, increase the value of x by 1



#reverse left triangle
num = 10                                
x = 1
while x <= num:
    print(" "*x + "*"*(num-x))          #create space to make it go down or make row x times and for each row, create star (num-x) times
    x +=1                               #for each loop, increase the value of x by 1

#reverse right triangle
num = 10        
x = 1
while x <= num:
    print(" "*num + "*"*(num-x))        #create space to make it go down or make row (num) times and for each row, create star (num-x) times
    x +=1                               #for each loop, increase the value of x by 1
