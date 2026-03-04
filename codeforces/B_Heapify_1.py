t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    h = n//2 + 1
    
    for i in range(1, h):
        if i % 2 == 0:
            continue
        next = i
        arr = []
        while next <= n:
            arr.append(a[next -1 ])
            next *= 2
        arr.sort()
        next = i
        for v in arr:
            a[next-1] = v
            next *= 2
    for i in range(n-1):
        if a[i] > a[i+1]:
            print('NO')
            break
    else:
        print('YES')