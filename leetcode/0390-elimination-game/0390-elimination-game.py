class Solution:
    def lastRemaining(self, n: int) -> int:
        
        head = 1
        remaining = n
        step = 1
        left = True

        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step

            left = not left
            step *= 2
            remaining //= 2
        return head