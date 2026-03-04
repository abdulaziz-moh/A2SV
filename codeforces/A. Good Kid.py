t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    y = min(a)
    ans = 1
    start = 0
    for i, x in enumerate(a):
        if x == y:
            ans *= (x + 1)
            start = i+1
            break
        ans *= x
    for i in range(start,n):
        ans *= a[i]
    print(int(ans))