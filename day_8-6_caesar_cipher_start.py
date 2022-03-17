alphabet = ['a', 'b', 'c', 'd', 'r', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
    cipher_text = ''
    for letter in text:
        item = alphabet.index(letter)
        if direction == 'encode':
            cipher_text += alphabet[item + shift]
        elif direction == 'decode':
            cipher_text += alphabet[item - shift]
    print(f'the {direction}d text is {cipher_text}. ')
        

caesar(direction, text, shift)