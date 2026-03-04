class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        med = []
        for v in cnt:
            med.append([cnt[v],v])
        med.sort(reverse = True)
        
        return [med[i][1] for i in range(k)]

        