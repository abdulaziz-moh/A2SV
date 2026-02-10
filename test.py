# t = int(input())
# for _ in range(t):
#     n = int(input())
    
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while True:
            temp = 0
            while n > 0:
                temp += (n%10)**2
                n //= 10
            n = temp
            print(n)
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.add(n)
            
obj = Solution()
obj.isHappy(19)