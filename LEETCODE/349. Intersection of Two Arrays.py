class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique1 = set(nums1)
        ans = set()
        for v in nums2:
            if v in unique1:
                ans.add(v)
        return list(ans)