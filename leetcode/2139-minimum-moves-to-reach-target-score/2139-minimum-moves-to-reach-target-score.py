class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target != 1:
            if target % 2 == 1:
                count += 1
                target -= 1
            elif maxDoubles != 0:
                target //= 2
                count += 1
                maxDoubles -= 1
            else:
                break
        else:
            return count
        return count + (target-1)