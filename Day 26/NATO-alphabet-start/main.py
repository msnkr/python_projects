# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv('./Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Get the input into a variable.
# Convert each letter in variable into a list using split or splitlines.
user_input = list(input('Enter Word: ').lower())
# Loop thorough each item in the variable list to print out the letters associated with the dictionary

