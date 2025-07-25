def is_valid(isbn: str):
    trimmed = isbn.replace("-","")
    if len(trimmed) != 10: return False
    if not (trimmed[-1].isdigit() or trimmed[-1] == "X"): return False
    if any(not char.isdigit() for char in trimmed[:-1]): return False

    checksum = 10 if trimmed[-1] == "X" else int(trimmed[-1])
    nums = [int(char) for char in trimmed[:-1]]

    return (checksum + sum(num*(10-i) for i,num in enumerate(nums))) % 11 == 0

