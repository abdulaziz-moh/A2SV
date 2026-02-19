class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str,nums))

        for i in range(1,n):

            for j in range(i,0,-1):
                if nums[j] + nums[j-1] > nums[j-1] + nums[j]:
                    nums[j] , nums[j-1] = nums[j-1] , nums[j]
                    continue
                break
        i = 0
        while i < n-1: 

            if nums[i] == "0":
                i += 1
                continue
            break
        return "".join(nums[i:])