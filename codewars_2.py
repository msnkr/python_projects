# queue = ["sheep", "sheep", "sheep", "sheep", "sheep", "wolf", "sheep", "sheep"]
# # queue = ["sheep", "sheep", "wolf"]


# def warn_the_sheep(queue):
#     if queue[::-1][0] == "wolf":
#         print("Pls go away and stop eating my sheep")
#     else:
#         for index, animal in enumerate(queue[::-1]):
#             if animal == "wolf":
#                 print(
#                     f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")


# warn_the_sheep(queue)


# def feast(beast, dish):
#     if beast[0] == dish[0] and beast[-1] == dish[-1]:
#         return True
#     else:
#         return False


# feast('chickadee', "chocolate cake")

# Solution
# def feast(beast, dish):
#     return beast[0]==dish[0] and dish[-1]==beast[-1]


# def even_or_odd(number):
#     return 'Odd' if number % 2 else 'Even'


# print(even_or_odd(8))


# def count_sheeps(array_of_sheep):
#   count = 0
#   for sheep in array_of_sheep:
#       if sheep:
#           count += 1
#   return count

# Solution
def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)
