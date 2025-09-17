#  wap a program to convert a tuple into a list and add a new element

t=(1,2,3,4)
l=list(t)
l.append(10)
t=tuple(l)
print(t)