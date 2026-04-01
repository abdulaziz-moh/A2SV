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