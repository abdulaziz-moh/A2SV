from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # this question preferes the counter sort way
        l = max(arr1) + 1
        count = [0] * l
        status = [True] * l
        # create the counter
        for v in arr1:
            count[v] += 1
        x = 0
        # store elements in relative order untill all arr2 elements finish
        for v in arr2:
            status[v] = False
            for _ in range(count[v]):
                arr1[x] = v
                x += 1
        # store the remaining elementes in ascending order 
        for i in range(l):
            if status[i]:
                for _ in range(count[i]):
                    arr1[x] = i
                    x += 1
        return arr1
    
# my second submission 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hm = {}
        for v in arr1:
            if v in hm:
                hm[v] += 1
            else:
                hm[v] = 1
        i = 0
        for v in arr2:
            while hm[v] > 0:
                arr1[i] = v
                hm[v] -= 1
                i += 1
            del hm[v]
        rem = []
        for key in hm.keys():
            rem.append(key)
        rem.sort()
        for v in rem:
            while hm[v] > 0:
                arr1[i] = v
                hm[v] -= 1
                i += 1
        return arr1