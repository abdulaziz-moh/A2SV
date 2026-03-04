class NumArray:

    def __init__(self, nums: List[int]):

        self.running, sum = [0], 0
        for v in nums:
            sum += v
            self.running.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.running[right + 1] - self.running[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)