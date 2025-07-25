COLOUR_MAP = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

TOLERANCE_MAP = {
    "grey"      : "±0.05%",
    "violet"    : "±0.1%",
    "blue"      : "±0.25%",
    "green"     : "±0.5%",
    "brown"     : "±1%",
    "red"       : "±2%",
    "gold"      : "±5%",
    "silver"    : "±10%",
}

def value(colors):
    if len(colors) == 2:
        return 10 * COLOUR_MAP[colors[0]] + COLOUR_MAP[colors[1]]
    else:
        return 100 * COLOUR_MAP[colors[0]] + 10* COLOUR_MAP[colors[1]] + COLOUR_MAP[colors[2]]


def label(colors):
    if len(colors) == 3:
        main_value = value(colors[:2])
        multiplier = 10 ** COLOUR_MAP[colors[2]]
    else:
        main_value = value(colors[:3])
        multiplier = 10 ** COLOUR_MAP[colors[3]]

    resistance = main_value * multiplier

    if resistance >= 10**9:
        return f"{resistance / 10**9 if int(resistance / 10**9) != resistance / 10**9 else int(resistance / 10**9) } gigaohms"
    elif resistance >= 10**6:
        return f"{resistance / 10**6 if int(resistance / 10**6) != resistance / 10**6 else int(resistance / 10**6)} megaohms"
    elif resistance >= 10**3:
        return f"{resistance / 10**3 if int(resistance / 10**3) != resistance / 10**3 else int(resistance / 10**3)} kiloohms"
    else:
        return f"{resistance} ohms"

def resistor_label(colors):
    if len(colors) == 1: return "0 ohms"
    elif len(colors) == 4:
        return f"{label(colors[:3])} {TOLERANCE_MAP[colors[3]]}"
    else:
        return f"{label(colors[:4])} {TOLERANCE_MAP[colors[4]]}"

