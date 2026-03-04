class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target, window = Counter(p), Counter(s[:len(p)-1])
        ans, left = [], 0

        for right in range(len(p)-1, len(s)):
            window[s[right]] += 1
            if target == window:
                ans.append(left)
                
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        return ans