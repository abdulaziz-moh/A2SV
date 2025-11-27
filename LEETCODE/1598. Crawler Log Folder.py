class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for v in logs:
            if v[0] == '.' and v[1] == '.':
                if stack:
                    stack.pop()
            elif v[0] != '.':
                stack.append('a')
        return len(stack)
