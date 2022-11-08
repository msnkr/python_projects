import random

area_code = '+27'
operator_num = ['84', '78', '76', '71', '73', '74', '64', '62', '81', '61', '82', '72', '79', '63', '60', '83']
random_numbers = []

how_many = int(input('How many?: '))
name_file = input('What to name the file?: ')
# work with net

def get_numbers():
    new_num = ''
    for _ in range(7):
        new_num += str(random.randint(0, 9))
        number = area_code + random.choice(operator_num) + new_num
    random_numbers.append(number)


def save_numbers():
    with open(f'{name_file}.txt', 'w') as f:
        for num in random_numbers:
            f.write(f'{num}\n')


for _ in range(how_many - 1):
    get_numbers()

save_numbers()
        
