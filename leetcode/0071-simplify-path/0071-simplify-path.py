class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split('/')
        for v in arr:
            if v == '..':
                if stack:
                    stack.pop()
            elif v != '.' and v != '':
                stack.append(v)

        return "/" + "/".join(stack)