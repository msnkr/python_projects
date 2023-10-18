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


# data = [(14, 14), (48, 21), (54, 12), (72, 7)]


# def open_or_senior(data):
#     return ["Senior" if age > 55 and handicap > 7 else "Open" for age, handicap in data]


# print(open_or_senior(data))

# seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]


# def find_it(seq):
#     highest_num = 0
#     for number in seq:
#         new_num = seq.count(number)

#         if new_num > highest_num and new_num % 2 != 0:
#             another_num = number

#     return another_num


# print(find_it(seq))

# Solution

# seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]


# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 != 0:
#             return i


# print(find_it(seq))

# sentence = "4of Fo1r pe6ople g3ood th5e the2"


# def order(sentence):
#     spit_sentence = sentence.split(" ")


# order(sentence)

# x = ["Ryan", "Kieran", "Mark",]


# def friend(x):
#     return [name for name in x if len(name) == 4]


# friend(x)

# def get_middle(s):
#     if len(s) %2 == 0:
#         text = s[len(s) // 2]

#     print(text)

# get_middle("test")


# def xo(s):
#     s = s.lower()
#     return True if s.count("x") == s.count("o") else False


# print(xo("ooOxx"))

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# def create_phone_number(n):
#     new_n = ""
#     for new in n:
#         new_n += str(new)

#     return "({}) {}-{}".format(new_n[:3], new_n[3:6], new_n[6:])

# def create_phone_number(n):
# 	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# print(create_phone_number(n))

# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"

# print(bool_to_word(False))

# def tower_builder(n_floors):
#     # build here


# tower_builder(2)

# def find_missing_letter(chars):
#     alphabet = [chr(letter) for letter in range(97, 123)]
#     return 

# print(find_missing_letter(['a','b','c','d','f']))


def high_and_low(numbers):
    numbers = numbers.split()
    n = [int(num) for num in numbers]

    highest = 0
    lowest = 1
    for num in n:
        if num > highest:
            highest = num
        elif num <= lowest:
            lowest = num

    return "{} {}".format(highest, lowest)

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))