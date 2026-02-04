class Solution:    
    def findUnion(self, a, b):
        a.extend(b)
        return (list(set(a)))

        # 1sub 2min