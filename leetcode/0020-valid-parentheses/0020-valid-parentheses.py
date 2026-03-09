class Solution:
    def isValid(self, s: str) -> bool:
        hm = {'(':')', '{':'}', '[':']'}
        stack = []
        for v in s:
            if v in hm:
                stack.append(v)
            else:
                if stack and hm[stack[-1]] == v:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
                









        # hm = {'(':')', '{':'}', '[':']'}
        # stack = []
        # for v in s:
        #     if v in hm:
        #         stack.append(v)
        #     else:
        #         if not stack or  v != hm[stack.pop()]:
        #             return False
        # if not stack:
        #     return True
        # else:
        #     return False