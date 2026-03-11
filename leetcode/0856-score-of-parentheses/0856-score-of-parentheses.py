class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for v in s:
            if v != ')':
                stack.append(v)
            else:
                sum = 0
                while stack and stack[-1] != '(':
                    sum += stack.pop()
                stack.pop()
                if sum != 0:
                    stack.append(2*sum)
                else:
                    stack.append(1)

        ans = 0
        for v in stack:
            ans += v
        return ans