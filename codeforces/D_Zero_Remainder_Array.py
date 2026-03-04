from collections import defaultdict


t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    
    rem = defaultdict(int)
    for v in a:
        temp = k - (v%k)
        if temp != k:
            rem[temp] += 1
    
    mx = 0
    for key,value in rem.items():
        temp = key + (value - 1) * k
        
        mx = max(mx,temp)
        
    if mx:
        print(mx+1)
    else:
        print(mx)