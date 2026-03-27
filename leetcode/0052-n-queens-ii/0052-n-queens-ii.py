class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

   
        # a = []
        mrx = [['.']*n for _ in range(n)]
        count = [0]

        def backtrack(depth):
            if depth == 1:
                for i in range(n):
                    if mrx[n-1][i] == '.':
                        count[0] += 1
                        break
                return
            row = n - depth
            for i in range(n):
                
                if mrx[row][i] == 'I':
                    continue
                arr = []
                mrx[row][i] = 'Q'
                x, y = row + 1, i + 1
                while x < n and y < n:
                    if mrx[x][y] != 'I':
                        arr.append([x,y])
                    mrx[x][y] = 'I'
                    x += 1
                    y += 1
                x, y = row + 1, i-1
                while x < n and y >= 0:
                    if mrx[x][y] != 'I':
                        arr.append([x,y])
                    mrx[x][y] = 'I'
                    x += 1
                    y -= 1
                x, y = row + 1, i
                while x < n :
                    if mrx[x][y] != 'I':
                        arr.append([x,y])
                    mrx[x][y] = 'I'
                    x += 1

                backtrack(depth - 1)
                mrx[row][i] = '.'
                for x,y in arr:
                    mrx[x][y] = '.'

        backtrack(n)

        return count[0]
