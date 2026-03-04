from collections import Counter
from typing import List

class Solution:
    def countPairs(nums: List[int], k: int) -> int:
        dic = Counter(nums)
        keys = dic.keys()
        
        pairs = {k:[] for k in keys}
        for i in range(len(nums)):
            pairs[nums[i]].append(i)
            
        count = 0
        for pair in pairs.values():
            print(pair)
            p = len(pair)
            if p <2:
                continue
            for i in range(p-1):
                for j in range(i+1,p):
                    if (pair[i]*pair[j])%k == 0:
                        count += 1
        return count
                    
        
obj = Solution
nums = [3,1,2,2,2,1,3]
k = 2
obj.countPairs(nums,k)