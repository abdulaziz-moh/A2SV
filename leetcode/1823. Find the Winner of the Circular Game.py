class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        p = [i for i in range(1,n+1)]
        i = (k % n) - 1
        while n != 1:
            del p[i]
            n -= 1
            if i < 0:
                i = ((k % n - 1) + i + 1) % n
            else:
                i = ((k % n - 1) + i) % n
        return p[0]
# obj = Solution()
# print(obj.findTheWinner(8,8))

# efficient way
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        c_arr = [i for i in range(1,n+1)]
        i = 0
        for _ in range(n-1):
            if i == -1:
                i = 0
            i = ((i + k) % len(c_arr)) - 1
            del c_arr[i]
        return c_arr[0]
 

