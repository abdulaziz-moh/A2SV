class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # idx = n-1
        ans = []
        for i in range(n-1,0,-1):
            mx = max(arr[:i+1])
            if mx == arr[i]:
                continue
            elif mx == arr[0]:
                ans.append(i+1)
                temp = (arr[:i+1])
                temp.reverse()
                for j in range(i+1):
                    arr[j] = temp[j]
                continue
            for j in range(i):
                if arr[j] == mx:
                    ans.append(j+1)
                    ans.append(i+1)
                    temp = arr[j+1:i+1]
                    a,b = i,j
                    while b >= 0:
                        arr[a] = arr[b]
                        b -= 1
                        a -= 1
                    for k in range(len(temp)):
                        arr[a] = temp[k]
                        a -= 1
                    break
        print(arr)
        return ans