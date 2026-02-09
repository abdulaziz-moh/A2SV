class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dd = defaultdict(list)
        for v in strs:
            dd["".join(sorted(v))].append(v)
        
        return list(dd.values())