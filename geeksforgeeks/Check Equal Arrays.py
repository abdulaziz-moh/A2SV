class Solution:
    def checkEqual(self, a, b) -> bool:
        hm = {}
        for v in a:
            if v in hm:
                hm[v] += 1
            else:
                hm[v] = 1
        for v in b:
            if v in hm and hm[v] > 0:
                hm[v] -= 1
            else:
                return False
        return True
    # 2sub 8 min