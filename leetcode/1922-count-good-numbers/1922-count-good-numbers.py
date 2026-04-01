class Solution:
    def countGoodNumbers(self, n: int) -> int:
        x = 10**9 + 7
        even = math.ceil(n/2)
        odd = n//2
        ans = pow(5,even, x) * pow(4, odd, x)
        return ans % x