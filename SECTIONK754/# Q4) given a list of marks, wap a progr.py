# Q4) given a list of marks, wap a program to find avg of marks.

import math
sum=0
n= int(input("enter the total no. of subjects: "))
for i in range(n):
    marks= int(input("enter marks"))
    sum= sum+ marks

avg= sum/n

print("average=", avg)




