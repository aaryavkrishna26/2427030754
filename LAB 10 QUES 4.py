#Q4. List Element Access
#Write a Python program that:
#• Takes a list of integers and an index number from the user.
#• Prints the element present at that index.
#  - IndexError: If the index is out of range.
 #  - ValueError: If a non-integer index is entered.
  # - TypeError: If the list contains incompatible data types.
   #- Generic Exception: For any other error.

def list_element_access():
    try:
        elements_input = input("Enter a list of integers (comma separated): ")
        elements = [int(x.strip()) for x in elements_input.split(",")]
        index = int(input("Enter index number: "))
        
        element = elements[index]
        print(f"Element at index {index} is {element}")
        
    except IndexError:
        print("Error: Index is out of range.")
    except ValueError:
        print("Error: Please enter integer values only.")
    except TypeError:
        print("Error: List contains incompatible data types.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

list_element_access()
