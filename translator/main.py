from tkinter import *


# window = Tk()
# window.title("Translator")

from translate import Translator

def translate_text(text, target_language, source_language):
    translator = Translator(to_lang=target_language, from_lang=source_language)
    translation = translator.translate(text)
    return translation

if __name__ == "__main__":
    source_text = "c’est ce que c’est"
    target_language = "en"
    source_language = "fr"
    
    translated_text = translate_text(source_text, target_language, source_language)
    print(f"Translation: {translated_text}")




# window.mainloop()