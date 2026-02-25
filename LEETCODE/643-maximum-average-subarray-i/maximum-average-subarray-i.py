class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r,n = 0, k, len(nums)
        sum = 0
        for i in range(k):
            sum += nums[i]
        mx = sum
        while r < n:
            sum += nums[r]
            sum -= nums[l]
            if sum > mx:
                mx = sum
            l += 1
            r += 1
        return mx/k