class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        lastidx = 0
        ans = []
        if not intervals:
            return [newInterval]
        for i in range(len(intervals)):
            lastidx = i
            if newInterval[0] > intervals[i][0]:
                if  newInterval[0] > intervals[i][1]:
                    ans.append(intervals[i])
                    continue
                elif newInterval[0] > intervals[i][0]:
                    newInterval[0] = intervals[i][0]
                    if newInterval[1] <= intervals[i][1]:
                        # newInterval[1] = intervals[i][1]
                        # ans.append(newInterval)
                        break
            else:
                if  newInterval[1] < intervals[i][0]:
                    # print(intervals[i][0])
                    # print(newInterval)
                    ans.append(newInterval)
                    lastidx = i
                    break
                elif newInterval[1] > intervals[i][1]:
                    # print(newInterval)
                    continue
                else:
                    newInterval[1] = intervals[i][1]
                    lastidx = i+1
                    # print(newInterval)
                    ans.append(newInterval)
                    break
        if newInterval[1] > intervals[len(intervals)-1][1]:
            ans.append(newInterval)
        else:
            ans.extend(intervals[lastidx:])
        return ans