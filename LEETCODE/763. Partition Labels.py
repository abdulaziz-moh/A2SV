from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i
        
        left = 0
        right = -1
        length = len(s)
        ans = []
        
        while right < length:
            

            left = right + 1
            start = left-1
            right = last_index[s[left]]
            
            while left < right:
                left +=1
                if last_index[s[left]] > right:
                    right = last_index[s[left]]
                       
            ans.append(right - start)
            if right == length -1:
                break 
        return ans