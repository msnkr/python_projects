# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv('./Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

game = True
while game:
    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    # Get the input into a variable.
    # Convert each letter in variable into a list using split or splitlines.

    user_input = input('Enter Word: ').upper()
    if user_input == 'EXIT':
        break

    # Loop thorough each item in the variable list to print out the letters associated with the dictionary

    nato_words = [nato_dict[letter] for letter in user_input]
    print(nato_words)