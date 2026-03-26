class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def find(l,r):
            if l >= r:
                return nums[l]

            a = nums[l] - find(l+1, r)
            b = nums[r] - find(l, r-1)
            
            return max(a,b)

        x = find(0, len(nums)-1)
        return x >= 0