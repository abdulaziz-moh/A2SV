class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n-2,-1,-1):
            
            if nums[i] > nums[i+1]:
                devide_amount = math.ceil(nums[i] / nums[i+1])
                count += (devide_amount-1)
                nums[i] = nums[i]//devide_amount

        return count