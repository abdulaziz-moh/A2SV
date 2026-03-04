class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            sum = l**2 + r**2
            if sum == c:
                return True
            elif sum > c:
                r -= 1
            else:
                l += 1
        return False