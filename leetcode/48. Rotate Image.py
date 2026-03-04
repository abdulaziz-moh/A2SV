class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # first transpose
        for i in range(1,n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        # next invese horizontally
        for row in matrix:
            l,r = 0,n-1
            while l<r:
                row[l],row[r] = row[r],row[l]
                l += 1
                r -= 1
        