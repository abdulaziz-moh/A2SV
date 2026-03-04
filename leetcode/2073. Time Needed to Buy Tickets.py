from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
    
        i = k
        count = 0
        while True:
            v = queue.popleft() - 1
            count += 1
            if v == 0 and i == 0:
                break
            elif v != 0:
                queue.append(v)
            
            if i != 0:
                i -= 1
            else:
                i = len(queue) - 1
            
        return(count)
        
            
            
        

    
    
obj = Solution()
tickets = [2,3,2]
k = 2
obj.timeRequiredToBuy(tickets,k)