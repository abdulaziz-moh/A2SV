class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x: abs(x[0] - x[1]), reverse = True)
        n = len(costs)//2
        city_one, city_two = n, n
        ans1, ans2 = 0, 0

        # print(costs)
        for one, two in costs:
            if city_one and one <= two:
                ans1 += one
                city_one -= 1
            
            elif city_two:
                ans2 += two
                city_two -= 1
            elif city_one:
                ans1 += one
                city_one -= 1
        # print(city_one)
        return ans1 + ans2