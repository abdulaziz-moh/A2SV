class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = set()
        loser = set()
        removed = set()

        for v in matches:
            winner.add(v[0])
            if v[1] in loser:
                removed.add(v[1])
            loser.add(v[1])
        w,l = [], []
        for v in winner:
            if v not in loser:
                w.append(v)
        for v in loser:
            if v not in removed:
                l.append(v)
        w.sort()
        l.sort()
        return [w,l]
        
