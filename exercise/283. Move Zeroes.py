
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)
        zi, nzi = 0, 0
        
        for i in range(length):
            while zi < length and nums[zi] != 0:
                zi += 1
            nzi = zi + 1
            while nzi < length and nums[nzi] == 0:
                nzi += 1
            
            if zi < length and nzi < length:
                nums[zi], nums[nzi] = nums[nzi], nums[zi]
        
        print(nums)

obj = Solution()   
nums = [0,1,0,3,12]
obj.moveZeroes(nums)

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i] = 0
        
        zi, nzi = 0, 0 
        for i in range(n):
            while zi < n and nums[zi] != 0:
                zi += 1
            nzi = zi + 1
            while nzi < n and nums[nzi] == 0:
                nzi += 1
            if nzi < n:
                nums[zi], nums[nzi] = nums[nzi], nums[zi]
        return nums
