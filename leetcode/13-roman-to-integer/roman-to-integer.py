class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        check = {'I','X','C'}

        n = len(s)
        i = 0
        ans = 0
        while i < n:
            if s[i] in check and  i+1 < n and s[i:i+2] in hm:
                ans += hm[s[i:i+2]]
                i += 2
                continue
            ans += hm[s[i]]
            i += 1
        return ans
            
            
