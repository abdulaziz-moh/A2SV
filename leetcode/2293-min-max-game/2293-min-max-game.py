class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while True:
            if len(nums) == 1:
                return nums[0]

            elif len(nums) == 2:
                return min(nums[0], nums[1])

            else:
                temp = []
                for i in range(0,len(nums),4):
                    temp.append(min(nums[i], nums[i+1]))
                    temp.append(max(nums[i+2], nums[i+3]))
                nums = temp