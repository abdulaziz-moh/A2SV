from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = []  # answer to be returned
        n = len(arr)
        for i in range(n-1):
            idx = arr.index(max(arr[:n-i])) + 1 # find the max element's index
            k.append(idx)  # each time we find the relative max we append it's index+1(first reverse to make max at first) and n-i (second reverse to make the max element bubble)
            k.append(n-i)
            temp = arr[:idx][::-1]
            for j in range(len(temp)):  # reverse from first to max index making the max index at first
                arr[j] = temp[j]
            temp = arr[:n-i][::-1]
            for j in range(len(temp)): # reverse from first to n-i(the currunt max position like bubble sort) resulting the max to bubble
                arr[j] = temp[j]   
        return(k)

        
        
        

obj = Solution()
arr = [3,2,4,1]
obj.pancakeSort(arr)