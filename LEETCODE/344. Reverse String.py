from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        k = l//2
        l -= 1 
        for i in range(k):
            s[i],s[l-i ] = s[l-i],s[i]
