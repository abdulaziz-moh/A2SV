
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        unique = []
        for i,v in enumerate(s):
            if v in hm:
                hm[v] += 1
            else:
                unique.append([i,v])
                hm[v] = 1
        for i,v in unique:
            if hm[v] == 1:
                return i
        return -1