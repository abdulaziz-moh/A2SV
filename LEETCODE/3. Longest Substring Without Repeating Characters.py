class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        left,count,longest = 0,0,0
        for v in s:
            if v in hm:
                while s[left] != v:
                    del hm[s[left]]
                    left += 1
                    count -= 1    
                count -= 1
                left += 1
            hm[v] = 0
            count += 1
            longest = max(longest,count)
        return longest