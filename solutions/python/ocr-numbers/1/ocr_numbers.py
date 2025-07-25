NUMBERS = {
    "".join([" _ ", "| |", "|_|", "   "]): "0",
    "".join(["   ", "  |", "  |", "   "]): "1",
    "".join([" _ ", " _|", "|_ ", "   "]): "2",
    "".join([" _ ", " _|", " _|", "   "]): "3",
    "".join(["   ", "|_|", "  |", "   "]): "4",
    "".join([" _ ", "|_ ", " _|", "   "]): "5",
    "".join([" _ ", "|_ ", "|_|", "   "]): "6",
    "".join([" _ ", "  |", "  |", "   "]): "7",
    "".join([" _ ", "|_|", "|_|", "   "]): "8",
    "".join([" _ ", "|_|", " _|", "   "]): "9",

}

def process_character(character):
    potential_char = "".join(character)
    return NUMBERS[potential_char] if potential_char in NUMBERS else "?"

def convert(input_grid):
    size_grid = len(input_grid)
    if size_grid % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    solution = ""
    i = 0
    while i < size_grid:
        character = input_grid[i:i+4]
        for line in character:
            if len(line) % 3 != 0: raise ValueError("Number of input columns is not a multiple of three")
        j = 0
        size_line = len(character[0])

        while j < size_line:
            solution += process_character([character[0][j:j+3],character[1][j:j+3],character[2][j:j+3],character[3][j:j+3]])
            j += 3
        i += 4
        solution += ","

    return solution[:-1]