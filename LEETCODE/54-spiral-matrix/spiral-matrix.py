class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        i, limit = 0, row*col

        while True:
            for j in range(i,col-i):
                ans.append(matrix[i][j])
            if len(ans) == limit: break

            for j in range(i+1,row-i):
                ans.append(matrix[j][col-i-1])
            if len(ans) == limit: break

            for j in range(col-i-2, i-1, -1):
                ans.append(matrix[row - i - 1 ][j])
            if len(ans) == limit: break

            for j in range(row-i-2, i,-1):
                ans.append(matrix[j][i])
            if len(ans) == limit: break
            i += 1
        
        return ans

            
