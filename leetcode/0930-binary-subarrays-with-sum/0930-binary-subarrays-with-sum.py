class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix, acc, n = [0], 0, len(nums)
        for v in nums:
            acc += v
            prefix.append(acc)

        l1, l2, count, right = 0, 0, 0, 1
        while right < n+1:
            while l1< right  and prefix[right] - prefix[l1] > goal:
                l1+= 1
            l2 = l1
            while l2 < right and prefix[right] - prefix[l2] == goal:
                l2 += 1
            val = prefix[right]
            while right < n + 1 and prefix[right] == val:
                count += (l2 - l1)
                if prefix[right] - prefix[l2] == goal:
                    l2 += 1
                right += 1
        return count
                 
            