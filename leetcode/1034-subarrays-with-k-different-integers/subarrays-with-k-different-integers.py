class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        left1, left2, count1, count2 = 0, 0, 0, 0
        unique1, unique2 = defaultdict(int), defaultdict(int)
        for right in range(len(nums)):
            unique1[nums[right]] += 1
            unique2[nums[right]] += 1

            while len(unique1) > k:
                unique1[nums[left1]] -= 1
                if unique1[nums[left1]] == 0:
                    del unique1[nums[left1]]
                left1 += 1
            count1 += (right - left1 + 1)

            while len(unique2) > k-1:
                unique2[nums[left2]] -= 1
                if unique2[nums[left2]] == 0:
                    del unique2[nums[left2]]
                left2 += 1
            count2 += (right - left2 + 1)
        return count1 - count2