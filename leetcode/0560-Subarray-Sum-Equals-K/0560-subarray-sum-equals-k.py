class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        unique = defaultdict(int)
        prefix, count, unique[0] = 0, 0, 1
        
        for num in nums:
            prefix += num
            x = prefix - k
            if x in unique:
                count += unique[x]
            unique[prefix] += 1
        return count