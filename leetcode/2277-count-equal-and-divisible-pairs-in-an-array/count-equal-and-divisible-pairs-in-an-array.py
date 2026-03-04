class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        idxpair = defaultdict(list)
        count = 0
        for i in range(len(nums)):
            idxpair[nums[i]].append(i)
        for arr in idxpair.values():
            if len(arr) > 1:
                for i in range(len(arr)-1):
                    for j in range(i+1, len(arr)):
                        if (arr[i] * arr[j]) % k == 0:
                            count += 1
        return count
