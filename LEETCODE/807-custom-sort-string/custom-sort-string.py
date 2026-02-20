class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = defaultdict(int)
        hm = defaultdict(int)
        rem = []
        
        for ch in order:
            hm[ch] += 1
        for ch in s:
            if ch in hm:
                count[ch] += 1
            else:
                rem.append(ch)
            
        for ch in order:
            for _ in range(count[ch]):
                rem.append(ch)
        return "".join(rem)