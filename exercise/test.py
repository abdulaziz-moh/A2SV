from typing import List

class Solution:
    def maxScoreIndices(nums: List[int]) -> List[int]:
        n = len(nums)  
        zc = [0]*(n+1)  # zero count
        oc = [0]*(n+1)  # one count
        
        count = 0
        for i in range(n):
            if nums[i] == 0:
                count += 1
                zc[i+1] = count
            else:
                zc[i+1] = count
        count = 0
        for i in range(n,0,-1):
            if nums[i-1] == 1:
                count += 1
                oc[i-1] = count
            else:
                oc[i-1] = count      
        ans = [0]
        maxm = 0
        for i in range(n+1):
            sum = zc[i] + oc[i]
            if sum > maxm:
                maxm = sum
                ans = []
                ans.append(i)
            elif sum == maxm:
                ans.append(i)
        return ans
            
        
   
obj = Solution
nums = [0,0,1,0]
obj.maxScoreIndices(nums)