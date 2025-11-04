class student():
    def __init__(self, name, roll_no, marks):
        self.name= name
        self.roll_no= roll_no
        self.marks= marks

    def display(self):
        print(f"my name is {self.name} ")
        print(f"my roll no is {self.roll_no} ")
        print(f"my marks are {self.marks} ")

    def grade(self):
        if self.marks>= 40:
            print("pass")
        else:
            print("fail")



student_details= student("aaryav", 1234, 80)
student_details.grade()
student_details.display()


        
