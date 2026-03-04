from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ans = 0

        for v in operations:
            if v == 'C':
                stack.pop()
            elif v == 'D':
                stack.append(2*stack[-1])
            elif v == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(v))
        for v in stack:
            ans += v
        return ans