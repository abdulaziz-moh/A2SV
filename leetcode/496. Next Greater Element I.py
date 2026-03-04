from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = {x:i for i,x in enumerate(nums2)}
        next_g = {x:-1 for x in nums2}
        stack = []
        
        for v in nums2:
            if not stack:
                stack.append(v)
            else:
                while stack and v > stack[-1]:
                    next_g[stack.pop()] = v
                stack.append(v)
        ans = []
        for v in nums1:
            ans.append(next_g[v])
        print(ans)
        return(ans)
                    
                    


obj = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]

obj.nextGreaterElement(nums1,nums2)