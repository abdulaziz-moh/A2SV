class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        firstidx = {0:-1}
        prefix, mx = 0, 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix in firstidx:
                mx = max(mx, (i-firstidx[prefix]))
            else:
                firstidx[prefix] = i
        return mx