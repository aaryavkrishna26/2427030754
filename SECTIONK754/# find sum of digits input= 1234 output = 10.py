# find sum of digits input= 1234 output = 10

n= 1234
sum=0
while n>0:
    rem= n%10
    sum+=rem
    n= n//10

print(sum)