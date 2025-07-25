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

def value(colors):
    return 10 * COLOUR_MAP[colors[0]] + COLOUR_MAP[colors[1]]

def label(colors):
    main_value = value(colors[:2])
    multiplier = 10 ** COLOUR_MAP[colors[2]]
    resistance = main_value * multiplier

    if resistance >= 10**9:
        return f"{resistance // 10**9} gigaohms"
    elif resistance >= 10**6:
        return f"{resistance // 10**6} megaohms"
    elif resistance >= 10**3:
        return f"{resistance // 10**3} kiloohms"
    else:
        return f"{resistance} ohms"
