# # Define a function named merge_sort that takes an array 'arr' as input
# def merge_sort(arr):
#     # Check if the length of the array is greater than 1 (i.e., if it can be split further)
#     if len(arr) > 1:
#         # Split the array into two halves: left_arr and right_arr
#         left_arr = arr[:len(arr)//2]
#         right_arr = arr[len(arr)//2:]

#         # Recursively call merge_sort on the left and right halves
#         merge_sort(left_arr)
#         merge_sort(right_arr)

#         # Initialize three pointers, i, j, and k
#         i = 0  # Pointer for left_arr
#         j = 0  # Pointer for right_arr
#         k = 0  # Pointer for the main array 'arr'

#         # Merge the two halves into the main array in sorted order
#         while i < len(left_arr) and j < len(right_arr):
#             # Compare elements from left_arr and right_arr
#             if left_arr[i] < right_arr[j]:
#                 # If the element from left_arr is smaller, put it in 'arr'
#                 arr[k] = left_arr[i]
#                 i += 1
#             else:
#                 # If the element from right_arr is smaller, put it in 'arr'
#                 arr[k] = right_arr[j]
#                 j += 1
#             k += 1  # Move the main array pointer

#         # Handle any remaining elements in left_arr (if any)
#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1

#         # Handle any remaining elements in right_arr (if any)
#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1


# # Create a test array
# arr_test = [2, 4, 1, 5, 8, 7, 5, 8, 5, 3, 8, 9, 4, 0]

# # Call the merge_sort function to sort the test array in-place
# merge_sort(arr_test)

# # Print the sorted array
# print(arr_test)


# def merge_sort(arr):
#     if len(arr) > 1:
#         left_arr = arr[:len(arr) // 2]
#         right_arr = arr[len(arr) // 2:]

#         merge_sort(left_arr)
#         merge_sort(right_arr)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] < right_arr[j]:
#                 arr[k] = left_arr[i]
#                 i += 1
#             else:
#                 arr[k] = right_arr[j]
#                 j += 1

#             k += 1

#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1

#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1


# # Create a test array
# arr_test = [2, 4, 1, 5, 8, 7, 5, 8, 5, 3, 8, 9, 4, 0]

# # Call the merge_sort function to sort the test array in-place
# merge_sort(arr_test)

# # Print the sorted array
# print(arr_test)


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0


# Create a test array
arr_test = [2, 4, 1, 5, 8, 7, 5, 8, 5, 3, 8, 9, 4, 0]

# Call the merge_sort function to sort the test array in-place
merge_sort(arr_test)

# Print the sorted array
print(arr_test)
