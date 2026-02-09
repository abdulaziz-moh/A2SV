class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        med = []
        for v in cnt:
            med.append([cnt[v],v])
        med.sort(key = lambda a:a[0], reverse = True)
        ans = []
        for i in range(k):
            ans.append(med[i][1])
        return ans

        