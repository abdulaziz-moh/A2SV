t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    sum = 0
    for i in range(0, 2*n, 2):
        sum += a[i]
    print(sum)