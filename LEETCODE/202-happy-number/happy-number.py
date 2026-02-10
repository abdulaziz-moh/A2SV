class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while True:
            temp = 0
            while n:
                temp += (n%10)**2
                n //= 10
            n = temp
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.add(n)