class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        elem = set()
        for v in nums:
            elem.add(v)
        for i in range(len(nums) + 1):
            if i not in elem:
                return i