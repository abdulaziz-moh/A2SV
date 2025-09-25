t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    c = 0
    u = list(set(a))
    u.sort()
    lu = len(u)
    x = 0
    lft = []
    p = 0
    for i in range(n):
        if a[i] == k:
            c += 1

    while x <= n:
        if p < lu and u[p] == x:
            p += 1
        else:
            lft.append(x)
        x += 1
    m = 0
    for v in lft:
        if v < k:
            m += 1
        else:
            break
    print(max(m,c))