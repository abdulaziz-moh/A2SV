class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n, hm = len(s), {}
        mn,mx = 0,0
        for i in range(n):
            if s[i] in hm:
                hm[s[i]][1] = i
            else:
                hm[s[i]] = [i,i]
        i = 0
        ans = []
        while i < n:
            mx = hm[s[i]][1]
            while i <= mx:
                mx = max(mx, hm[s[i]][1])
                i += 1
                
            ans.append(i-mn)
            mn = i
        return ans