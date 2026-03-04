class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hm = {}
        for i in range(n):
            if nums[i] in hm:
                return [hm[nums[i]],i]
            v = target - nums[i]
            hm[v] = i
            

        # for i in range(n-1):
        #     v = target - nums[i]
        #     if v in hm and hm[v] != i:
        #         return [i,hm[v]]









        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]