class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # for i in range(len(nums)):
        #     if nums[i] == target or nums[i] > target:
        #         return i
        # return len(nums)
        l = 0
        r = len(nums)-1
        m = 0
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
        return l

    