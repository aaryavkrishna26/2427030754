#  check a number is prime or not

n= int(input("enter a number: "))
count=0

for i in range(2,n):
    if n%i==0:
        count= count+1

if count==0:
    print("n is a prime number")
else:
    print("n is not a prime number")
    