# def selection_sort(arr):
#     for i in range(0, len(arr) - 1):
#         idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[idx]:
#                 idx = j
                
#         arr[i], arr[idx] = arr[idx], arr[i]

# arr = [2, 6, 5, 1, 4]

# selection_sort(arr)
# print(arr)

# def selection_sort(arr):
#     # Traverse through all array elements
#     for i in range(len(arr)):
#         # Find the minimum element in remaining unsorted array
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
                
#         # Swap the found minimum element with the first element of the 'unsorted' part of the array
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# # Test the function
# arr = [64, 25, 12, 22, 11]
# selection_sort(arr)
# print ("Sorted array is:", arr)



# def selection_sort(arr):
#     for i in range(len(arr)):
#         idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[idx] > arr[j]:
#                 idx = j

#         arr[i], arr[idx] = arr[idx], arr[i]


# arr = [64, 25, 12, 22, 11]
# selection_sort(arr)
# print(arr)

# def insertion_sort(arr):
#     for i in range(len(arr)):
#         idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[idx] > arr[j]:
#                 arr[idx], arr[j] = arr[j], arr[idx]


# arr = [64, 25, 12, 22, 11]
# insertion_sort(arr)
# print(arr)


# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         idx = i


#         for j in range(i + 1, len(arr)):
#             if arr[idx] > arr[j]:
                
#                 arr[idx], arr[j] = arr[j], arr[idx]


# names = ["Tim", "John", "Snow", "KD", "Lara", "Mo", "Selene"]
# selection_sort(names)

# print("Sorted names:", names)
