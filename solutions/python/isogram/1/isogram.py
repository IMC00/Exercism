from string import ascii_lowercase
def is_isogram(string: str):
    s = string.lower()
    result = set()
    for char in s:
        if char in ascii_lowercase:
            if char in result:
                return False
            else:
                result.add(char)

    return True