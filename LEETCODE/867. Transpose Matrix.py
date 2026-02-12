class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        if row == col:
            for i in range(1, row):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix
        else:
            new_mrx = [[0]*row for _ in range(col)]

            for i in range(row):
                for j in range(col):
                    new_mrx[j][i] = matrix[i][j]
            return new_mrx
