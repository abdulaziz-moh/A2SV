class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def rec(n):
            if n == 1:
                return 1
            return 2 * ((n//2)+1 - rec(n//2))
        return rec(n)