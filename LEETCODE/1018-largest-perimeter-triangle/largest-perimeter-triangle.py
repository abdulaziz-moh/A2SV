class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n,mx = len(nums), 0
        nums.sort()
        for i in range(n-2):
            if nums[i] + nums[i+1] > nums[i+2] and nums[i] + nums[i+2] > nums[i+1] and nums[i+1] + nums[i+2] > nums[i]:
                mx = max(mx, (nums[i] + nums[i+1] + nums[i+2]))
        return mx