class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        a = bisect_left(nums, target)
        b = bisect_right(nums, target) - 1
        if a <= b:
            return [a,b]
        return [-1,-1]