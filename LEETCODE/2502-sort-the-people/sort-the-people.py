class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        hm = {}
        for i in range(n):
            hm[heights[i]] = names[i]

        # for i in range(1,n):
        #     for j in range(i,0,-1):
        #         if heights[j] > heights[j-1]:
        #            heights[j] , heights[j-1] = heights[j-1], heights[j] 
        #         else:
        #             break
        # return [hm[heights[i]] for i in range(n)]

        mx,mn = max(heights), min(heights)
        count = [0] * (mx-mn+1)
        for v in heights:
            count[v-mn] += 1
        ans = []
        for i in range(len(count)):
            for j in range(count[i]):
                ans.append(mn + i)
        ans.reverse()
        return [hm[ans[i]] for i in range(n)]