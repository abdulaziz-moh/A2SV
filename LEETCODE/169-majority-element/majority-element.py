class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = len(nums)//2
        hm = {}
        for v in nums:
            if v in hm:
                hm[v] += 1
            else:
                hm[v] = 1
            if hm[v] > t:
                return v
        