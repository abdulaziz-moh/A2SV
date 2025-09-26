from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r = n,0
        x = m+n
        for i in range(m-1,-1,-1):
            x -= 1
            nums1[x] = nums1[i]
        x = m+n
        i = 0
        while l < x and r < n:
            if nums1[l] <= nums2[r]:
                nums1[i] = nums1[l]
                l += 1
            else:
                nums1[i] = nums2[r]
                r += 1
            i += 1
        while l<x:
            nums1[i] = nums1[l]
            l += 1
            i += 1
        while r<n:
            nums1[i] = nums2[r]
            r += 1
            i += 1
        # print(nums1)



obj = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj.merge(nums1,m,nums2,n)