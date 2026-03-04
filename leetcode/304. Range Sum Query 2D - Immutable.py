from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
                
        if matrix:
            row,col = len(matrix), len(matrix[0])
        else:
            row,col = 0,0
        self.prefixsum2d = [[0]*col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if i > 0 and j > 0:
                    self.prefixsum2d[i][j] = matrix[i][j] + self.prefixsum2d[i-1][j] + self.prefixsum2d[i][j-1] - self.prefixsum2d[i-1][j-1]
                else:
                    if i == 0 and j == 0:
                        self.prefixsum2d[i][j] = matrix[i][j]
                    elif i == 0:
                        self.prefixsum2d[i][j] = matrix[i][j] + self.prefixsum2d[0][j-1]
                    elif j == 0:
                        self.prefixsum2d[i][j] = matrix[i][j] + self.prefixsum2d[i-1][0]
                        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            ans = self.prefixsum2d[row2][col2] - self.prefixsum2d[row2][col1 - 1] - self.prefixsum2d[row1 -1 ][col2] + self.prefixsum2d[row1 - 1][col1 - 1]
        else:
            if row1 == 0 and col1 == 0:
                ans = self.prefixsum2d[row2][col2]
            elif row1 == 0:
                ans = self.prefixsum2d[row2][col2] - self.prefixsum2d[row2][col1 - 1]
            elif col1 == 0:
                ans = self.prefixsum2d[row2][col2] - self.prefixsum2d[row1 -1 ][col2]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)