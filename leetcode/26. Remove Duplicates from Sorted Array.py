from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        n = len(nums)
        if n > 0:
            k = 1
        for i in range(n-1):
            if nums[i] != nums[i + 1]:
                k += 1
        s,f = 0 ,0
        while s < k:
            nums[s] = nums[f]
            while f+1<n and nums[f] == nums[f + 1]:
                    f += 1
            f += 1
            s += 1 
        return k
        
        
obj = Solution()
height = [0,0,1,1,1,2,2,3,3,4]
obj.removeDuplicates(height) 