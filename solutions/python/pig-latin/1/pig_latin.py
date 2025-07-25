def translate_word(text: str):
    vowels = {"a", "e", "i", "o", "u"}
    if text[0] in vowels or text[0:2] in {"yt", "xr"}:
        return text + "ay"

    # Case 3: Looking for qu
    for i,x in enumerate(text):
        if x in vowels:
            break
        if x == 'q' and text[i+1] == 'u':
            return text[i+2:] + text[:i+2] + "ay"

    # Case 4: Looking for y
    for i,x in enumerate(text):
        if i == 0: continue
        if x in vowels:
            break
        if x == 'y':
            return text[i:] + text[:i] + "ay"

    # Case 2: Moving consonants
    for i,x in enumerate(text):
        if x in vowels:
            return text[i:] + text[:i] + "ay"

def translate(text: str):
    return " ".join([translate_word(word) for word in text.split()])