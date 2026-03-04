class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[0])
        n = len(points)
        
        i, arrow = 0, 0
        l,r = points[0][0], points[0][1]
        while i < n:
            while  i < n and l <= points[i][0] <= r :
                l, r = max(l,points[i][0]), min(r,points[i][1])
                i += 1
            arrow += 1
            if i < n:
                l, r = points[i][0], points[i][1]
        return arrow