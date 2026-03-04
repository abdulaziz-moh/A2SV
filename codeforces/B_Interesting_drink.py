from typing import Counter


n = int(input())
x = list(map(int,input().split()))
x.sort()
q = int(input())

for _ in range(q):
    m = int(input())
    l = 0
    r = n
    
    while l < r:
        md = (l+r)//2
        if x[md] <= m:
            l = md +1
        else:
            r = md

    print(l)