#waf bonus (salary, rate =.10) that calculate new salary 
# after applying a bonus rate. call the functional once using positional args and once 
# using keyword arguments,
# show a case where incorrect mixing of positional and keyword arguments showing an error

def bonus(salary,  rate= 0.10):
    return salary+(salary*rate)

print ( bonus(salary= 1000 , rate= 0.2))
print(bonus(2000, 0.33))
print(bonus(rate=0.20, 2000))
