from tkinter import *
from translate import Translator


language_codes = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Russian": "ru",
    "Italian": "it",
    "Dutch": "nl",
    "Portuguese": "pt",
    "Swedish": "sv",
    "Korean": "ko",
    "Greek": "el",
    "Turkish": "tr",
    "Hindi": "hi",
    "Bengali": "bn",
    "Vietnamese": "vi",
    "Thai": "th",
    "Polish": "pl",
}



# def get_language_code(language):
#     return language


# def show_menu():
#     menu.post(menu_btn.winfo_rootx(), menu_btn.winfo_rooty() + menu_btn.winfo_height())


# window = Tk()
# window.title("Translator")
# window.geometry("600x400")


# clicked = StringVar()
# clicked.set("English")


# language_label = Label(window, text="What language do you want to use?")
# language_label.grid(column=0, row=0)
# language_label.config(padx=10, pady=20, font=("Arial", 16, "bold"))


# menu = Menu(window, tearoff=0)
# for key in language_codes:
#     menu.add_command(label=key, command=lambda language = key: get_language_code(language))


# menu_btn = Button(window, text="Menu", command=show_menu)
# menu_btn.grid(column=1, row=0)


# text_label = Label(window, text="What do you want to translate?: ")
# text_label.grid(column=0, row=1)

# text_entry = Entry(window, width=50)
# text_entry.grid(column=0, row=2)

# translate_btn = Button(window, text="Translate", command=translate_machine)
# translate_btn.grid(column=0, row=3)


# window.mainloop()


# def translate_machine(code, text):
#     translator = Translator(to_lang=code)
#     translation = translator.translate(text)

#     return translation


# def main():
#     to_lang = input("What language do you want to use? ").capitalize()
#     text_to_translate = input("What do you want to translate?: ")

#     if to_lang in language_codes:
#         value = language_codes[to_lang]

#         translate_machine(value, text_to_translate)
#     else:
#         print("That language doesn't exist. Try again")
#         main()



# if __name__=="__main__":
#     main()

# Get text from english textbox, get option from languiage mene, when translate is cliked, put new text in language text

def translate(language):
    to_translate = english_text.get("1.0", "end-1c")

    
    translator = Translator(to_lang=language_codes[language])
    translation = translator.translate(to_translate)

    translated_text.insert("end", translation)



def show_menu():
    translated_text.delete("1.0", "end-1c")
    menu.post(menu_btn.winfo_rootx(), menu_btn.winfo_rooty() + menu_btn.winfo_height())


window = Tk()

window.title("Translator App")
window.config(padx=20, pady=20)
window.geometry("600x400")

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)

english_label = Label(window, text="English")
english_label.grid(column=0, row=0)
english_label.config(font=("Arial", 22, "bold"))

english_text = Text(window, width=30, height=10)
english_text.grid(column=0, row=1)


menu = Menu(window, tearoff="0")
for language in language_codes:
    menu.add_command(label=language, command=lambda key = language: translate(key))

menu_btn = Button(window, text="English", command=show_menu)
menu_btn.grid(column=2, row=0)
menu_btn.config(font=("Arial", 22, "bold"))

menu_item = StringVar()
menu_item.set("English")

translated_text = Text(window, width=30, height=10)
translated_text.grid(column=2, row=1)


window.mainloop()