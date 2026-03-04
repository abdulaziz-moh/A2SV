class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        hm = {0:-1}
        prefix = 0

        for i in range(n):
            prefix += nums[i]
            x = prefix % k
            if x in hm and i - hm[x] > 1:
                return True
            if x not in hm:
                hm[x] = i
        return False





# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:

#         n = len(nums)
#         prefix = []
#         sum = 0
#         for v in nums:
#             sum += v
#             prefix.append(sum)
#         hm = {prefix[0] % k:0}

#         for i in range(1,n):
#             x = prefix[i] % k
#             if x == 0 or x in hm and i - hm[x] > 1:
#                 return True
#             if x not in hm:
#                 hm[x] = i
#         return False