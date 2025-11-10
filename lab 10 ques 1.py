#Q1. Student Result Processing Program
#Write a Python program that:
#a) Takes input of marks obtained and total marks.
#b) Calculates the percentage of the student.
#c) Handles possible exceptions like:
 #  • ValueError: When non-numeric input is given.
  # • ZeroDivisionError: When the total marks entered is zero.
   #• FileNotFoundError: When the result file to store data is missing.
   #• Generic Exception: To handle any other unexpected errors.


def student_result_processing():
    try:
        marks_obtained = float(input("Enter marks obtained: "))
        total_marks = float(input("Enter total marks: "))
        
        percentage = (marks_obtained / total_marks) * 100
        print(f"Percentage: {percentage:.2f}%")
        
        with open("result.txt", "w") as file:
            file.write(f"Marks Obtained: {marks_obtained}\n")
            file.write(f"Total Marks: {total_marks}\n")
            file.write(f"Percentage: {percentage:.2f}%\n")
        print("Result saved to result.txt")
        
    except ValueError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Total marks cannot be zero.")
    except FileNotFoundError:
        print("Error: The result file could not be created or accessed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

student_result_processing()

