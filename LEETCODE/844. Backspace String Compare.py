class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack, tstack = [],[]
        for v in s:
            if v != '#':
                sstack.append(v)
            else:
                if sstack:
                    sstack.pop()
        for v in t:
            if v != '#':
                tstack.append(v)
            else:
                if tstack:
                    tstack.pop()
        if sstack == tstack:
            return True
        return False