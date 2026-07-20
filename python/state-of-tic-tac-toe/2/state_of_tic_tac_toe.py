def gamestate(board):
    is_board_full = True
    x_number = 0
    o_number = 0

    x_won = False
    o_won = False

    # Check win
    ## Rows
    for row in range(3):
        symb = board[row][row]
        is_line_row = True
        is_line_col = True

        for col in range(3):
            x_number = x_number + (1 if board[row][col] == "X" else 0)
            o_number = o_number + (1 if board[row][col] == "O" else 0)

            if board[row][col] != " ":
                is_line_row = is_line_row and board[row][col] == symb
            else:
                is_line_row = False
                is_board_full = False

            if board[col][row] != " ":
                is_line_col = is_line_col and board[col][row] == symb
            else:
                is_line_col = False
                is_board_full = False

        if is_line_col or is_line_row:
            if symb == "X":
                x_won = True
            else:
                o_won = True

    if x_number - o_number > 1:
        raise ValueError("Wrong turn order: X went twice")

    if o_number > x_number:
        raise ValueError("Wrong turn order: O started")
    # Check diagonals
    mid_symb = board[1][1]
    is_line_diag = False
    if mid_symb != " ":
        is_line_diag = board[0][0] == mid_symb and board[2][2] == mid_symb
        is_line_diag = is_line_diag or (board[2][0] == mid_symb and board[0][2] == mid_symb)

    if is_line_diag:
        if mid_symb == "X":
            x_won = True
        else:
            o_won = True

    if x_won and o_won:
        raise ValueError("Impossible board: game should have ended after the game was won")

    if x_won ^ o_won:
        return "win"

    return "draw" if is_board_full else "ongoing"
