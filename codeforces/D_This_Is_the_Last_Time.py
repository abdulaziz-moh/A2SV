t = int(input())
for _ in range(t):

    n, k = map(int, input().split())
    casino = []
    for _ in range(n):
        a = list(map(int, input().split()))
        casino.append(a)
    casino.sort(key= lambda x:x[0])
    for v in casino:
        if v[0] <= k <= v[1] and v[2] > k:
            k = v[2]
    print(k)