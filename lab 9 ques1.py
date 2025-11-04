#linear search

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  
    return -1  


arr = [10, 25, 7, 9, 30]
key = int(input("Enter element to search: "))

result = linear_search(arr, key)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
