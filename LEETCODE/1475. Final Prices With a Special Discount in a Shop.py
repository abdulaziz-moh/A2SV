class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = prices.copy()
        discount = [0]*len(prices)
        n = len(prices)
        for i in range(n-2,-1,-1):
            v = stack.pop()
            j = i
            while j >= 0 and v <= prices[j]:
                discount[j] = v
                j -= 1
        for i in range(n):
            discount[i] = prices[i] - discount[i]
        return discount