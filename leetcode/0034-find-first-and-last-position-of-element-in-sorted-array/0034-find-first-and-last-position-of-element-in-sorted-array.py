class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = bisect_left(nums, target)
        b = bisect_left(nums, target+1)
        b -= 1
        if a <= b:
            return [a,b]
        return [-1,-1]



        # idx, left, right = -1, 0, len(nums)-1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # start = right + 1

        # idx, left, right = -1, 0, len(nums)-1
        # while left <= right:
        #     mid = (left + right) // 2

        #     if nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # end = left - 1
        # if start <= end:
        #     return [start, end]
        # return [-1,-1]