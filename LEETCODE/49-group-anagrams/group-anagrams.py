class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sortedstr = []
        dd = defaultdict(list)
        for v in strs:
            dd[str(sorted(v))].append(v)
        
        return list(dd.values())