from PyDictionary import PyDictionary

dictionary = PyDictionary()
word = input("What word do you want to check?: ")

dict_word = dictionary.meaning(word)

for x in dict_word:
    print(x, dict_word[x])
