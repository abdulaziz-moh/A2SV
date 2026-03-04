class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # ranges.sort()

        for i in range(left,right+1):
            status = True
            for v in ranges:
                if i >= v[0] and i <= v[1]:
                    status = False
                    break
            if status:
                return False
        return True


        
            