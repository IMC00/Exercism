def encoded_letter(letter: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    ind = alphabet.find(letter.lower())
    return reversed_alphabet[ind] if ind > -1 else letter

def encode(plain_text):
    encoded_text = ""
    cur_segment = ""
    for character in plain_text:
        if str.isalnum(character):
            cur_segment +=  encoded_letter(character)
        if len(cur_segment) == 5:
            encoded_text += cur_segment + " "
            cur_segment = ""
    return (encoded_text.rstrip() + " " + cur_segment).strip()

def decode(ciphered_text: str):
    return "".join([encoded_letter(letter) for letter in ciphered_text if str.isalnum(letter)])