# q1 DISPLAY MULTIPLICATION TABLE OF A NUMBER 

n= int(input("enter a number"))
for i in range(1,11):
    mtable= i*n
    print(n, "*", i, "=", mtable)