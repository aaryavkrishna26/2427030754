# wap to check whether a given number exist in a tuple or not

t=(1,2,3,5,7,1,3,1)
check=0

for i in t:
    if i==4:
        print("yes")
        check=1
        break
if check!=1:
    print("no")