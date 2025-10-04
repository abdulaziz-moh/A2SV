from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum,left,count,ans = 0,0,0,len(nums)
        
        for v in nums:
            while sum < target:
                sum += v
                count += 1
            while sum >= target:
                sum -= nums[left]
                left += 1
                count -= 1
            ans = min(ans,count+1)
        print(ans)
        return ans