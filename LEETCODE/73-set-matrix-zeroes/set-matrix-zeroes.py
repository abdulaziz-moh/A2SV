class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        rowset = set()
        colset = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowset.add(i)
                    colset.add(j)
        for i in range(row):
            if i in rowset:
                for j in range(col):
                    matrix[i][j] = 0
            else:
                for j in colset:
                    matrix[i][j] = 0