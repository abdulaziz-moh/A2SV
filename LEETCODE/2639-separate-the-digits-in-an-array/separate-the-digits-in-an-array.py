class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            temp = str(num)
            for v in temp:
                ans.append(int(v))
        return ans