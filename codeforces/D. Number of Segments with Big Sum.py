n,s = map(int,input().split())
a = list(map(int,input().split()))
l,r = 0,0
sum,ans = 0,0
for r in range(n):
    sum += a[r]
    if sum >= s:
        while sum >= s:
            ans += (n-r)
            sum -= a[l]
            l += 1
print(ans)