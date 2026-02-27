n,s = map(int,input().split())
a = list(map(int,input().split()))

l , rem, sum, ans = 0,n+1,0,0
for r in range(n):
    sum += a[r]
    rem -= 1
    if sum < s:
        continue
    while sum >= s:
        sum -= a[l]
        l += 1
        ans += (rem)
print(ans)