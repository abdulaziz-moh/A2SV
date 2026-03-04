class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if mat == target:
            return True
        for _ in range(3):
            for i in range(n-1):
                for j in range(i+1,n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            half = math.ceil(n/2)
            for i in range(n):
                for j in range(half):
                    mat[i][j], mat[i][n-j-1] = mat[i][n-j-1], mat[i][j]
            if mat == target:
                return True
        return False
