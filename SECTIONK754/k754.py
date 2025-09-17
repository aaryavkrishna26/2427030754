a= input("enter a string")
total=0
vowels= "AEIOUaeiou"
for i in vowels:
    if i in a:
        total+=1

print("total no. of vowels:", total)