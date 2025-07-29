NUMBER_TO_WORD = {
    0: "no",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}

def recite(start, take=1):
    result = []
    def bottle(i): return "bottle" if i == 1 else "bottles"
    for i in range(start, start-take, -1):
        result.append(f"{NUMBER_TO_WORD[i].capitalize()} green {bottle(i)} hanging on the wall,")
        result.append(f"{NUMBER_TO_WORD[i].capitalize()} green {bottle(i)} hanging on the wall,")
        result.append(f"And if one green bottle should accidentally fall,")
        result.append(f"There'll be {NUMBER_TO_WORD[i-1]} green {bottle(i-1)} hanging on the wall.")
        if i != start-take+1:
            result.append("")
    return result
