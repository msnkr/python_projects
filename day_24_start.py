# with open('day_24_text.txt')as file:
#     contents = file.read()

# print(contents)

with open('day_24_text.txt', 'a')as f:
    greeting = '\nHello. It\'s nearly Christmas'
    f.write(greeting)
