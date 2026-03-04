class Solution:
    def isValid(self, s: str) -> bool:
        peek = -1
        hm = {'(':')','{':'}','[':']'}
        stack = []
        for v in s:
            if v in hm:
                stack.append(v)
                peek += 1
            else:
                if stack and hm[stack[peek]] == v:
                    stack.pop()
                    peek -= 1
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False