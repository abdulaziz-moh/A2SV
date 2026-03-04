# this is a premium leetcode problem
class Solution:
    def solve(self,s,k):
        unique = set()
        n,l,count = len(s),0,0
        
        for i in range(n):
            if s[i] in unique:
                while s[i] in unique:
                    unique.remove(s[l])
                    l += 1
            elif i-l >= k:
                unique.remove(s[l])
                l += 1
            unique.add(s[i])
            if len(unique) == k:
                count += 1
        return count

obj = Solution()
s = "havefunonleetcode"  # result = 6
k = 5
# s = "home"   # result = 0 
# k = 5          
print(obj.solve(s,k))
        
