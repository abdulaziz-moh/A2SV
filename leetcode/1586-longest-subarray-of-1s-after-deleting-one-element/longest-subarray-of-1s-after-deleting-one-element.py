class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        idx, k, count, ans, n = 0, 1, 0, 0, len(nums)

        for right in range(n):
            if nums[right] == 0:
                if k == 1:
                    k = 0
                else:
                    count = right - idx - 1
                idx = right
            else:
                count += 1
                ans = max(ans,count)
        if k == 1:
            ans -= 1
        return ans

           
                