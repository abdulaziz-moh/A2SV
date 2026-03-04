class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win,lft,mx_count,ans = 0,0,0,0
        hm = collections.Counter()
        for v in s:
            hm[v] += 1
            win += 1
            mx_count = max(hm.values())
            if win - mx_count <= k:
                ans = max(ans,win)
            else:
                hm[s[lft]] -= 1
                lft += 1
                win -= 1
        return ans