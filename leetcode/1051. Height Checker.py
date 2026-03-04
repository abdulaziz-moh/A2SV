from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # # we can also use the built in function sorted() instead of sorting here
        # expected = sorted(heights)
        expected = heights.copy()
        n = len(heights)
        for i in range(1,n):
            si = i
            while si > 0 and expected[si] < expected[si-1]:
                expected[si], expected[si-1] = expected[si-1], expected[si]
                si -= 1
        
        count = 0
        for i in range(n):
            if expected[i] != heights[i]:
                count += 1
        return count
obj = Solution()
heights = [1,1,4,2,1,3]
obj.heightChecker(heights)