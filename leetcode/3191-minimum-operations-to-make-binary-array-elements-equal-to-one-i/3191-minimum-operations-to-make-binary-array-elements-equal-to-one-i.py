class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, count = len(nums), 0
        reverse = {1:0,0:1}
        for i in range(n-2):
            if nums[i] == 1:
                continue
            nums[i] = 1
            nums[i+1] = reverse[nums[i+1]]
            nums[i+2] = reverse[nums[i+2]]
            count += 1
        if len(nums) == 1 and nums[0] == 1:
            return -1
        elif len(nums) >= 2 and ( nums[-1] == 0 or nums[-2] == 0):
            return -1
        return count



















        # n = len(nums)
        # reverse = {1:0,0:1}
        # count = 0
        # for i in range(n-2):
        #     if nums[i] == 0:
        #         nums[i] = 1
        #         nums[i+1] == reverse[nums[i+1]]
        #         nums[i+2] == reverse[nums[i+2]]
        #         count += 1
        # if nums[-1] == 0 or nums[i-2] == 0:
        #     return -1
        # return count