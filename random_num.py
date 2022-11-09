import random
import PySimpleGUI as sg


sg.theme('DarkAmber')
area_code = '+27'
operator_num = ['84', '78', '76', '71', '73', '74', '64', '62', '81', '61', '82', '72', '79', '63', '60', '83']
random_numbers = []


def get_numbers():
    new_num = ''
    for _ in range(7):
        new_num += str(random.randint(0, 9))
        number = area_code + random.choice(operator_num) + new_num
    random_numbers.append(number)


def save_numbers(file):
    with open(f'{file}.txt', 'w') as f:
        for num in random_numbers:
            f.write(f'{num}\n')


how_many = 'How Many Numbers?: '
name_file = 'What to name the file?: '

layout = [
    [sg.Text(how_many), sg.InputText()],
    [sg.Text(name_file), sg.InputText()],
    [sg.Button('Submit'), sg.Button('Cancel')],
]
window = sg.Window('Bleggh', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        quit()
    elif event == 'Submit':
        value = int(values[0])
        for _ in range(value):
            get_numbers()

    save_numbers(values[1])
    quit()


window.close()