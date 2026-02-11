class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unqelements = set(nums)

        end = []
        for v in unqelements:
            if v-1 in unqelements and v+1 not in unqelements:
                end.append(v)
            elif v-1 not in unqelements and v+1 in unqelements:
                end.append(v)
        end.sort()
        mx = 1
        n = len(end)
        for i in range(0,n,2):
            mx = max(mx,( end[i+1]-end[i] + 1 ))
        return mx





[100,4,200,1,3,2]
[0,3,7,2,5,8,4,6,0,1]
[1,2,0,1]
[0]
[0,0]
[]
