from typing import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        imp = input()
        a = []
        for v in imp:
            a.append(int(v))
        arr.append(a)
    
    count = 0
    l = 0
    r = n - 1
    
    while l < r:
        for i in range(l,r):
            newarr = [arr[i][l], arr[r][i], arr[n-1 - i][r], arr[l][n-1-i]]
            hm = {0:0,1:0}
            for v in newarr:
                hm[v] += 1
            count += min(hm.values())
        l += 1
        r -= 1        
    print(count)