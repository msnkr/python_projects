from PyDictionary import PyDictionary
from termcolor import colored

dictionary = PyDictionary()


flag = True
while flag:
    word = input("What word do you want to check?: ")

    if word != 'q':
        dict_word = dictionary.meaning(word)

        for x in dict_word:
            print(colored(x, "green"))
            print(colored(" ".join(dict_word[x]), "blue"))

        print("=" * 200)

    else:
        print("Goodbye!")
        flag = False
