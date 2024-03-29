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


# def palindrome(x):

#     if x < 0:
#         return False

#     str_x = str(x)
#     left, right = 0, len(str_x) - 1

#     while left < right:
#         if str_x[left] != str_x[right]:
#             return False

#         left += 1
#         right -= 1

#     return True


# print(palindrome(23232323231))


def palindrome_checker(x):
    str_x = str(x)

    left, right = 0, len(str_x) - 1

    while left < right:
        if str_x[left] != str_x[right]:
            return False

        left += 1
        right -= 1

    return True


results = palindrome_checker(1551)
print(results)
