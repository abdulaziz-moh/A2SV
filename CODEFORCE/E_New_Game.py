from typing import Counter


t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    
    a.sort()
    hm = Counter(a)
    arr = []
    for key,v in hm.items():
        arr.append([key,v])
    arr.sort()

    l, r, x = 0,0,k
    sum, mx = 0,0
    while r < len(arr):
        while r < n and x > 0:
            sum += arr[r][1]
            x -= 1
            if arr[r][0] + 1 not in hm:
                mx = max(mx,sum)
                sum = 0
                r += 1
                l = r
                x = k
                break
            r += 1
        else:
            
            mx = max(mx,sum)
            sum -= arr[l][1]
            l += 1
            x = 1

    print(mx)