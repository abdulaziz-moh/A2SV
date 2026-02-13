class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        row, col = len(mat), len(mat[0])
        i, j, dxn = 0, 0, 1

        while i < row and j < col:
            if dxn == 1:
                ans.append(mat[i][j])
                x = i - 1
                y = j + 1
                if x < 0 or y >= col:
                    if j == col - 1:
                        i += 1
                    else:
                        j += 1
                    dxn = 0
                else:
                    i, j = x, y
            else:
                ans.append(mat[i][j])
                x = i + 1
                y = j - 1
                if x >= row or y < 0:
                    if i == row - 1:
                        j += 1
                    else:
                        i += 1
                    dxn = 1
                else:
                    i, j = x, y
        return ans