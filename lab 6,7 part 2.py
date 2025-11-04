# create 2 employees and printtheir salary slips, methods:

# calaculate_salary() -> returns total salary after adding da 20% and hra 15%
# display()-> prints emplyee setails with total salary

class employee() :
    def __init__(self,emp_id, name, salary):
        self.emp_id= emp_id
        self.name= name
        self.salary= salary

    def calculate_salary(self, salary):
        total_salary= self.salary + 0.2* self.salary + 0.15* self.salary
        print("total salary is : ", total_salary)
    

    def display(self):
        print(f"my emp_id is {self.emp_id} ")
        print(f"my name is {self.name} ")
        print(f"my salary is {self.salary} ")
        
employee_details= employee(24436758, "aaryav", 100000)
employee_details.calculate_salary(10000)
employee_details.display()



