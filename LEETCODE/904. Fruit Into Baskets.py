from typing import Counter, List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r,ans,count = 0,0,0,0
        length = len(fruits)
        hm = Counter()
        while r < length:
            if len(hm) < 2:
                hm[fruits[r]] += 1
                r += 1
                count += 1
            else:
                if fruits[r] in hm:
                    r += 1
                    count += 1
                else:
                    for key in hm:
                        if key != fruits[r-1]:
                            wanted = key
                            
                    temp,sub = l,0
                    while temp < r:
                        if fruits[temp] == wanted:
                            l = temp 
                            count -= sub
                            sub = 0
                        temp += 1
                        sub += 1
                    hm[fruits[r]] += 1
                    l += 1
                    r += 1
                    del hm[wanted]
            ans = max(ans,count)
        return ans
obj = Solution()
fruits = [3,3,3,1,2,1,1,2,3,3,4]
obj.totalFruit(fruits)