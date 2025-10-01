class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k,n = len(p),len(s)
        if k > n:
            return []
        target = {v:0 for v in p}
        window = {v:0 for v in p}
        a,ans = [],[]
        for v in p:
            target[v] += 1
            a.append(v)
# =============================================
        for i in range(k):
            if s[i] in a:
                window[s[i]] += 1
        status = True
        for v in a:
            if window[v] != target[v]:
                status = False
        if status:
            ans.append(i-k+1)
# ==============================================
        for i in range(k,n):
            if s[i-k] in a:
                window[s[i-k]] -= 1
            if s[i] in a:
                window[s[i]] += 1
            status = True
            for v in a:
                if window[v] != target[v]:
                    status = False
            if status:
                ans.append(i-k+1)
        return ans