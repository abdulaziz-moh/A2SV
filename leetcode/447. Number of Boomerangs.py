import math
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for x,y in points:
            hm = {}
            for x1,y1 in points:
                # rg = math.sqrt((x-x1)**2 + (y-y1)**2)
                rg = (x-x1)**2 + (y-y1)**2 # no need of sqrt because we are conserned on the difference not on the value
                if rg in hm:
                    hm[rg] += 1
                else:
                    hm[rg] = 1
            for v in hm.values():
                count += (v * (v-1))
        return count