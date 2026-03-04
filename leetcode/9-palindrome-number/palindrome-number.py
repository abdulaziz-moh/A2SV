class Solution:
    def isPalindrome(self, x: int) -> bool:
        v = str(x)
        l,r = 0,len(v)-1
        while l < r:
            if v[l] != v[r]:
                return False
            l += 1
            r -= 1
        return True