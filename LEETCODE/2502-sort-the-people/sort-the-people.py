class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        hm = {}
        for i in range(n):
            hm[heights[i]] = names[i]
        
        for i in range(1,n):
            for j in range(n-i):
                if heights[j] < heights[j + 1]:
                    heights[j],  heights[j + 1] = heights[j + 1], heights[j]
        return [hm[heights[i]] for i in range(n)]
                