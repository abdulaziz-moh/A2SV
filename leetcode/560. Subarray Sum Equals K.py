class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix,count = 0,0
        hm ={0:1}
        for v in nums:
            prefix += v
            if prefix == k or prefix - k in hm:
                count += hm[prefix-k]
            hm[prefix] = hm.get(prefix,0) + 1
        return count