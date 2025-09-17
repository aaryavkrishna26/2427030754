# Q1) wap to input 10 numbers find smallest and largest.
import math
l=[]
for i in range(0,10):
    n= int (input("enter a number n = "))
    l.append(n)

l.sort()
print(l)
print("largest=", l[0], "smallest=", l[9])
