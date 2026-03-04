# let's solve it by bubble sort
from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(heights)
        for i in range(1,n):
            for j in range(n - i):
                if heights[j] < heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1], heights[j]
                    names[j],names[j+1] = names[j+1], names[j]
        return names
    
obj = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
obj.sortPeople(names,heights)

# let's solve it by selection sort

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(heights)
        for i in range(n-1):
            min_i = i
            for j in range(i+1,n):
                if heights[j] > heights[min_i]:
                    min_i = j
            heights[i],heights[min_i] = heights[min_i], heights[i]
            names[i],names[min_i] = names[min_i], names[i]
        return names

# let's solve it by insertion sort
  
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(heights)
        for i in range(1,n):
            j = i
            while j > 0:
                if heights[j] > heights[j-1]:
                    heights[j],heights[j-1] = heights[j-1], heights[j]
                    names[j],names[j-1] = names[j-1], names[j]
                    j -= 1
                else:
                    break
        return names