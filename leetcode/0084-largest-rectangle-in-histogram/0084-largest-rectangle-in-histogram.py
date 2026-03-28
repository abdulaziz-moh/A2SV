class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        hmf = {idx: -1 for idx in range(n)}

        stack = []  # store index, monotonic increasing stack to get smaller(next smaller)
        for idx in range(n):

            while stack and heights[stack[-1]] > heights[idx]:
                hmf[stack.pop()] = idx
            stack.append(idx)
        
                # hm = {idx: -1 for idx in range(n)}

        hmb = {idx: -1 for idx in range(n)}
        stack = []  # store index, monotonic increasing stack to get smaller(next smaller)
        for idx in range(n-1,-1,-1):

            while stack and heights[stack[-1]] > heights[idx]:
                hmb[stack.pop()] = idx
            stack.append(idx)
        print(hmf)
        print(hmb)

        ans = -1
        for idx in range(n):
            if hmf[idx] == -1:
                temp = (n - idx) * heights[idx]
            elif hmf[idx] != -1:
                temp = (hmf[idx] - idx) * heights[idx]
            
            if hmb[idx] == -1:
                temp += idx * heights[idx]
            elif hmb[idx] != -1:
                temp += (idx - hmb[idx] - 1) * heights[idx]
            ans = max(ans, temp)
        
        return ans
            