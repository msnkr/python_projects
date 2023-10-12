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
# def count_sheeps(arrayOfSheeps):
#     return arrayOfSheeps.count(True)


# def spin_words(sentence):
#     new_sentence = ""
#     words = sentence.split(" ")
#     if len(words) >= 1:
#         for word in words:
#             if len(word) >= 5:
#                 new_sentence += word[::-1]
#             else:
#                 new_sentence += word
#             new_sentence += " "

#     return new_sentence.strip()


# print(spin_words("Hey fellow warriors"))


# data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]


# def open_or_senior(data):
#     for member in data:
#         if member[0] > 55 and member[1] > 7:
#             pass


# print(open_or_senior(data))

seq = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]


def find_it(seq):
    highest_num = 0

    for num in seq:
        num_item = seq.count(num)

        if num_item > highest_num:
            highest_num = num_item

    if highest_num % 2 == 0:
        print("Even")
    else:
        print("odd")


find_it(seq)
