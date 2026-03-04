class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        mx, count = 0, 0
        direction = [(-1,0),(0,1),(1,0),(0,-1)]

        def find(i,j):
            nonlocal count
            if grid[i][j] == 0:
                return
            count += 1
            grid[i][j] = 0

            for x,y in direction:
                nx, ny = i+x, j+y
                if 0 <= nx < row and 0 <= ny < col:
                    find(nx, ny)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                count = 0
                find(i,j)
                mx = max(mx,count)
        return mx