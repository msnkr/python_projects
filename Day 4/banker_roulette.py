# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

convert_to_num = len(names)

rand_name = random.randint(0, convert_to_num -1)

print(f'{names[rand_name]} will pay for dinner.')