# # def binary_search(arr, target):
# #     left, right = 0, len(arr) - 1

# #     while left <= right:
# #         mid = left + (right - left) // 2  # Calculate the midpoint to divide the search interval in half

# #         if arr[mid] == target:
# #             return mid  # Found the target, return its index
# #         elif arr[mid] < target:
# #             left = mid + 1  # Target is in the right half, so update the left boundary
# #         else:
# #             right = mid - 1  # Target is in the left half, so update the right boundary

# #     return -1  # Target not found in the array

# # # Example usage
# # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # target = 6
# # result = binary_search(arr, target)

# # if result != -1:
# #     print(f"Element {target} is present at index {result}")
# # else:
# #     print(f"Element {target} is not present in the array")


# # def binary_search(arr, target):
# #     left, right = 0, len(arr) - 1

# #     while left <= right:
# #         mid = left + (right - left) // 2

# #         if arr[mid] == target:
# #             return target

# #         elif arr[mid] < target:
# #             left = mid + 1

# #         elif arr[mid] > target:
# #             right = mid - 1

# #     return -1


# # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # target = 2
# # result = binary_search(arr, target)

# # if result != -1:
# #     print(f"Element {target} is present at index {result}")
# # else:
# #     print(f"Element {target} is not present in the array")


# # def binary_search(arr, target):
# #     low = 0
# #     high = len(arr) - 1

# #     while low <= high:
# #         mid = (low + high) // 2
# #         guess = arr[mid]
# #         if guess == target:
# #             return mid
# #         if guess > target:
# #             high = mid - 1
# #         else:
# #             low = mid + 1
# #     return None

# # arr = list(range(11))
# # target = 7

# # result = binary_search(arr, target)
# # print(result)


# # def binary_search(arr, target):
# #     low = 0
# #     high = len(arr) - 1

# #     while low <= high:
# #         mid = (low + high) - 1 // 2

# #         if arr[mid] == target:
# #             return mid

# #         elif arr[mid] > target:
# #             high = mid - 1

# #         elif arr[mid] < target:
# #             low = mid + 1

# #     return None


# # arr = list(range(11))
# # target = 4

# # result = binary_search(arr, target)

# # print(result)


# # def binary_search(names, target):
# #     left, right = 0, len(names) - 1

# #     while left <= right:
# #         guess = (left + right) // 2

# #         if names[guess] == target:
# #             return guess

# #         elif names[guess] < target:
# #             left = guess + 1

# #         else:
# #             right = guess - 1

# #     return -1

# # target = "Tim"
# # names = sorted(["Tim", "John", "Snow", "KD", "Lara", "Mo", "Selene"])

# # result = binary_search(names, target)
# # if result != -1:
# #     print("{} found at index {}".format(target, result))
# # else:
# #     print("{} not found in the list.".format(target))

# # def binary_search(names, target):

# #     l, r = 0, len(names) -1

# #     while l <= r:
# #         m = (l + r) // 2

# #         if names[m] == target:
# #             return m

# #         elif names[m] < target:
# #             l = m + 1

# #         elif names[m] > target:
# #             r = m - 1

# #     return -1


# # target = "Lara"
# # names = sorted(["Tim", "John", "Snow", "KD", "Lara", "Mo", "Selene"])

# # result = binary_search(names, target)
# # if result != -1:
# #     print("{} found at index {}".format(target, result))
# # else:
# #     print("{} not found in the list.".format(target))


# # def binary_search(names, target):
# #     left, right = 0, len(names) - 1 # left is beginning, right is end working backwards

# #     while left <= right: # Left is smaller or equal to right
# #         middle = (left + right) // 2 # Get the middle index

# #         if names[middle] == target:
# #             return middle

# #         elif names[middle] < target: # Smaller than target
# #             left = middle + 1 # Pickup left by 1

# #         elif names[middle] > target: # greater than the target
# #             right = middle - 1 # Minus right by 1

# #     return -1 # If nothing. Return - 1

# # target = "Kashia"
# # names = sorted(["Tim", "John", "Snow", "KD", "Lara", "Mo", "Selene", "Mikyle", "Kashia", "Fourie"]) # Must be a sorted list

# # result = binary_search(names, target)
# # if result != -1:
# #     print("{} found at index {}".format(target, result))
# # else:
# #     print("{} not found in the list.".format(target))


# # def binary_search(arr, target):
# #     left, right = 0, len(arr) - 1

# #     while left <= right:
# #         mid = (left + right) // 2

# #         if arr[mid] == target:
# #             return mid

# #         elif arr[mid] < target:
# #             left = mid + 1

# #         elif arr[mid] > target:
# #             right = mid - 1

# #     return -1


# # target = "Kashia"
# # names = sorted(["Tim", "John", "Snow", "KD", "Lara", "Mo", "Selene",
# #                "Mikyle", "Kashia", "Fourie"])  # Must be a sorted list

# # print(names)
# # result = binary_search(names, target)
# # if result != -1:
# #     print("{} found at index {}".format(target, result))
# # else:
# #     print("{} not found in the list.".format(target))


# # def binary_search(arr, target):
# #     left, right = 0, len(arr) - 1

# #     while left <= right:
# #         mid = (left + right) // 2

# #         if arr[mid] == target:
# #             return mid

# #         elif arr[mid] < target:
# #             left = mid + 1

# #         elif arr[mid] > target:
# #             right = mid - 1

# #     return -1


# # target = "Mikyle"
# # names = sorted(["Tim", "John", "Snow", "KD", "Lara", "Mo", "Selene",
# #                "Mikyle", "Kashia", "Fourie"])  # Must be a sorted list

# # print(names)
# # result = binary_search(names, target)
# # if result != -1:
# #     print("{} found at index {}".format(target, result))
# # else:
# #     print("{} not found in the list.".format(target))


# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1

#     return -1


# target = "Mikyle"
# names = sorted(["Tim", "John", "Snow", "KD", "Lara", "Mo", "Selene",
#                "Mikyle", "Kashia", "Fourie"])  # Must be a sorted list

# print(names)
# result = binary_search(names, target)
# if result != -1:
#     print("{} found at index {}".format(target, result))
# else:
#     print("{} not found in the list.".format(target))

# target = "Mikyle"
# names = sorted(["Tim", "John", "Snow", "KD", "Lara", "Mo", "Selene",
#                "Mikyle", "Kashia", "Fourie"])  # Must be a sorted list

# result = binary_search(names, target)
# if result != -1:
#     print("{} found at index {}".format(target, result))
# else:
#     print("{} not found in the list.".format(target))


# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return - 1


# target = 5
# arr = [1, 3, 4, 5, 5, 6, 7, 8, 9, 9]  # Must be a sorted list

# result = binary_search(arr, target)
# if result != -1:
#     print("{} found at index {}".format(target, result))
# else:
#     print("{} not found in the list.".format(target))
