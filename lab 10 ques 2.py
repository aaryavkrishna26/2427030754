#Q2. Employee Salary Calculation Program
#Write a Python program that:
#• Takes input for basic salary, HRA, and DA.
##• Calculates the gross salary (gross = basic + HRA + DA).
#  - ValueError: If the user enters a non-numeric value.
 # - KeyboardInterrupt: If the user interrupts input using Ctrl+C.
  # - Generic Exception: To handle any other unknown errors.


def employee_salary_calculation():
    try:
        basic_salary = float(input("Enter basic salary: "))
        hra = float(input("Enter HRA: "))
        da = float(input("Enter DA: "))
        
        gross_salary = basic_salary + hra + da
        print(f"Gross Salary: {gross_salary:.2f}")
        
    except ValueError:
        print("Error: Please enter numeric values only.")
    except TypeError:
        print("Error: Unsupported data type used in calculation.")
    except KeyboardInterrupt:
        print("Input interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

employee_salary_calculation()

