class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        count = 0
        num,i = 0,0
        while count < k:
            num += 1
            if num != arr[i]:
                count += 1
            elif i < n-1:
                i += 1   
        return num