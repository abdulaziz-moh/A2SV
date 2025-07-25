class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        ans = [[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                ans[j][i] = matrix[i][j]
        return ans
    
obj = Solution()
matrix = [[1,2],[4,5],[7,8]]
print(obj.transpose(matrix))