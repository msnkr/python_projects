# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")


from audioop import add


name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
counter1 = 0
counter2 = 0

true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']

for i in name1.lower():
    if i in true:
        counter1 += 1

for i in name2.lower():
    if i in true:
        counter1 += 1

for i in name1.lower():
    if i in love:
        counter2 += 1

for i in name2.lower():
    if i in love:
        counter2 += 1


love_counter = str(counter1) + str(counter2)

if int(love_counter) < 10 or int(love_counter) > 90:
    print(
        f'Your score is {love_counter}. You got together like Coke and Mentos!')
elif int(love_counter) >= 40 and int(love_counter) <= 50:
    print(f'Your score is {love_counter}. You are alright together.')
else:
    print(f'Your score is {love_counter}.')
