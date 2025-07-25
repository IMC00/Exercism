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
        line = input_grid[i:i+4]
        for char in line:
            if len(char) % 3 != 0: raise ValueError("Number of input columns is not a multiple of three")
        j = 0
        size_line = len(line[0])

        while j < size_line:
            char = [line[k][j:j+3] for k in range(4)]
            solution += process_character(char)
            j += 3
        i += 4
        solution += ","

    return solution[:-1]