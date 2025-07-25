def create_cipher_dict():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = alphabet[::-1]
    return {letter: rev for letter, rev in zip(alphabet, reversed_alphabet)}

CIPHER_DICT = create_cipher_dict()

def encoded_letter(letter: str) -> str:
    lower_letter = letter.lower()
    return CIPHER_DICT.get(lower_letter, letter) if letter.isalpha() else letter

def encode(plain_text: str) -> str:
    encoded_chars = [encoded_letter(char) for char in plain_text if char.isalnum()]
    return " ".join("".join(encoded_chars[i:i+5]) for i in range(0, len(encoded_chars), 5))

def decode(ciphered_text: str) -> str:
    return "".join(encoded_letter(char) for char in ciphered_text if char.isalnum())
