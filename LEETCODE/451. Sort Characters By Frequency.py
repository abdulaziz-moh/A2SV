class Solution:
    def frequencySort(self, s: str) -> str:
        hm = {}
        count = []
        for v in s:
            if v in hm:
                hm[v] += 1
            else:
                hm[v] = 1
        for k,v in hm.items():  # [num,count]
            count.append([k,v])
        n = len(count)
        for i in range(1,n):
            si = i
            while si > 0 and count[si][1] > count[si-1][1]:
                count[si], count[si-1] = count[si-1], count[si]
                si -= 1
        ans = []
        for v,c in count:
            while c > 0:
                ans.append(v)
                c -= 1
        return "".join(ans)