class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left =  0
        winsum = sum(nums[:k])
        mx = winsum

        for right in range(k,len(nums)):
            winsum = winsum - nums[left] + nums[right]
            mx = max(mx,winsum)
            left += 1
        return mx/k