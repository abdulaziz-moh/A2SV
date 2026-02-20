class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n, mx, mn = len(heights), max(heights), min(heights)
        revsorted, hm, count = [], {}, [0]*(mx-mn+1)

        for i in range(n):
            hm[heights[i]] = names[i]
        
        for v in heights:
            count[abs(v-mx)] += 1
        
        for i in range(len(count)):
            for j in range(count[i]):
                revsorted.append(i)

        return [hm[mx-revsorted[i]] for i in range(n)]