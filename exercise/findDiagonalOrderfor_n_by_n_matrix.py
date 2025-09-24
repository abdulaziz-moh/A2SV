class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        a,b = 0,0
        d = 1
        row = len(mat)
        col = len(mat[0])
        n = max(row,col)
        for i in range(n): 
            d *= -1
            if d > 0:
                a = 0
                b = i
            else:
                a = i
                b = 0
            for _ in range(i+1):
                if a >= 0 and a < row and b >= 0 and b < col:
                    ans.append(mat[a][b])
                a += d
                b -= d
        for i in range(n-1,0,-1):
            d *= -1
            if d > 0:
                a = n - i
                b = n - 1
            else:
                a = n - 1
                b = n - i
            for _ in range(i):
                if a >= 0 and a < row and b >= 0 and b < col:
                    ans.append(mat[a][b])
                a += d
                b -= d
        return ans