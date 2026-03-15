t = int(input())
for _ in range(t):
    n, m, v = map(int, input().split())
    a = list(map(int,input().split()))
    
    acc = 0
    forward, backward = [-1], [n]
    for i in range(n):
        acc += a[i]
        if acc >= v:
            forward.append(i)
            acc = 0
    acc = 0
    for i in range(n-1,-1,-1):
        acc += a[i]
        if acc >= v:
            backward.append(i)
            acc = 0
    if m >= len(forward):
        print(-1)
        continue
    
    prefix = [0]
    for v in a:
        prefix.append(prefix[-1] + v)
    prefix.append(0)
    
    mx = 0
    for i in range(m+1):
        temp = prefix[backward[i]] - prefix[forward[m-i]+1]
        mx = max(mx, temp)
    print(mx)