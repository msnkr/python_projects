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


# x = ["Ryan", "Kieran", "Mark",]


# def friend(x):
#     return [name for name in x if len(name) == 4]


# friend(x)

# def get_middle(s):
#     num = len(s)
#     if num % 2 == 0:
#         return "{}{}".format(s[num // 2 - 1],s[num // 2])
#     else:
#         return "{}".format(s[num  // 2])

# print(get_middle("testing"))


# def get_middle(s):
#     num = len(s)
#     return "{}{}".format(s[num // 2 - 1],s[num // 2]) if num % 2 == 0 else "{}".format(s[num  // 2])

# print(get_middle("test"))


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
#     pass


# tower_builder(6)


# def find_missing_letter(chars):
#     alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
#     new_list = alphabet[alphabet.index(chars[0]): alphabet.index(chars[0]) + len(chars) + 1]

#     x = [x for x in new_list if x not in chars]
#     return "".join(x)

# print(find_missing_letter(['O','Q','R','S']))

# ######################### SOLUTION
# def find_missing_letter(chars):
#     n = 0
#     while ord(chars[n]) == ord(chars[n+1]) - 1:
#         n += 1
#     return chr(1+ord(chars[n]))

# def high_and_low(numbers):
#     nums = [int(num) for num in numbers.split()]
#     return "{} {}".format(sorted(nums)[-1], sorted(nums)[0])

# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


# def filter_list(l):
#     'return a new list with the strings filtered out'
#     return [i for i in l if type(i) == int]

# print(filter_list([1, 2, 'a', 'b']))

# def filter_list(l):
#   'return a new list with the strings filtered out'
#   return [x for x in l if type(x) is not str]

# print(filter_list([1, 2, 'a', 'b']))

# return masked string
# def maskify(cc):
#     if len(cc) >= 4:
#         length = len(cc) - 4
#         return "#" * length + cc[length:]
#     else:
#         return cc


# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]

# print(maskify("SF$SDfgsd2eA"))


# def generate_hashtag(s):
#     if s != "":
#         sentence = ""
#         for word in s.split():
#             sentence += word.capitalize()

#         if len(sentence) < 140 or "":
#             return "#{}".format(sentence)
#         else:
#             return False
#     else:
#         return False


# print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))

# def generate_hashtag(s):
#     output = "#"
#     for word in s.split():
#         output += word.capitalize()

#     return False if (len(s) == 0 or len(output) > 140) else output


# print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))

# ################################## DANG!

# def to_camel_case(text):
#     removed = text.replace("_", " ").replace("-", " ").split()
#     if len(removed) == 0:
#         return ""
#     else:
#         return removed[0] + "".join([x.capitalize() for x in removed[1:]])


# print(to_camel_case("the_stealth-warrrior"))


# def solution(s):
#     pass

# solution('asdfads')


# def capitals(word):
# for index, x in enumerate(word):
#     if x == x.upper():
#         new_list.append(index)

# return new_list
# return [index for index, x in enumerate(word)  if x == x.upper()]


# print(capitals("CodEWaRs"))


# def find_smallest_int(arr):
#     return sorted(arr)[0]

# print(find_smallest_int([34, -345, -1, 100]))


# def likes(names):
#     # your code here
#     if len(names) >= 4:
#         return "{}, {} and {} others like this".format(names[0], names[1], len(names[2:]))
#     elif len(names) == 3:
#         return "{}, {} and {} like this".format(*names)
#     elif len(names) == 2:
#         return "{} and {} like this".format(*names)
#     elif len(names) == 1:
#         return "{} likes this".format(*names)
#     else:
#         return "No one likes this"

# print(likes(['Alex']))

# def likes(names):
#     n = len(names)
#     return {
#         0: "no one like this",
#         1: "{} like this",
#         2: "{} and {} like this",
#         3: "{}, {} and {} like this",
#         4: "{}, {} and {} others like this"
#     }[min(4, n)].format(*names[:3], others=n-2)

# print(likes(["Jacob", "Mark", "Steve", "Lara"]))


# def array_diff(a, b):
#     pass

# print(array_diff([1,2,2,2,3],[2]))


# def remove_url_anchor(url):
#     # TODO: complete
#     return url.split("#")[0]

# print(remove_url_anchor("www.codewars.com#about"))


# def gimme(input_array):
#     # Implement this function
#     return input_array.index(sorted(input_array)[1])

# print(gimme([5, 10, 14]))

# sentence = "4of Fo1r pe6ople g3ood th5e the2"


# def order(sentence):
#     numbers = range(1, len(sentence) + 1)
#     new_sentence = sentence.split()
#     sentence = ""

#     for num in numbers:
#         for word in new_sentence:
#             if str(num) in word:
#                 sentence += "{} ".format(word)

#     return sentence.strip()

# print(order(sentence))


# sentence = "4of Fo1r pe6ople g3ood th5e the2"


# def order(sentence):
#     result = [word for num in range(1, len(sentence.split()) + 1) for word in sentence.split() if str(num) in word]
#     return " ".join(result)

# order(sentence)

# def order(sentence):
#   return " ".join(sorted(sentence.split(), key=min))


# fruits = ["banana4", "3apple", "ora1nge", "mang4o", "gua2va"]

# print(" ".join(sorted(fruits, key=min)))


# def duplicate_count(text):
#     for x in text.lower():
#         letters = text.find(x)

#     print(letters)

# duplicate_count("aabbccc")

# def explode(arr):
#     x = [x for x in arr if isinstance(x, int)]
#     return ["Void!" if x == [] else [arr] * sum(x)]

# print(explode(["a", 3]))


# def explode(arr):
#     x = [x for x in arr if isinstance(x, int)]
#     return [arr] * sum(x) if x else "Void!"


# print(explode(["a", 3]))


# def find_outlier(n):
#     pass

# find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])

# def high(x):
#     # Code here
#     alphabet = "abcdefghijklmnopqrstuvwxyz"

#     score, total_score = 0, 0
#     largest_word = ""
#     for word in x.split():
#         for letter in word:
#             score += alphabet.index(letter) + 1

#         if score > total_score:
#             total_score = score
#             largest_word = word

#         score = 0

#     return largest_word


# high("man i need a taxi up to ubud")


# def litres(time):
#     return time // 2


# print(litres(1787))

def unique_in_order(sequence):
    i = 0
    j = 1
    k = []

    if len(sequence) > 1:
        while j < len(sequence):
            if sequence[i] != sequence[j]:
                k.append(sequence[i])
            i += 1
            j += 1

        k.append(sequence[j - 1])
    return k


print(unique_in_order('ABBCcAD'))
