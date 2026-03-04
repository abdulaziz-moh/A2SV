class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m, sum, ans = 1, 0, []
        for i in range(len(digits)-1,-1,-1):
            sum += digits[i] * m
            m *= 10
        sum += 1
        sum = str(sum)
        for v in sum:
            ans.append(int(v))
        return ans