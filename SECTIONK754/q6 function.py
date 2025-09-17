# design a func studentrecord(course, *subject,**details) that
#1) store the course name
#2) store multiple subjects using * argument
#3) storedetails like name, age, grade using keyword arguments
#wap that demonstrates all function cases using function call

def studentrecord(course, *subjects, **details):

    print(course)
    print(subjects)
    print(details)

studentrecord("btech", "physics", "chemistry", "biology", name= "aaryav", section= "k")

    
    




