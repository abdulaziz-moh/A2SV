from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max,l,r = 0,0,len(height) - 1
        
        while l<r:
            if height[l] <= height[r]:
                x = height[l] * (r-l)
                l += 1
            else:
                x = height[r] * (r-l)
                r -= 1
            if x > max:
                max = x   
        return max

obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
obj.maxArea(height)   