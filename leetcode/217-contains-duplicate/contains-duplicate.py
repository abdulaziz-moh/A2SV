class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for v in nums:
            if v in set1:
                return True
            set1.add(v)
        return False
        