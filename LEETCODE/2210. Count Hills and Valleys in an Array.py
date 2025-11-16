class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        n = len(nums)
        m,l,r = 0,0,0
        count = 0

        while r < n:
            while m < n and nums[m] == nums[l]:
                m+= 1
            l = m- 1
            r = m+ 1
            if r < n and nums[l] < nums[m]:
                while r < n and nums[r] >= nums[m]:
                    r += 1
                    m+= 1
                if r != n:
                    count += 1
                    l = m

            elif  r < n and nums[l] > nums[m]:
                while r < n and nums[r] <= nums[m]:
                    r += 1
                    m+= 1
                if r != n:
                    count += 1
                    l = m

        return count