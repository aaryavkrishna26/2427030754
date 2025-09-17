# wap to count how many times a particular element appears in a tuple using loop

t=(1,2,1,3,4,5,1)
count=0

l= len(t)

for i in t:
    if i==1:
        count+=1

print("total occurence of 1 = ", count)
