from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        r,l,sum,count = 0,0,0,0
        length = len(nums)
        while r < length:
            while r <length and sum < k and sum >= 0:
                sum += nums[r]
                r += 1
                count += 1
            if sum < 0:
                while l < r:
                    sum -= nums[l]
                    count -= 1
                    l += 1
                    if sum >= k:
                        ans = min(ans,count)
                
                l = r
                sum = 0
                count = 0
                continue
            if sum >= k:
                ans = min(ans,count)
                sum -= nums[l]
                l += 1
                count -= 1
                
        while l < length:
            sum -= nums[l]
            count -= 1
            l += 1
            if sum >= k:
                ans = min(ans,count)

        if ans == float('inf'):
            print(ans)
            return -1
        else:
            print(ans)
            return ans
        
obj = Solution()
nums =[-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
k = 151
obj.shortestSubarray(nums,k)