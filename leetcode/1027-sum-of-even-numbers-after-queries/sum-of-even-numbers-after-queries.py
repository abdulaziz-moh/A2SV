class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even = 0
        ans = []
        for v in nums:
            if v % 2 == 0:
                even += v
        for q in queries:
            if nums[q[1]] % 2 == 0:
                even -= nums[q[1]]
            nums[q[1]] += q[0]
            if nums[q[1]] % 2 == 0:
                even += nums[q[1]]
            ans.append(even) 
        return ans