class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        hm = defaultdict(int)
        prefix, ans, hm[0] = 0, 0, 1
        for v in nums:
            prefix += v
            x = prefix % k
            ans += hm[x]
            hm[x] += 1
        return ans


















        # hm = {0:1}
        # count,prefix = 0,0
        # for v in nums:
        #     prefix += v
        #     x = prefix % k
        #     if x in hm:
        #         count += hm[x]
        #     hm[x] = hm.get(x,0) + 1
        # return count