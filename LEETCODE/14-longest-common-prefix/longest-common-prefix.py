class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            mn = float("inf")
            for v in strs:
                if len(v) < mn:
                    mn = len(v)
                    s = v
            ans = []
            for i in range(mn):
                for v in strs:
                    if v[i] != s[i]:
                        return "".join(ans)
                ans.append(s[i])
            return "".join(ans)
                         