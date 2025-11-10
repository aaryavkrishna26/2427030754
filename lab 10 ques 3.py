#Q3. File Data Reader
#Write a Python program that:
#• Asks the user to input a filename to read data from.
##• Displays the file content line by line.
##  - FileNotFoundError: If the file does not exist.
  # - PermissionError: If the file is not accessible.
   ##- Generic Exception: For other possible file reading errors.

def file_data_reader():
    try:
        filename = input("Enter filename to read: ")
        with open(filename, "r") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied to access the file.")
    except UnicodeDecodeError:
        print("Error: The file contains unreadable characters.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_data_reader()

