#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        hm = {}
        for v in b:
            if v in hm:
                hm[v] += 1
            else:
                hm[v] = 1
        for v in a:
            if v in hm:
                hm[v] -= 1
        for v in hm.values():
            if v > 0:
                return False
        return True
    # 6min