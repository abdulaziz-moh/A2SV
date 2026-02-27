class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, window, mx, ans, n = 0, 0, 0, 0, len(s)
        dd = defaultdict(int)
        for right in range(n):
            dd[s[right]] += 1
            mx = max(dd.values())
            window += 1
            while window - mx > k:
                dd[s[left]] -= 1
                window -= 1
                mx = max(dd.values())
                left += 1
            ans = max(ans, window)
        return ans

