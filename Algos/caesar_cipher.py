import string

def caesar_cipher(text: str, shift: int):
    result = ''
    
    for char in text:
        if char.isupper():
            alphabet = string.ascii_uppercase
        elif char.islower():
            alphabet = string.ascii_lowercase
        else:
            result += char
        index = (alphabet.index(char) + shift) % len(alphabet)
        result += alphabet[index]
    
    return result

print(caesar_cipher('aaaasss', 3))