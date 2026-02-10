class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        for v in s:
            s_count[v] = s_count.get(v,0) + 1
        for v in t:
            t_count[v] = t_count.get(v,0) + 1
        return t_count == s_count
        