#binary_search

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [5, 8, 12, 20, 33, 45, 60]  # must be sorted
key = int(input("Enter element to search: "))

result = binary_search(arr, key)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
