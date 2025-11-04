# q3) A school has a person, teacher and a class teacher. each level add its own properties and method. 



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f" Name: {self.name}")
        print(f" Age: {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject, salary):

        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display(self):
   
        super().display()
        print(f" Subject: {self.subject}")
        print(f"Salary: ₹{self.salary}")

    def teach(self):
        print(f" {self.name} is teaching {self.subject} to students.")


class ClassTeacher(Teacher):
    def __init__(self, name, age, subject, salary, class_name, num_students):

        super().__init__(name, age, subject, salary)
        self.class_name = class_name
        self.num_students = num_students

    def display(self):
       
        super().display()
        print(f" Class Incharge: {self.class_name}")
        print(f" Number of Students: {self.num_students}")

    def conduct_meeting(self):
        print(f" {self.name} is conducting a parent–teacher meeting for class {self.class_name}.")


person1 = Person("Aarav", 28)
teacher1 = Teacher("Ms. Nisha", 35, "Mathematics", 50000)
class_teacher1 = ClassTeacher("Mr. Raj", 40, "Science", 55000, "10A", 45)


person1.display()

teacher1.display()
teacher1.teach()

class_teacher1.display()
class_teacher1.conduct_meeting()
