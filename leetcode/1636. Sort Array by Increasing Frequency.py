from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm = {}
        
        for v in nums:
            if v in hm:
                hm[v] += 1
            else:
                hm[v] = 1
        nwc = [] # num with count
        for key,value in hm.items():
            nwc.append([key,value])
        n = len(nwc)
        for i in range(1,n):
            si = i
            while si > 0 and nwc[si][1] < nwc[si-1][1]:
                nwc[si],nwc[si-1] = nwc[si-1],nwc[si]
                si -= 1
            while si > 0 and nwc[si][1] == nwc[si-1][1] and nwc[si][0] > nwc[si-1][0]:
                nwc[si],nwc[si-1] = nwc[si-1],nwc[si]
                si -= 1
        i = 0
        for num,count in nwc:
            while count > 0:
                nums[i] = num
                i += 1
                count -= 1
        return nums
    
obj = Solution()
nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]
nums = [-1,1,-6,4,5,-6,1,4,1]
obj.frequencySort(nums)