class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        unq = set()

        for v in nums:
            if v in unq:
                ans.append(v)
            else:
                unq.add(v)
        return ans