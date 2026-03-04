class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n =len(nums)
        count = defaultdict(int)
        mx = [0,0]
        for v in nums:
            count[v] += 1
            if count[v] > mx[1]:
                mx = [v,count[v]]

        if mx[1] <= (n//2):
            return -1
        count = defaultdict(int)
        mid = n
        for i in range(n):
            count[nums[i]] += 1
            if count[mx[0]] > (i+1)//2:
                mid = i
                break
        print(mid)
        rightCount = Counter(nums[i+1:])
        if mid != n and rightCount[mx[0]] > (n - mid - 1)//2:
            return mid
        return -1


[1,1,1,1,1,1,1,1]
            