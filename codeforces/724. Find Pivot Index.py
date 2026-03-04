class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        lsum, rsum = [0]*n,[0]*n
        lsum[0], rsum[n-1] = nums[0],nums[n-1]
        for i in range(1,n):
            lsum[i] = lsum[i-1] + nums[i]
        for i in range(n-2,-1,-1):
            rsum[i] = rsum[i+1] + nums[i]

        for i in range(n):
            if lsum[i] == rsum[i]:
                return i
        return -1