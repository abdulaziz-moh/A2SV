from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    
    hm = defaultdict()
    for i in range(n):
        if s[i] in hm:
            hm[s[i]].append(i+1)
        else:
            hm[s[i]] = [i+1]
    # print(hm)
    ans = []
    for arr in hm.values():
        if len(arr) <= 1:
            print(-1)
            break
        
        for i in range(len(arr)-1):
            arr[i], arr[i+1] = arr[i+1], arr[i]
        ans.extend(arr)
    else:
        print(*ans)