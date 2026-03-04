class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        ans = [[],[]]
        for v in set1:
            if v not in set2:
                ans[0].append(v)
            else:
                set2.discard(v)
        ans[1] = list(set2)
        return ans
