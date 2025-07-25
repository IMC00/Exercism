from itertools import chain

def number_encode(number):
    remaining = bin(number)[2:]
    segments = ["0" + remaining[-7:].rjust(7, "0")]
    remaining = remaining[:-7]

    while remaining:
        segments.append("1" + remaining[-7:].rjust(7, "0"))
        remaining = remaining[:-7]

    return [int(x, 2) for x in reversed(segments)]

def encode(numbers):
    return list(chain(*[number_encode(number) for number in numbers]))

def decode(bytes_):
    print()
    result = []
    current = ""
    for byte in bytes_:
        formatted_byte = bin(byte)[2:].rjust(8, "0")
        current += formatted_byte[1:]
        if formatted_byte[0] == "0":
            result.append(int(current, 2))
            current = ""
    if current != "":
        raise ValueError("incomplete sequence")

    return result
