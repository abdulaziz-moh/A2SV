class NumArray:
    def __init__(self, nums:List[int]):

        self.prefixsum = [0]
        self.prefixsum.extend(nums)
        
        for i in range(2,len(self.prefixsum)):
            self.prefixsum[i] += self.prefixsum[i-1]

    def sumRange(self,left:int,right:int):
        return self.prefixsum[right + 1] - self.prefixsum[left]