class Matrix:
    def __init__(self, matrix_string : str):
        self.rows = [list(map(lambda x: int(x), row.split(" "))) for row in matrix_string.split("\n")]

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return [self.rows[row][index-1] for row in range(len(self.rows))]
