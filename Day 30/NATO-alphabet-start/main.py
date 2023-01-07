import pandas


{"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv('./Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

def generate_phonetic():
    try:
        user_input = input('Enter Word: ').upper()
        if user_input != 'EXIT':
            nato_words = [nato_dict[letter] for letter in user_input]
            print(nato_words)
    except KeyError:
        print('Please only use words in the alphabet.')
        generate_phonetic()

generate_phonetic()