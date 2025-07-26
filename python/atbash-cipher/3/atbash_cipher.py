def encoded_letter(letter: str):
    reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    return reversed_alphabet[ord(letter.lower()) - ord('a')] if str.isalpha(letter) else letter

def encode(plain_text):
    encoded_text = []
    cur_segment = ""
    for character in plain_text:
        if str.isalnum(character):
            cur_segment +=  encoded_letter(character)
        if len(cur_segment) == 5:
            encoded_text.append(cur_segment)
            cur_segment = ""
    if cur_segment: encoded_text.append(cur_segment)
    return " ".join(encoded_text)

def decode(ciphered_text: str):
    return "".join([encoded_letter(letter) for letter in ciphered_text if str.isalnum(letter)])
