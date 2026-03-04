class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        h,s = 0,0
        while s < n and h < n:
            while s < n and nums[s] == 0:
                s += 1
            if s >= n:
                break
            nums[s],nums[h] = nums[h],nums[s]
            h += 1
            s += 1