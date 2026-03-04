class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        hm = {}
        i = 0
        for arr in responses:
            for v in arr:
                if v not in hm:
                    hm[v] = [i,1]
                else:
                    if hm[v][0] != i:
                        hm[v][0] = i
                        hm[v][1] += 1
            i += 1

        mx = 0
        ans = ""
        for key,value in hm.items():
            if mx < value[1]:
                ans = key
                mx = value[1]
            elif mx == value[1] and key <= ans:
                ans = key
            
        return ans