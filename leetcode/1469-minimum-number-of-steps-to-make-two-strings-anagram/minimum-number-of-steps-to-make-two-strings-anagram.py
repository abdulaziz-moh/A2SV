class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        sc = Counter(s)
        tc = Counter(t)
        for k,v in sc.items():
            x = v - tc[k]
            if x > 0:
                ans += x
        return ans
