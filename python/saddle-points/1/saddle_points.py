import sys

def saddle_points(matrix):
    min_column = {}
    max_row = {}

    n_rows = len(matrix)
    if n_rows == 0:
        return []

    n_cols = len(matrix[0])

    for row in range(n_rows):
        if len(matrix[row]) != n_cols:
            raise ValueError("irregular matrix")

        for col in range(n_cols):
            elem = matrix[row][col]
            min_column[col] = min(elem, min_column.get(col, sys.maxsize))
            max_row[row] = max(elem, max_row.get(row, 0))

    result = []
    for row in range(n_rows):
        for col in range(n_cols):
            elem = matrix[row][col]
            if min_column[col] == elem and max_row[row] == elem:
                result.append({"row": row+1, "column": col+1})

    return result
