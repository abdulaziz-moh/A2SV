class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        ans = []
        r,c,d = 0,0,1
        row = len(mat)
        col = len(mat[0])

        for _ in range(row*col):
            ans.append(mat[r][c])
            if d == 1:
                if c == col - 1:    # hit right wall
                    r += 1
                    d = -1
                elif r == 0:        # hit top wall
                    c += 1
                    d = -1
                else:               # normal moving upward
                    r -= 1
                    c +=1
            else:
                if r == row - 1:    # hit bottom wall
                    c += 1
                    d = 1
                elif c == 0:        # hit left wall
                    r += 1
                    d = 1
                else:
                    r += 1
                    c -= 1
        return ans
