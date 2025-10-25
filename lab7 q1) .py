# q1) a) create a base class person with attributes: name and age 
#     b) create a derived class employee that inherits from person and add attributes employee id and salary.
#     c) implement multilevel inheritence with the class manager derived from employee with the department attribute.
#     d) implement multiple inheritance with the class trainer that inherits from employee and certifications.
#     e) write appropiate method to display all details for rach type of employee. create objects for each and their information.



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    
    def display(self):
        
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


class Manager(Employee):  
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):

        print("Department:", self.department)

class certifications:
    def __init__(self, certificate):
        self.certificate= certificate

    def display(self):
        print ("certification = ", self.certificate)

class Trainer(Employee, certifications):
    def __init__(self, name, age, employee_id, salary, cert_list):
        Employee.__init__(self, name, age, employee_id, salary)
        certifications.__init__(self, cert_list)

    def display(self):
        Employee.display(self)
        
    



p1 = Person("Alice", 25)
e1 = Employee("Bob", 30, "E101", 50000)
d1 = Manager("Ravi", 35, "M202", 70000, "Sales")
c1 = certifications(["Python", "Data Science"])
t1 = Trainer("David", 35, "T301", 60000, ["Python", "Data Science"])

p1.display()
e1.display()
d1.display()
c1.display()
t1.display()