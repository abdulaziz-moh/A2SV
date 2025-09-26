class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        new = nums[n-k:]
        x = n
        for i in range(n-k-1,-1,-1):
            x -= 1
            nums[x] = nums[i]
        for i in range(k):
            nums[i] = new[i]