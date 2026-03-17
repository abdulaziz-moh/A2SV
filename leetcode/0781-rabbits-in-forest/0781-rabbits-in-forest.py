class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        count = Counter(answers)

        for key, val in count.items():
            ans += math.ceil(val/(key+1)) * (key + 1)
        return ans 
