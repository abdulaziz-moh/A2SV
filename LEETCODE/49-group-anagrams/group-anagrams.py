class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedstr = []
        dd = defaultdict(list)
        for v in strs:
            sortedstr.append(str(sorted(v)))
        n = len(strs)
        for i in range(n):
            dd[sortedstr[i]].append(strs[i])
        ans = []
        for v in dd:
            ans.append(dd[v])
        return ans