# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = left + (right - left) // 2  # Calculate the midpoint to divide the search interval in half

#         if arr[mid] == target:
#             return mid  # Found the target, return its index
#         elif arr[mid] < target:
#             left = mid + 1  # Target is in the right half, so update the left boundary
#         else:
#             right = mid - 1  # Target is in the left half, so update the right boundary

#     return -1  # Target not found in the array

# # Example usage
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 6
# result = binary_search(arr, target)

# if result != -1:
#     print(f"Element {target} is present at index {result}")
# else:
#     print(f"Element {target} is not present in the array")


# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = left + (right - left) // 2
        
#         if arr[mid] == target:
#             return target
        
#         elif arr[mid] < target:
#             left = mid + 1

#         elif arr[mid] > target:
#             right = mid - 1

#     return -1



# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 2
# result = binary_search(arr, target)

# if result != -1:
#     print(f"Element {target} is present at index {result}")
# else:
#     print(f"Element {target} is not present in the array")


# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == target:
#             return mid
#         if guess > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None

# arr = list(range(11))
# target = 7

# result = binary_search(arr, target)
# print(result)


# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) - 1 // 2

#         if arr[mid] == target:
#             return mid
        
#         elif arr[mid] > target:
#             high = mid - 1

#         elif arr[mid] < target:
#             low = mid + 1

#     return None



# arr = list(range(11))
# target = 4

# result = binary_search(arr, target)

# print(result)


