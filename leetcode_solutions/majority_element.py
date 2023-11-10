# def majorityElement(nums):
#     # Initialize variables to keep track of the majority element and its count.
#     # Initialize the majority_element with the first element.
#     majority_element = nums[0]
#     # Initialize the count to 1, as we've seen one occurrence of the majority_element so far.
#     count = 1

#     # Iterate through the array.
#     # Start from the second element and go up to the end of the array.
#     for i in range(1, len(nums)):
#         if count == 0:
#             # If the count reaches 0, we've canceled out all previous elements, so update the majority_element.
#             majority_element = nums[i]
#             count = 1
#         elif majority_element == nums[i]:
#             # If the current element is the same as the majority_element, increment the count.
#             count += 1
#         else:
#             # If the current element is different from the majority_element, decrement the count.
#             count -= 1

#     # After iterating through the entire array, the majority_element will be the majority element.
#     return majority_element


# nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# result = majorityElement(nums)
# print("The majority element is:", result)


# def majorityElement(arr):
#     count = 1
#     majority_element = arr[0]

#     for x in range(1, len(arr)):
#         if count == 0:
#             majority_element = arr[x]
#             count = 1
#         elif majority_element == arr[x]:
#             count + 1
#         else:
#             count -= 1

#     return majority_element


# nums = [3, 1, 1, 3, 4, 1, 1, 2, 4]
# result = majorityElement(nums)
# print("The majority element is:", result)


# def majorityElement(arr):
#     count = 1
#     majority_element = arr[0]

#     for x in range(1, len(arr)):
#         if count == 0:
#             majority_element = arr[x]
#             count = 1
#         elif majority_element == arr[x]:
#             count += 1
#         else:
#             count -= 1

#     return majority_element


# nums = [3, 1, 1, 3, 4, 1, 1, 2, 4]
# result = majorityElement(nums)
# print("The majority element is:", result)
