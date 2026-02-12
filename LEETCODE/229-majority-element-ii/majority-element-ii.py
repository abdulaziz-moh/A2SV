class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        candid = {}
        for v in nums:
            if len(candid) < 3:
                if v not in candid:
                    candid[v] = 1
                else:
                    candid[v] += 1
            elif v in candid:
                candid[v] += 1
            else:
                st = False
                x = -1
                for k,val in candid.items():
                    if val == 0:
                        x = k
                        x = k
                        st = True
                        break
                else:
                    for k in candid:
                        candid[k] -= 1
                if st:
                    del candid[x]
                    candid[v] = 1
        ans = [] 
        t = len(nums)//3
        for k in candid:
            if nums.count(k) > t:
                ans.append(k)
        return ans
