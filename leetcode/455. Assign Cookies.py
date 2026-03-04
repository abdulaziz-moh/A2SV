from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gp,sp = 0,0
        count = 0
        while sp < len(s) and gp < len(g):
            if g[gp] <= s[sp]:
                gp += 1
                sp += 1
                count += 1
            else:
                sp += 1
        return count