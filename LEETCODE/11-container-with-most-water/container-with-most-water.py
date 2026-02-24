class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        ln, a = n-1, min(height[l], height[r])*(n-1)

        while l < r:
            if height[l] < height[r]:
                l += 1
            else :
                r -= 1
            ln -= 1
            x = min(height[l], height[r])*ln
            if x > a:
                a = x
        return a