def rows(letter):
    size = ord(letter) - ord("A")
    result = [f"{' '*(size)}A{' '*(size)}"]
    for index in range(0, size):
        result.append(f"{' '*(size-index-1)}{chr(ord('A')+index+1)}{' '*(1+2*index)}{chr(ord('A')+index+1)}{' '*(size-index-1)}")
    return result + list(reversed(result[:-1]))

