class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda a: a[0])
        ans = []
        merged = intervals[0]
        n = len(intervals)
        
        for i in range(1,n):
            if merged[1] >= intervals[i][0]:
                merged = [merged[0], max(merged[1],intervals[i][1])]
            else:
                ans.append(merged)
                merged = intervals[i]
        ans.append(merged)
        return ans