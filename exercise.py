class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sum = 0
        # while True:
        for _ in range(10):
            while n != 0:
                sum += (n%10)**2
                n = n//10
            if sum == 1:
                return True
            elif sum in seen:
                return False
            else:
                seen.add(sum)
            print(sum)
            print(n)
            n = sum
            sum = 0
sol = Solution()
print(sol.isHappy(19))