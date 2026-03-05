class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix,acc = [], 0
        for v in nums:
            acc += v
            prefix.append(acc)
        mn, ans = 0, float('-inf')
        for v in prefix:
            ans = max(ans,v-mn)
            mn = min(mn,v)
        return ans