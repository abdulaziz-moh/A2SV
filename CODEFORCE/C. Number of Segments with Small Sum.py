n,s = map(int,input().split())
a = list(map(int,input().split()))

r,l = 0,0
sum,ans = 0,0
for r in range(n):
    
    sum += a[r]
    while sum > s:
        sum -= a[l]
        l += 1
    ans += (r - l + 1)
print(ans)