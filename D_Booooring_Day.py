t = int(input())
for _ in range(t):
    n, l,r = map(int,input().split())
    a = list(map(int,input().split()))
    
    i, sum = 0, 0
    cnt = 0

    
    while i < n:
        while i < n and sum < l:
            sum += a[i]
            i += 1
        if sum >= l:
            if sum <= r:
                cnt += 1
        sum = 0
    print(cnt)
        
