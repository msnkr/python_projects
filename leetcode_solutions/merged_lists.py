# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# # Function to merge two sorted lists
# def merged_lists(l1, l2):
#     # Initialize a new list
#     merged_list = []

#     # While both lists have elements
#     while l1 and l2:
#         # If the first element of list1 is smaller
#         if l1[0] < l2[0]:
#             # Add it to the merged list
#             merged_list.append(l1.pop(0))
#         else:
#             # Otherwise, add the first element of list2
#             merged_list.append(l2.pop(0))

#     # If there are remaining elements in either list, add them to the merged list
#     merged_list.extend(l1 if l1 else l2)

#     return merged_list


# Assumes the list is already sorted
# list1, list2 = [1, 2, 4], [1, 3, 4]
# results = merged_lists(list1, list2)
# print(results)

# def merged_lists(arr1, arr2):
#     merged_list = []

#     while arr1 and arr2:
#         if arr1[0] < arr2[0]:
#             merged_list.append(arr1.pop(0))
#         else:
#             merged_list.append(arr2.pop(0))

#     merged_list.extend(arr1 if arr1 else arr2)

#     return merged_list


# list1, list2 = [1, 2, 4], [1, 3, 4]
# results = merged_lists(list1, list2)
# print(results)


# def merged_lists(arr1, arr2):
#     merged_list = []

#     while arr1 and arr2:
#         if arr1[0] < arr2[0]:
#             merged_list.append(arr1.pop(0))
#         else:
#             merged_list.append(arr2.pop(0))

#     merged_list.extend(arr1 if arr1 else arr2)

#     return merged_list


# list1, list2 = [1, 2, 4], [1, 3, 4]
# results = merged_lists(list1, list2)
# print(results)


def merged_lists(arr1, arr2):

    merged_list = []

    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            merged_list.append(arr1.pop(0))
        else:
            merged_list.append(arr2.pop(0))

    merged_list.extend(arr1 if arr1 else arr2)
    return merged_list


list1, list2 = sorted([1, 5, 2, 4]), sorted([1, 3, 4, 7])
results = merged_lists(list1, list2)
print(results)
