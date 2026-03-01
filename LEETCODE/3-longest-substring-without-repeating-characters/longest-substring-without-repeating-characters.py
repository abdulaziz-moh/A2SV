class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left, longest = 0, 0

        for right in range(len(s)):
            if s[right] in unique:
                while s[right] in unique:
                    unique.remove(s[left])
                    left += 1
            unique.add(s[right])
            longest = max(longest, right - left + 1)
        return longest