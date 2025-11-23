class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = [0]*3
        for v in nums:
            count[v] += 1
        i,j = 0,0
        while i<n:
            while count[j] >0:
                nums[i] = j
                i += 1
                count[j] -= 1
            j += 1
            
# alternative
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0,0,0]
        for v in nums:
            arr[v] += 1
        k = 0
        for i in range(len(arr)):
            while  arr[i]> 0:
                nums[k] = i
                arr[i] -= 1
                k += 1