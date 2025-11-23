class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str,nums))
        for i in range(1,n):
            si = i
            while si > 0 and nums[si] + nums[si-1] > nums[si-1] + nums[si]:
                nums[si] , nums[si-1] = nums[si-1] , nums[si]
                si -= 1
        i = 0
        while i < n-1:
            if nums[i] != "0":
                break
            i += 1

        return "".join(nums[i:])