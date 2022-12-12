#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('Day 24/Mail Merge Project Start/Input/Names/invited_names.txt')as file:
    names_list = file.readlines()

with open('Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt')as file:
    letter = file.read()

for name in names_list:
    with open(f'Day 24/Mail Merge Project Start/Output/ReadyToSend/{name}.txt', 'w')as file:
        new_name = name.rstrip()
        file.write(letter.replace('[name]', new_name))