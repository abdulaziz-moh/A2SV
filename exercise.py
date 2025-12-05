from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        hm = {'(':')', '{':'}', '[':']'} 
        stack = []
        for v in s:
            if v in hm:
                stack.append(v)
            else:
                if not stack or v != hm[stack.pop()]:
                    return False
        if stack:
            return False
        else:
            return True