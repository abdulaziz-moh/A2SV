class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for v in s:
            if stack and v == '*':
                stack.pop()
            else:
                stack.append(v)
        return "".join(stack)