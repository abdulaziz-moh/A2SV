class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        t = len(nums)//3
        count = {}
        ans = set()
        for v in nums:
            if v in count:
                count[v] += 1
            else:
                count[v] = 1

            if count[v] > t:
                    ans.add(v)
        return list(ans)
            