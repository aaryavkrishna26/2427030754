# wap to swap the values of two variables using a tuple without using temporary variable

a,b= 1,3
print(a,b)
t=(a,b)
b,a=t
print(a,b)