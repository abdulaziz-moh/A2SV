class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        col = len(grid[0])
        ans = 0
        for arr in grid:
            for i in range(col):
                if arr[i] < 0:
                    ans += (col - i)
                    break
        return ans