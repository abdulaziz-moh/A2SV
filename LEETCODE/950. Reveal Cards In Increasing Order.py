from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        idx_queue = deque(i for i in range(n))
        ans = [0]*n
        deck.sort()
        for i in range(n-1):
            ans[idx_queue.popleft()] = deck[i]
            idx_queue.append(idx_queue.popleft())
            print(idx_queue)
        ans[idx_queue.popleft()] = deck[-1]
        
        return ans
obj = Solution()
deck = [17,13,11,2,3,5,7]
obj.deckRevealedIncreasing(deck)