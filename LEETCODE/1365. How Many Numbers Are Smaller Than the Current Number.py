class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        htable = {}
        newnum = list(nums) 
        sorted_nums = sorted(nums)
        length = len(sorted_nums)

        for i in range(length):
            if sorted_nums[i] not in htable:
                htable[sorted_nums[i]] = i

        result = []
        for num in newnum:
            result.append(htable[num])

        return result