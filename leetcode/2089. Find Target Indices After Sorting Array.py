class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        length = len(nums)
        rlist=[]

        for i in range(length):
            if nums[i] > target:
                    break 
            if nums[i] == target:
                rlist.append(i)
                
        return rlist