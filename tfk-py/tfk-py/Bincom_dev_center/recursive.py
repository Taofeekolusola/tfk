def binary_search_recursive(arr, target, low, high):
    # Base case: if the search range is empty, the target is not in the list
    if low > high:
        return -1  # Target not found
    
    # Calculate the middle index of the current search range
    mid = (low + high) // 2
    
    # Check if the middle element is the target
    if arr[mid] == target:
        return mid  # Target found at index mid
    
    # If the target is smaller than the middle element, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    
    # If the target is larger than the middle element, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# Example usage:
user_input = int(input("Enter the number to search for: "))
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search_recursive(my_list, user_input, 0, len(my_list) - 1)

if result != -1:
    print(f"Number {user_input} found at index {result}.")
else:
    print(f"Number {user_input} not found in the list.")
