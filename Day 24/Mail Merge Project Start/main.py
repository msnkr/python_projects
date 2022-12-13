#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(r'.\Day 24\Mail Merge Project Start\Input\Names\invited_names.txt')as names:
    name_content = names.readlines()


with open(r'.\Day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt')as letter:
    letter_content = letter.read()



for name in name_content:
    with open (f'.\Day 24\Mail Merge Project Start\Output\LettersToSend\{name}.txt', 'w') as name_letter:
        strip_name = name.strip()
        new_letter = letter_content.replace('[name]', strip_name)
        name_letter.write(new_letter)
        


        
