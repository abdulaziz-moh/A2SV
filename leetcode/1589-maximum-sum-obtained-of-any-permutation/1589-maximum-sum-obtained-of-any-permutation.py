class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        n = len(nums)
        prefix = [0]*(n+1)
        for l,r in requests:
            prefix[l] += 1
            prefix[r+1] -= 1
        for i in range(1,n):
            prefix[i] += prefix[i-1]
        prefix.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                break
            ans += (prefix[i] * nums[i])
        return ans % (10**9 + 7)