t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    count = []
    for i in range(n):
        if a[i] < i+1:
            count.append(1)
        else:
            count.append(0)
    for i in range(1,n):
        count[i] += count[i-1]
    ans = 0
    for i in range(1,n):
        if a[i] < i+1:
            x = a[i] - 2
            if x >= 0:
                ans += count[a[i] - 2]
    print(ans)