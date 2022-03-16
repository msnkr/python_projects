alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encode_text = ''

    for i in text:
        num = alphabet.index(i)
        item = alphabet[num + shift]
        encode_text += item
    print(f'the encoded text is {encode_text}. ')

def decrypt(text, shift):
    decode_text = ''

    for i in text:
        num = alphabet.index(i)
        item = alphabet[num + -shift]
        decode_text += item
    print(f'the decoded text is {decode_text}. ')


if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)