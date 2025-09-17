a= int(input("enter a "))
b= int(input("enter b "))
c= int(input("enter c "))
d= int(input("enter d "))

sum=a+b+c+d

if sum>1000:
    disc_price= sum*.9

gstbill= disc_price*.12

grandtotal= disc_price + gstbill

print("sum=", sum)
print("disc_price=", disc_price)
print("gstbill= ", gstbill)
print("grandtotal= ", grandtotal)