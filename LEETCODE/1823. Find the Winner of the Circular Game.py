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

