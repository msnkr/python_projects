# Get user input
# split the user input into a list
# Get random number based on length of numbers in sentence
# remove word from list based on random number till there are no letters left


import random


user_sentence = input("What do you want to Yoda-fy?: \n")

sentence_list = user_sentence.lower().split()
yoda_list = []

while len(sentence_list) > 0:
    random_num = random.randint(0, len(sentence_list) - 1)
    yoda_list.append(sentence_list[random_num])
    sentence_list.pop(random_num)


print(" ".join(yoda_list))
