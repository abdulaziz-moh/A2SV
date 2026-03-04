from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.append(0)        
        j = 0
        num = target
        length = len(nums) 

        while j<length and num >0 :
            num -= nums[j]
            j+=1
        
        if num > 0:
            return 0

        mn = j

        left = 0
        right = j

        while right < length:
            if num <= 0:
                mn =min (mn, right-left)
                num += nums[left]
                left+=1
            else:
                num -= nums[right]
                right+=1
        mn = min (mn, right-left)        
        return mn