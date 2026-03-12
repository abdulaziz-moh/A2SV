class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mn =[float('inf')]
        minimum = float('inf')
        for v in nums:
            minimum = min(minimum, v)
            mn.append(minimum)
        next_g = {i: float('-inf') for i in range(len(nums))}
        dec_stack = []
        for i in range(len(nums) - 1, -1, -1):
            while dec_stack and nums[dec_stack[-1]] < nums[i]:
                next_g[dec_stack.pop()] = i
            dec_stack.append(i)

        # print(next_g)
        # print(mn)
        for i in range(2,len(nums)):
            # pass
            if next_g[i] != float("-inf") and mn[next_g[i]] < nums[i]:
                return True
        return False 