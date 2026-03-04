t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort()
    
    total = sum(a)
    idx = 0
    for v in b:
        idx += v
        if idx > n:
            break
        else:
            total -= a[idx - 1]
    print(total)