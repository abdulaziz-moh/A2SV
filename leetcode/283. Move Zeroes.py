# brutforce approch use this example nums = [1,0,1,3,6,0,0,0]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nzp = 0
        for i in range(n):
            if nums[i] == 0:
                for j in range(i+1,n):
                    if nums[j] != 0:
                        nzp = j
                        break
                else:
                    break
            nums[i], nums[nzp] = nums[nzp], nums[i]

# more efficient way
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ins_pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[ins_pos] = nums[ins_pos], nums[i]
                ins_pos += 1

                    