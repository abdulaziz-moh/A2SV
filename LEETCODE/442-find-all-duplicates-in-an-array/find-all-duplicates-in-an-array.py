class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for v in nums:
            if nums[abs(v)-1] < 0:
                ans.append(abs(v))
            nums[abs(v)-1] *= -1
        return ans