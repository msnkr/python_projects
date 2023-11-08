# Given an integer x, return true if x is a palindrome, and false otherwise.

# def isPalindrome(x):
#     # Special cases
#     if x < 0:
#         return False
#     if x == 0:
#         return True

#     # Convert the integer to a string
#     x_str = str(x)
#     left, right = 0, len(x_str) - 1

#     # Check for palindrome
#     while left < right:
#         if x_str[left] != x_str[right]:
#             return False
#         left += 1
#         right -= 1

#     return True


# print(isPalindrome(23423423423423423))


# def palindromeCheck(x):

#     if x < 0:
#         return False
#     if x == 0:
#         return True

#     x = str(x)

#     left, right = 0, len(x) - 1
#     while left < right:
#         if x[left] != x[right]:
#             return False

#         left += 1
#         right -= 1

#     return True


# print(palindromeCheck(121))
