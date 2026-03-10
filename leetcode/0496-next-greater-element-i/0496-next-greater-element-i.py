class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
        return(ans)