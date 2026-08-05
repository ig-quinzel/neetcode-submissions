class NumMatrix:

    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        self.pre = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.pre[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.pre[r][c + 1]
                    + self.pre[r + 1][c]
                    - self.pre[r][c]
                )

    def sumRegion(self, row1, col1, row2, col2):

        return (
            self.pre[row2 + 1][col2 + 1]
            - self.pre[row1][col2 + 1]
            - self.pre[row2 + 1][col1]
            + self.pre[row1][col1]
        )