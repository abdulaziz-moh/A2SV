class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snum = sorted(nums)
        cnt, eq = 0, 0
        hm = {}
        hm[snum[0]] = 0
        for i in range(1,len(nums)):
            if snum[i] != snum[i-1]:
                cnt += (eq + 1)
                eq = 0
                hm[snum[i]] = cnt
                continue
            hm[snum[i]] = cnt
            eq += 1
        return [hm[v] for v in nums]