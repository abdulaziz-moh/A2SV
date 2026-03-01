class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left, longest, window = 0, 0, 0

        for right in range(len(s)):
            if s[right] not in unique:
                unique.add(s[right])
                window += 1
            else:
                while s[left] != s[right]:
                    unique.remove(s[left])
                    left += 1
                left += 1
                window = right - left + 1
                
            longest = max(longest, window)

        return longest