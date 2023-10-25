from tkinter import *
from translate import Translator



# window = Tk()
# window.title("Translator")


# window.mainloop()



# translator = Translator(to_lang="zh")
# translation = translator.translate("This is a pen")

# print(translation)


to_lang = input("Language Code?: ")
text_to_translate = input("What do you want to translate?: ")


translator = Translator(to_lang=to_lang)
translation = translator.translate(text_to_translate)

print(translation)