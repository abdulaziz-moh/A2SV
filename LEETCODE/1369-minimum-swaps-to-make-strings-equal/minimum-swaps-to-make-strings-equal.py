class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        s1c = Counter(s1)
        s2c = Counter(s2)

        if (s1c['x'] + s2c['x']) % 2 != 0:
            return -1
        
        n = len(s1)
        ans = 0
        first = {'x':0,'y':0}
        for i in range(n):
            if s1[i] != s2[i]:
                first[s1[i]] += 1
        ans += (first['x'] //2 ) + (first['x'] % 2) + (first['y'] //2 ) + (first['y'] % 2)

        return ans
