#Polymorphism 

# Design a python program for a university system to manage student grades and evaluation demonstrating polymorphism. 
# A) Method overriding: create a base class Person with a method get roll. Create derived classes student and staff that override get roll. 
# B) Method overloading: create a class Grade with a method Calculate using default argument to handle single or multiple marks.
# C) operator overloading: create a class Score with attribute Marks. Overload the plus operator using add to sum two score objects. 
# Create objects and demonstrate all types of polymorphism 

class Person:
    def get_roll(self):
        print("Person has a general roll number.")

class Student(Person):
    def get_roll(self):
        print("Student Roll Number: S123")

class Staff(Person):
    def get_roll(self):
        print("Staff ID: ST456")



class Grade:
    def Calculate(self, m1=None, m2=None, m3=None):
        if m1 is not None and m2 is not None and m3 is not None:
            avg = (m1 + m2 + m3) / 3
            print("Average of three marks:", avg)
        elif m1 is not None and m2 is not None:
            avg = (m1 + m2) / 2
            print("Average of two marks:", avg)
        elif m1 is not None:
            print("Single mark:", m1)
        else:
            print("No marks provided")



class Score:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return Score(self.marks + other.marks)

    def __str__(self):
        return str(self.marks)



print("Method Overriding")
p1 = Person()
s1 = Student()
st1 = Staff()

p1.get_roll()
s1.get_roll()
st1.get_roll()

print("Method Overloading")
g = Grade()
g.Calculate(85)
g.Calculate(80, 90)
g.Calculate(70, 80, 90)

print("\n=== Operator Overloading ===")
score1 = Score(50)
score2 = Score(40)
total = score1 + score2
print("Total Score =", total)
