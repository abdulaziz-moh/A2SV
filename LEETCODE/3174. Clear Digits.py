class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for v in s:
            if v.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(v)
        return "".join(stack)