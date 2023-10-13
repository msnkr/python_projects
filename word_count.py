def word_counter():
    letters = input("Enter the words: ")
    print(f"This many characters in what you entered: {len(letters)}")

    words = letters.split(" ")
    print(f"This many words in what you entered: {len(words)}")


word_counter()
