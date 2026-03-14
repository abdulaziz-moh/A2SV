class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans =0
        while l < r:
            sum = nums[l] + nums[r]
            if sum < target:
                ans += (r-l)
                l += 1
            else:
                r -= 1
        return ans