n,s = map(int,input().split())
a = list(map(int,input().split()))

l , window, sum, ans = 0,0,0,0
for r in range(n):
    sum += a[r]
    window += 1
    while sum > s:
        sum -= a[l]
        l += 1
        window -= 1
    ans += window
print(ans)