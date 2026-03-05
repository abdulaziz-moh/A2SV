class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix, mn = 0, float('inf')        
        for v in nums:
            prefix += v
            mn = min(mn, prefix)
        ans = 1-mn
        return ans if ans > 0 else 1
        