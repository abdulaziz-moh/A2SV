class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unq = set()
        left = 0
        longest, count = 0, 0

        for right in range(len(s)):
            if s[right] not in unq:
                unq.add(s[right])
                count += 1
            else:
                while s[left] != s[right]:
                    unq.remove(s[left])
                    count -= 1
                    left += 1
                left += 1
            
            longest = max(count,longest) 
        return longest

                    