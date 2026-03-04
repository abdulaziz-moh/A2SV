class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        reverse = {1:0,0:1}
        count = 0
        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] == reverse[nums[i+1]]
                nums[i+2] == reverse[nums[i+2]]
                count += 1
        if nums[-1] == 0 or nums[i-2] == 0:
            return -1
        return count