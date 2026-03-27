class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ansarr = []
        a = []
        mrx = [['.']*n for _ in range(n)]

        def backtrack(depth):
            if depth == 1:
                # print(mrx)
                for i in range(n):
                    if mrx[n-1][i] == '.':
                        mrx[n-1][i] = 'Q'
                        ansarr.append([row[:] for row in mrx])
                        mrx[n-1][i] = '.'
                        continue
                return
            row = n - depth
            for i in range(n):
                
                if mrx[row][i] == 'I':
                    continue
                # print(depth, " ", i)
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
                # a.append(arr)


                backtrack(depth - 1)
                # arrs = a.pop()
                # arrs = arr[:]
                mrx[row][i] = '.'
                for x,y in arr:
                    mrx[x][y] = '.'

        backtrack(n)
        ans= []
        for v in ansarr:
            temp = []
            for row in v:
                for i in range(len(row)):
                    if row[i] != 'Q':
                        row[i] = '.'
                temp.append("".join(row))
            ans.append(temp)
        print(ans[::-1])
        return ans
