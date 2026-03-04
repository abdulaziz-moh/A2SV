class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        i = 0
        while i < n:
            while i < n and path[i] == '/':
                i += 1
            l = i
            while i < n and path[i] != '/':
                i += 1
            val = path[l:i]

            if val == "..":
                if stack:
                    stack.pop()
            elif val != "." and val != "":
                stack.append(val)

        return "/" + ("/".join(stack))